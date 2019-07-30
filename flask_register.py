from flask import Flask, render_template,flash,redirect,url_for,request
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from flask_login import LoginManager
import os
from flask_bcrypt import Bcrypt
from config import Config



pjdir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__)
app.config.from_object(Config)
bcrypt = Bcrypt(app)
db = SQLAlchemy(app)
bootstrap = Bootstrap(app)


#  新版本的部份預設為none，會有異常，再設置True即可。
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
#  設置資料庫為sqlite3
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + \
                                        os.path.join(pjdir, 'register.sqlite')
app.config['SECRET_KEY']=b'\xa0\x18a\xb0\xb1\x04\xf2B\x182\x0f~\x82d\x8a\x11\xa0\x97\x19\xa1\x8a\x89\x19\x9e'

@app.route('/')
def index():
    flash('6/12(三)貳樓中山南西店正式開幕~~~~')
    flash('6/15(六)警察節活動優惠開跑!!!')
    return render_template('base.html')

@app.route('/login',methods = ['GET','POST'])
def login():
    from form import FormLogin
    from model import UserRegister

    formd=FormLogin()
    if formd.validate_on_submit():
        user = UserRegister.query.filter_by(email=formd.email.data).first()
        if user:
            #  當使用者存在資料庫內再核對密碼是否正確。
            if user.check_password(formd.password.data):
                return 'Welcome'
            else:
                #  如果密碼驗證錯誤，就顯示錯誤訊息。
                return('Wrong Email or Password')
        else:
            #  如果資料庫無此帳號，就顯示錯誤訊息。
            return('No Email')

    return render_template('Login.html',formdetail=formd)


@app.route('/logout')
def logout():
    return render_template('sf.html')


@app.route('/store')
def store():
    return render_template('store.html')


@app.route('/about')
def about():

    return render_template('info.html')



@app.route('/register',methods = ['GET','POST'])
def register():
    from form import FormRegister
    from model import UserRegister
    form = FormRegister()
    if form.validate_on_submit():
        user = UserRegister(username = form.username.data,email = form.email.data,password = form.password.data)
        db.session.add(user)
        db.session.commit()
        return 'Success'
    return render_template('register.html',formdetail=form)




login = LoginManager(app)
login.login_view = 'login'

if __name__ == '__main__':
    app.debug = True
    app.run()
