from flask import make_response, jsonify, abort, request
from flask_restplus import Namespace, Resource
from utils.getters import get_starwars_url
import urllib.parse
import requests
import re
from datetime import datetime
from server import Tcharacters
from server import db

class Characters(Resource):
    ''' This api have a post service to get all characters form starwars
        Example:
        ========
        Native curl on windows:
        =======================
        curl -X POST -H "Content-Type:application/json" --data "{"""filmID""":"""1"""}" http://localhost:5000/characters

        On linux:
        =========
        curl -X POST -H "Content-Type:application/json" --data '{"filmID":"1"}' http://localhost:5000/characters
    ''' 
    
    def get_input_params(self, json_):
        try:
            film_id = json_['filmID']
            return int(film_id)
        except:
            abort("Need filmID in input request!!!")
   
    def is_expired_data_in_cache(self, film_id, current_time):
        """ Flag to refresh table data or not.
        """
        for db_obj in Tcharacters.query.filter_by(filmid=film_id).get(1):
            if (current_time - db_obj.lastupdate).total_seconds() <= 3600:
                return False
        return True

    def _get_character_urls(self, film_id):
        """ Gives characters urls for a film.
        """
        films_url = urllib.parse.urljoin(get_starwars_url(), 'films') 
        film_url = films_url + '/' + str(film_id) + '/'
        json_ = requests.get(film_url).json()
        return json_['characters']

    def get_id(self, url):
        pattern = "([0-9]+)/$"
        return re.search(pattern, url).group(1)

    def get_character_name(self, url):
        return requests.get(url).json()['name']

    def get_characters(self, film_id):
        """ Gives characters details. 
        """
        names = []
        for url in self._get_character_urls(film_id):
            template = {'id': None, 'name': None}
            template['id'] = self.get_id(url)
            template['name'] = self.get_character_name(url)
            names.append(template)
        return names

    def truncate_cache(self):
        Tcharacters.query.delete()

    def insert_file_info_to_cache(self, output, current_time, film_id):
        for element in output:
            db.session.add(Tcharacters(id_=element['id'], name=element['name'],
                                  lastupdate=current_time, filmid=film_id))
        db.session.commit()

    def _get_character_info_from_cache(self):
        film_info = []
        for row_obj in Tfilms.query.all():
            template = {'id': None, 'title': None, 'release_date': None}
            template['id'] = row_obj.id_
            template['title'] = row_obj.title
            template['release-date'] = row_obj.releasedate
            film_info.append(template)
        return film_info

    def post(self):
        '''Processing post request start here'''
        input_json = request.get_json()
        current_time = datetime.now()
        film_id = self.get_input_params(input_json)
        if self.is_expired_data_in_cache(film_id, current_time):
           output = self.get_characters(film_id)
           self.truncate_cache()
           self.insert_character_info_to_cache(output, current_time, film_id)
        else:
            output = self._get_character_info_from_cache(film_id)
        return make_response(jsonify(output))
