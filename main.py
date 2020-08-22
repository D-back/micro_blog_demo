from flask import Flask
from flask import redirect
from flask_script import Manager
from flask_migrate import Migrate,MigrateCommand


#从自己的包中导入SQLAlchemy 实例db对象
from libs.orm import db
from user.views import user_dp




app = Flask(__name__)    #创建了一个app模型

#app连接数据库的配置
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:961224@localhost:3306/micro_blog_demo'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
#初始化app对象
db.init_app(app)


#定义manager对象
manager = Manager(app)

#为app绑定数据库迁移工具
migrate = Migrate(app,db)
manager.add_command('db',MigrateCommand)


app.register_blueprint(user_dp)


@app.route('/')
def home():
    return redirect('/user/register')


if __name__ == '__main__':
    manager.run()