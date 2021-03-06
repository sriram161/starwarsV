import werkzeug
werkzeug.cached_property = werkzeug.utils.cached_property
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restplus import Api

class Server(object):
    """ Setup and configure flask application.
    """
    def __init__(self):
        self.app = Flask(__name__)
    
    def config_app(self):
        self.app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database/test1.db'
        self.app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
    def setup_database(self):
        self.db = SQLAlchemy(self.app)
    
    def get_db(self):
        return self.db

    def get_api(self):
        return self.api

    def drop_all_tables(self):
        self.db.drop_all()

    def create_all_tables(self):
        self.db.create_all()

    def start(self, debug_=False, host_ ='0.0.0.0', port_=8080):
        self.app.run(debug=debug_, host=host_, port=port_)

    def setup_api(self):
        self.api = Api(self.app, version='1.0', title='Starwars films.', description='get all the starwars films.')
        from services.films import Films
        from services.characters import Characters
        self.api.add_resource(Films, '/films', endpoint='films')
        self.api.add_resource(Characters, '/characters', endpoint='characters')

server = Server()
server.config_app()
server.setup_database()
db = server.get_db()

class Tcharacters(db.Model):
    """ ORM tables definiton for charactes table on database.
    """
    __tablename__ = 'characters'
    id = db.Column(db.Integer, primary_key=True)
    id_ = db.Column(db.Integer, nullable=False)
    name = db.Column(db.String(80), nullable=False)
    lastupdate = db.Column(db.DateTime, nullable=False)
    filmid = db.Column(db.Integer, nullable=False)

    def __init__(self, id_, name, lastupdate, filmid):
        self.id_ = id_
        self.name = name
        self.lastupdate = lastupdate
        self.filmid = filmid


class Tfilms(db.Model):
    """ ORM tables definiton for films table on datbase.
    """
    __tablename__ = 'films'
    id_ = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=False)
    releasedate = db.Column(db.String(30), nullable=False)
    lastupdate = db.Column(db.DateTime, nullable=False)

    def __init__(self, id_, title, releasedate, lastupdate):
        self.id_ = id_
        self.title = title
        self.releasedate = releasedate
        self.lastupdate = lastupdate

if __name__ == "__main__":
    server.drop_all_tables()
    server.create_all_tables()
    server.setup_api()
    server.start()
