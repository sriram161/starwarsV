import werkzeug
werkzeug.cached_property = werkzeug.utils.cached_property
from flask import Flask
from flask_restplus import Api
from services.films import Films
from services.characters import Characters

app = Flask(__name__)

api = Api(app, version='1.0', title='Starwars films.',
          description='get all the starwars films.')

api.add_resource(Films, '/films', endpoint='films')
api.add_resource(Characters, '/characters', endpoint='characters')

if __name__ == "__main__":
    app.run(debug=True)
