from flask import make_response, jsonify, abort, request
from flask_restplus import Namespace, Resource
from utils.getters import get_starwars_url
import urllib.parse
import requests
import re
from datetime import datetime

class Characters(Resource):
    '''This api have a post service to get all films form starwars''' 
    
    def post(self):
        '''Create a new task'''
        input_json = request.get_json()
        current_time = datetime.now()
        film_id = self.get_input_params(input_json)
        output = self.get_characters(film_id)
        return make_response(jsonify(output))
    
    def get_input_params(self, json_):
        try:
            film_id = json_['filmID']
            return int(film_id)
        except:
            abort("Need filmID in input request!!!")

    def _get_character_urls(self,film_id):
        films_url = urllib.parse.urljoin(get_starwars_url(), 'films') 
        film_url = films_url + '/' + str(film_id) + '/'
        json_ = requests.get(film_url).json()
        return json_['characters']

    def get_characters(self, film_id):
        names = []
        for url in self._get_character_urls(film_id):
            template = {'id': None, 'name': None}
            template['id'] = self.get_id(url)
            template['name'] = self.get_character_name(url)
            names.append(template)
        return names
        
    def get_id(self, url):
        pattern = "([0-9]+)/$"
        return re.search(pattern, url).group(1)

    def get_character_name(self, url):
        return requests.get(url).json()['name']
