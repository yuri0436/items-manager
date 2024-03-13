from pydantic_settings import BaseSettings, SettingsConfigDict
from functools import lru_cache

#設定ファイルを読み込む
class Settings(BaseSettings):
    secret_key: str
    sqlalchemy_database_url: str

    model_config = SettingsConfigDict(env_file=".env")


@lru_cache()
def get_settings():
    return Settings()