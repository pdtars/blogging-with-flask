from app import app, db

from app.models import User, Post


#The following function in microblog.py creates a shell context that adds 
# the database instance and models to the shell session. use flask shell in the cmd, digita depois 
# db, User ou Post
@app.shell_context_processor
def make_shell_context():
    return {'db':db, 'User':User, 'Post':Post}
