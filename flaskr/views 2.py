from flask import Blueprint, request, render_template, redirect, url_for
from flask_login import login_user, login_required, logout_user
from flaskr.forms import LoginForm, RegisterForm
from flaskr.models import User

bp = Blueprint('app', __name__, url_prefix='')

@bp.route('/')
def home():
    return render_template('home.html')

# login_requiredにより、login_userが実行されていない場合以下の関数は実行されない。
# ログインしていない場合は、__init__.pyのlogin_viewに指定されている処理に遷移する。
@bp.route('/welcome')
@login_required
def welcome():
    return render_template('welcome.html')

@bp.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm(request.form)
    if request.method == 'POST' and form.validate():
        user = User.select_by_email(form.email.data)

        if user and user.validate_password(form.password.data):
            # login_user関数にユーザー名を渡すことでログイン処理を実行する。
            # remember=Trueとすることで、ブラウザを閉じてもsession情報を残す事が可能。
            login_user(user, remember=True)
            # このログインメソッドを呼び出した処理が本来の遷移先として指定していた
            # ページ(url)を取得する。
            next = request.args.get('next')
            if not next:
                next = url_for('app.welcome')

            return redirect(next)
    return render_template('login.html', form=form)