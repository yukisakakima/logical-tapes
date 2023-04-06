import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

login_manager = LoginManager() #Flask-Loginライブラリとアプリケーションを繋ぐ
#ログインの関数
login_manager.login_view = 'app.login'
#ログインにリダイレクトしたさいのメッセージ
login_manager.login_message = 'Please login.'

basedir = os.path.abspath(os.path.dirname(__name__))
db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config['SCRET_KEY'] = 'mysite'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + \
        os.path.join(base_dir, 'data.sqlite')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # アプリにBlueprintオブジェクトを登録
    from flaskr.views import bp
    app.register_blueprint(bp)

    # DBを使用するアプリケーションを初期化
    db.init_app(app)

    # migrationするflaskアプリとDBを初期化
    migrate.init_app(app, db)

    # loginManagerを初期化
    login_manager.init_app(app)
    return app