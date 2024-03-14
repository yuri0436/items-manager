# ITEMS-MANAGER
商品情報を管理するためのWebAPIです。
<br>商品情報を取得・登録・更新・削除などのCRUD処理が全て実装されています。

## Development Environment
■OS環境
<br>Windows 11
<br>
<br>■使用技術
<br>バックエンド
<br>・Python 3.12.2
<br>データベース
<br>・Postgresql 16.2
<br>フレームワーク
<br>・FastAPI
<br>・Pytest

## Getting Started
○インストール手順
<br>&emsp; ITEMS-MANAGERをお使いいただくにあたり、動作環境を構築していただく必要があります。
<br>&emsp; 環境構築の手順については「環境構築手順.pdf」を参考に環境構築を行ってください。
<br>
<br>○ツールの機能紹介と基本的な使い方
<br>&emsp; ITEMS-MANAGERは以下の機能を実装しています。
<br>
<br>■機能一覧
<br>・ログイン認証
<br>・ユーザー登録
<br>・検索(商品ID・キーワード検索)
<br>・商品登録
<br>・商品更新
<br>・商品削除
<br>
<br>機能紹介と基本的な使い方については「ITEMS-MANAGER.pdf」で紹介しております。
<br>動作検証の際は、是非ご参照ください。


## Database
ITEMS-MANAGERでは、以下のテーブルを使用します。
<br>
<br>■itemsテーブル
| No  | PK  | FK  | カラム名    | 項目名                 | データ型 | NOT NULL | 列制約      | 備考                                            | 
| --- | :-: | :-: | ----------- | ---------------------- | -------- | :-:  | ----------- | ----------------------------------------------- | 
| 1   | 〇  | -   | id          | 商品ID                 | int      | 〇       | primary_key | 自動採番                                        | 
| 2   | -   | -   | name        | 商品名                 | String   | 〇       | -           | 2文字以上20文字以内の文字列が入るように入力規制 | 
| 3   | -   | -   | price       | 価格                   | int      | 〇       | -           | 1円以上の金額が入るように入力規制               | 
| 4   | -   | -   | description | 商品説明               | String   | -        | -           |                                                 | 
| 5   | -   | -   | category    | 商品カテゴリー(大分類) | String   | 〇       | -           | ItemCategory(Enum)                              | 
| 6   | -   | -   | status      | 商品ステータス         | String   | 〇       | -           | ItemStatus(Enum)                                | 
| 7   | -   | -   | stock       | 在庫                   | int      | 〇       | -           |                                                 | 
| 8   | -   | -   | created_at  | 作成日時               | datetime | 〇       | -           | デフォルトで現在日時を登録                              | 
| 9   | -   | -   | updated_at  | 編集日時               | datetime | 〇       | -           | デフォルトで現在日時を登録                             | 
| 10  | -   | 〇  | user_id     | ユーザーID             | int      | 〇       | foreign_key | 外部キー：User.id                               | 

<br>■usersテーブル
| No  | PK  | FK  | カラム名   | 項目名         | データ型 | NOT NULL | 列制約      | 備考                                       | 
| --- | :-: | :-: | ---------- | :------------- | :------- | :------: | :---------: | ------------------------------------------ | 
| 1   | 〇  | -   | id         | ユーザーID     | int      | 〇       | primary_key | 自動採番<br>外部キー：Item.user_id         | 
| 2   | -   | -   | username   | ユーザー名     | String   | 〇       | unique      |                                            | 
| 3   | -   | -   | password   | パスワード     | String   | 〇       | -           | sha256でハッシュ化                         | 
| 4   | -   | -   | salt       | ランダム文字列 | String   | 〇       | -           | ランダム文字列を加えてpasswordをハッシュ化 | 
| 5   | -   | -   | created_at | 作成日時       | datetime | 〇       | -           | デフォルトで現在日時を登録                 | 
| 6   | -   | -   | updated_at | 編集日時       | datetime | 〇       | -           | デフォルトで現在日時を登録                 | 


## Test
Pytestフレームワークを導入し、テストの自動化を行いました。
<br>テスト項目一覧・テスト実行方法については「WebAPIテストについて.pdf」をご参照ください。




