from flask import  Blueprint
from flask import request
from flask import session
from flask import render_template

from user.model import User
from libs.orm import db

#定义 Blueprint 对象
user_dp = Blueprint('user',__name__,url_prefix='/user')
user_dp.template_folder = './templates'


@user_dp.route('/register',methods=('POST','GET'))
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        gender = request.form.get('gender')
        age = request.form.get('age')
        city = request.form.get('city')
        phone = request.form.get('phone')

        user = User(username=username,password=password,gender=gender,
                    age=age,city=city,phone=phone)
        db.session.add(user)
        db.session.commit()
        return render_template('/user/login')


    else:
        return render_template('register.html')
