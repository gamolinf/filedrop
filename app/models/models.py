from app import db
from datetime import datetime

class Image(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    filename = db.Column(db.String(256), nullable=False, unique=True)
    upload_date = db.Column(db.DateTime, default=datetime.now)
    url = db.Column(db.String(512), nullable=False, unique=True)

    def __repr__(self):
        return f'<Image {self.filename}>'
