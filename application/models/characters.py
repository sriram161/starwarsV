from server import db

class Tcharacters(db.Model):
    __tablename__ = 'characters'
    id_ = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    lastupdate = db.Column(db.DateTime, nullable=False)

    def __init__(id_, name, lastupdate):
        self.id_ = id_
        self.name = name
        self.lastupdate = lastupdate
