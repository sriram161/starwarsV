import werkzeug
werkzeug.cached_property = werkzeug.utils.cached_property
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restplus import Api

class Server(object):
        def start(self):
            self.app.run(debug=True)

        def setup_api(self):
            self.api = Api(self.app, version='1.0', title='Starwars films.', description='get all the starwars films.')
            from services.films import Films
            from services.characters import Characters
            self.api.add_resource(Films, '/films', endpoint='films')
            self.api.add_resource(Characters, '/characters', endpoint='characters')

        def config_app(self):
            self.app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database/test1.db'

        def setup_database(self):
            self.db = SQLAlchemy(self.app)
        
        def get_db(self):
            return self.db

        def get_api(self):
            return self.api

        def __init__(self):
            self.app = Flask(__name__)

        def create_all_tables(self):
            from models.characters import Tcharacters
            from models.films import Tfilms
            self.db.create_all()

server = Server()
server.config_app()
server.setup_database()
db = server.get_db()
if __name__ == "__main__":
    server.create_all_tables()
    server.setup_api()
    server.start()
