from libs.orm import db

class Article(db.Model):
    __tablename__ = 'article'

    id = db.Column(db.Integer,primary_key=True)
    title = db.Column(db.String(20),nullable=False)
    content = db.Column(db.Text,nullable=False)
    created_time = db.Column(db.DateTime)