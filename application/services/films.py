from flask import make_response, jsonify
from flask_restplus import Namespace, Resource
from utils.getters import get_starwars_url
import urllib.parse
import requests

class Films(Resource):
    '''This api have a post service to get all films form starwars'''

    def post(self):
        '''Create a new task'''
        output = self._prepare_film_info()
        return make_response(jsonify(output))

    def _get_starwars_film_data(self):
        films_url = urllib.parse.urljoin(get_starwars_url(), 'films')
        return requests.get(films_url).json()['results']

    def _prepare_film_info(self):
        film_info = []
        for element in self._get_starwars_film_data():
            template = {'id': None, 'title': None, 'release_date': None}
            template['id'] = element['episode_id']
            template['title'] = element['title']
            template['release_date'] = element['release_date']
            film_info.append(template)
        return film_info
