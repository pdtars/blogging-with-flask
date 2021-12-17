from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))

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