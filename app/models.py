from datetime import datetime
from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    posts = db.relationship('Post', backref='author', lazy='dynamic')

    def __repr__(self):
        '''For Debug only. tells Python how to print objects of this class, 
        which is going to be useful for debugging
        eg. 
        from app.models import User
        u = User(username='susan', email='susan@example.com')
        u
        <User susan>
        '''
        return f'<User {self.username}>'

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String(140))
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow) #pass func itself, not calling it
    user_id = db.Column(db.Integer, db.ForeignKey('user.id')) 
    # SQLAlchemy por padrao faz snakecase na hora de criar as tableas
    # Ficar ligado para diferenciar quando eh a model class (User) e a tabela (user)
    def __repr__(self):
        return f'<Post {self.body}>'