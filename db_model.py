from main import db



class User(db.Model):
    user_id = db.Column(db.String(80), primary_key=True)
    user_password = db.Column(db.String(120), unique=True)
    user_email = db.Column(db.String(120))

    def __init__(self, user_id, user_password, user_email=None):
        self.user_id = user_id
        self.user_password = user_password
        self.user_email = user_email

    def __repr__(self):
        return '<User %r>' % self.user_id