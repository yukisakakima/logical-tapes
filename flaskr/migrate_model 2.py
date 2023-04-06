#migrate_model.py
import email
import os
from unicodedata import name
from click import password_option
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from datetime import datetime
import pytz

base_dir = os.path.dirname(__file__)

app = Flask(__name__)

# sqliteのファイル保存先を指定
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(base_dir, 'migrate_data.sqlite')

# モデルに変更があった場合にシグナル送出の有無を設定する
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# appに設定した内容でDBに接続する
db = SQLAlchemy(app)
Migrate(app, db)

# モデルクラスの定義にはdb.Modelクラスを継承する必要がある。
class UserInfo(db.Model):

    __tablename__ = "user_info"

    # 作成するテーブルのカラムを定義
    id = db.Column(db.Integer, primary_key=True) # 主キー
    first_name = db.Column(db.Text)
    last_name = db.Column(db.Text)
    email = db.Column(db.Text)
    password = db.Column(db.Text)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.now(pytz.timezone("Asia/Tokyo")))

    def __init__(self, first_name, last_name, email, password):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password

    def __str__(self):
        return f"id = {self.id}, name={self.first_name}, age={self.last_name}, email={self.email}, password={self.password}, created_at={self.created_at}"