import os
from flask import Flask, render_template, redirect, request, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import pytz

app = Flask(__name__)

#ファイルのパス
base_dir = os.path.dirname(__file__)

# sqliteのファイル保存先を指定
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(base_dir, 'data.sqlite')

# モデルに変更があった場合にシグナル送出の有無を設定する
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# appに設定した内容でDBに接続する
db = SQLAlchemy(app)

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











##### Flaskを用いてCSSを反映させるもの #####
#src:https://qiita.com/kujirahand/items/896ea20b28ee2ed96311
@app.context_processor
def override_url_for():
    return dict(url_for=dated_url_for)

def dated_url_for(endpoint, **values):
    if endpoint == 'static':
        filename = values.get('filename', None)
        if filename:
            file_path = os.path.join(app.root_path,
                                endpoint, filename)                        
            values['q'] = int(os.stat(file_path).st_mtime)
    return url_for(endpoint, **values)


##### 基本ルーティング #####


@app.route("/", methods=["GET", "POST"]) #methods=["GET", "POST"]でGETもPOSTも対応してくれる
def home(): 
    add_to_the_title = "Home"
    if request.method == "GET":
        user_info = UserInfo.query.all()
    return render_template("home.html", add_to_the_title=add_to_the_title, user_info=user_info)

@app.route("/merch")
def merch():
    add_to_the_title = "Merch"
    return render_template("merch.html", add_to_the_title=add_to_the_title)

@app.route("/about")
def about():
    add_to_the_title = "About"
    return render_template("about.html", add_to_the_title=add_to_the_title)

@app.route("/terms")
def terms():
    add_to_the_title = "Terms"
    return render_template("terms.html", add_to_the_title=add_to_the_title)

@app.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        first_name = request.form.get("first_name")
        last_name = request.form.get("last_name")
        email = request.form.get("email")
        password = request.form.get("password")

        user_info = UserInfo(first_name=first_name, last_name=last_name, email=email, password=password)

        db.session.add(user_info)
        db.session.commit()
        return redirect("/")
    else:
        add_to_the_title = "Sign Up"
        return render_template("signup.html", add_to_the_title=add_to_the_title)

@app.route("/signin")
def signin():
    add_to_the_title = "Sign In"
    return render_template("signin.html", add_to_the_title=add_to_the_title)

@app.route("/cart")
def cart():
    add_to_the_title = "Cart"
    return render_template("cart.html", add_to_the_title=add_to_the_title)

# @app.errorhandler(404)    
# def redirect_main_page(error):
    # return render_template("home.html")
    #return redirect(url_for("home"))#url_forの引数の関数に遷移

if __name__ == "__main__":
    app.run(debug=True)