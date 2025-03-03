from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class SocialData(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    platform = db.Column(db.String(50), nullable=False)
    followers = db.Column(db.Integer, nullable=False)

    def __init__(self, platform, followers):
        self.platform = platform
        self.followers = followers