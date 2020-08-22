from libs.orm import db

#创建User模型
class User(db.Model):
    __tablename__ = 'user_info'

    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(10),unique=True,nullable=False)
    password = db.Column(db.String(16),nullable=False)
    gender = db.Column(db.Enum('男','女'),default='男')
    age = db.Column(db.Integer,default=24)
    city = db.Column(db.String(20),default='上海')
    phone = db.Column(db.String(16))