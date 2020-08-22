from flask import  Blueprint
from flask import request
from flask import session
from flask import redirect
from flask import render_template

from user.model import User
from libs.orm import db

#定义 Blueprint 对象
user_dp = Blueprint('user',__name__,url_prefix='/user')
user_dp.template_folder = './templates'


#注册页面
@user_dp.route('/register',methods=('POST','GET'))
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        gender = request.form.get('gender')
        age = request.form.get('age')
        city = request.form.get('city')
        phone = request.form.get('phone')
        try:
            user = User.query.filter_by( username = username ).one()
            if user :
                return '用户名已存在'
        except Exception:
            user = User(username=username,password=password,gender=gender,
                        age=age,city=city,phone=phone)
            db.session.add(user)
            db.session.commit()

        return redirect('/user/login')


    else:
        return render_template('register.html')

#登录页面
@user_dp.route('/login',methods=('POST','GET'))
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        try:
            user = User.query.filter_by(username = username).one()
            if password != user.password:
                return '密码错误，请重新输入'
            session['user_id'] = user.id
        except Exception:
            return '用户名不存在'

        return redirect('/user/info')

    else:
        return render_template('login.html')


#用户信息页面
@user_dp.route('/info')
def user_info():
    uid = session.get('user_id')
    if  not uid:
        return '您还没有登录，请先登录'
    else:
        user = User.query.filter_by(id=uid).one()
        return render_template('user_info.html',user=user)
