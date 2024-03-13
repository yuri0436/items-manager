import os
import sys

#親ディレクトリのファイルを取得
app_dir = os.path.join(os.path.dirname(__file__), "..")
sys.path.append(app_dir)

import pytest
from fastapi.testclient import  TestClient
from sqlalchemy import create_engine
from sqlalchemy.pool import StaticPool
from sqlalchemy.orm import Session, sessionmaker
from models import Base, Item
from schemas import ItemCategory, ItemStatus, DecodedToken
from main import app
from database import get_db
from cruds.auth import get_current_user


#データベース(SQLite)設定
@pytest.fixture()
def session_fixture():
    engine = create_engine(
        url="sqlite://",
        connect_args={"check_same_thread": False},
        poolclass=StaticPool
    )
    Base.metadata.create_all(engine)
    #セッションを作成
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    db = SessionLocal()
    #初期データを作成
    try:
        item1 = Item(
            name="PC1", price=100000, description="test1", category=ItemCategory.PC, 
            status=ItemStatus.ORIGINAL_PRICE, stock=100, user_id = "1"
            )
        item2 = Item(
            name="PC2", price=100000, description="test2", category=ItemCategory.PC, 
            status=ItemStatus.ORIGINAL_PRICE, stock=100, user_id = "2"
            )
        db.add(item1)
        db.add(item2)
        db.commit()
        yield db
    finally:
        db.close()



#ダミーの認証済みユーザー情報を返却
@pytest.fixture()
def user_fixture():
    return DecodedToken(username="users1", user_id=1)

#テスト用クライアントを生成
@pytest.fixture()
def client_fixture(session_fixture: Session, user_fixture: DecodedToken):
    def override_get_db():
        return session_fixture
    
    def override_get_current_user():
        return user_fixture
    #テスト用に上書き
    app.dependency_overrides[get_db] = override_get_db
    app.dependency_overrides[get_current_user] = override_get_current_user

    client = TestClient(app)
    yield client
    #上書きした設定を消去
    app.dependency_overrides.clear()

    