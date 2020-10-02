from flask import make_response, jsonify
from flask_restplus import Namespace, Resource
from utils.getters import get_starwars_url
import urllib.parse
import requests
from datetime import datetime
from models.films import Tfilms

class Films(Resource):
    '''This api have a post service to get all films form starwars'''

    def post(self):
        '''Create a new task'''
        current_time = datetime.now()
        if self.is_expired_data_in_cache(current_time):
            output = self._prepare_film_info()
            self.truncate_cache()
            self.insert_file_info_to_cache(output, current_time)
        else:
            output = self._get_film_info_from_cache()
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

    def is_expired_data_in_cache(self, current_time):
        try:
            for row in Tfilms.query.get(1):
                print(row)
        except:
            return True

    def insert_file_info_to_cache(self, output, current_time):
        for element in output:
            db.session.add(Tfilms(id_=element['id'], title=element['title'],
                                  releasedate=element['releasedate'], 
                                  lastupdate=current_time))
        db.session.commit()

    def truncate_cache(self):
        Tfilms.query.delete()

    def _get_film_info_from_cache(self):
        film_info = []
        for row in Tfilms.query.all():
            template = {'id': None, 'title': None, 'release_date': None}
            template['id'] = row[0]
            template['title'] = row[1]
            template['release-date'] = row[2]
            film_info.append(template)
        return film_info