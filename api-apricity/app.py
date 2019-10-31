from flask_restful import Api
import os
from src.census_learn.view.view_census_learn import Census

from src import create_app

api = Api()

api.add_resource(Census, '/all/<string:col_name>', endpoint='all')

app = create_app(os.getenv('FLASK_CONFIG'))

if __name__ == '__main__':
    app.run(host='0.0.0.0')
