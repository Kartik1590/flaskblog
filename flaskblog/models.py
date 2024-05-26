from flaskblog import db,login_manager
from datetime import datetime as dt
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model,UserMixin):
    id=db.Column(db.Integer,primary_key=True)
    username=db.Column(db.String(20),unique=True,nullable=False)
    email=db.Column(db.String(120),unique=True,nullable=False)
    image_file=db.Column(db.String(20),default='default.jpg')
    password=db.Column(db.String(60),nullable=False)
    post=db.relationship('Post',backref='author',lazy=True)
    # gf=db.relationship('Girlfriend',backref='author',lazy=True)
    
    def __repr__(self):
        return f"User('{self.username}','{self.email}')"
    
class Post(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    title=db.Column(db.String(100),nullable=False)
    date=db.Column(db.DateTime,nullable=False,default=dt.now)
    content=db.Column(db.Text,nullable=False)
    user_id=db.Column(db.Integer,db.ForeignKey('user.id'),nullable=False)
    
    
    def __repr__(self):
        return f"User('{self.title}','{self.date}')"
    
# class Girlfriend(db.Model):
#     id=db.Column(db.Integer,primary_key=True)
#     name=db.Column(db.String(30),nullable=False)
#     age=db.Column(db.Integer,nullable=False)
#     active=db.Column(db.Boolean)
#     user_id=db.Column(db.Integer,db.ForeignKey('user_id'),nullable=False)

#     def __repr__(self):
#         return f"GirlFriend('{self.name}', '{self.active}')"
