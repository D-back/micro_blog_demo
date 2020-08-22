import datetime

from flask import Blueprint
from flask import session
from flask import render_template
from flask import redirect
from flask import request


from libs.orm import db
from article.model import Article
from user.model import User

#创建文章的蓝图
article_dp = Blueprint('article',__name__,url_prefix='/article')
article_dp.template_folder = './templates'

#创建文章页面
@article_dp.route('/create',methods=('POST','GET'))
def create_article():
    if request.method == 'POST':
        title = request.form.get('title')
        content = request.form.get('content')
        create_time = datetime.datetime.now()
        if title and content :
            article = Article(title=title,content=content,created_time=create_time)
            db.session.add(article)
            db.session.commit()
        else:
            return '标题和内容都不能为空'
        session['title'] = title

        return redirect('/article/show')


    else:
        uid = session.get('user_id')
        if uid:
            return render_template('create_article.html')
        else:
            return redirect('/user/login')

@article_dp.route('/show')
def show_article():
    title = session.get('title')
    if not title:
        return redirect('/article/create')
    else:
        article = Article.query.filter_by(title=title).one()
        return render_template('show_article.html',article=article)

