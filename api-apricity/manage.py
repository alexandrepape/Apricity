from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
from src import db
import os

from src import create_app

app = create_app(os.getenv('FLASK_CONFIG'))

with app.app_context():
    from src.census_learn.model.model_census_lean import Census_learn_sql

migrate = Migrate(app, db)

manager = Manager(app)
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()
