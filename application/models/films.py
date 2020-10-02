from server import db

class Tfilms(db.Model):
    __tablename__ = 'films'
    id_ = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=False)
    releasedate = db.Column(db.DateTime, nullable=False)
    lastupdate = db.Column(db.DateTime, nullable=False)
    
    def __init__(self, id_, title, releasedate, lastupdate):
        self.id_ = id_
        self.title = title
        self.releasedate = releasedate 
        self.lastupdate = lastupdate
