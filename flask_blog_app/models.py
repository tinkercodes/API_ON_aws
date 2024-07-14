from flask_blog_app import db
from datetime import datetime

class Blog(db.Model):
    blog_id = db.Column(db.Integer,primary_key=True)
    title = db.Column(db.String(50),nullable=False)
    content = db.Column(db.Text,nullable=False)
    created_on = db.Column(db.DateTime,default=datetime.utcnow)
    u_id = db.Column(db.Integer,db.ForeignKey('user.user_id'))
    def __repr__(self):
        return '{}, {}, {}, {}, {}'.format(str(self.blog_id),self.title,self.content,self.created_on,str(self.u_id))

class User(db.Model):
    user_id = db.Column(db.Integer,primary_key=True)
    user_name = db.Column(db.String(50))
    def __repr__(self):
        return '{}, {}'.format(str(self.user_id),self.user_name)