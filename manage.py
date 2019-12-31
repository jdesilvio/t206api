"""Management scripts."""

from flask_script import Manager

from scripts.upload import load_all_data
from t206api.app import create_app
from t206api.db import db


app = create_app()
manager = Manager(app)


@manager.command
def load_data():
    load_all_data()


@manager.command
def count_tables():
    session = db.session()
    meta = db.metadata
    for table in reversed(meta.sorted_tables):
        print(f'{table.name}: {len(session.query(table).all())}')


@manager.command
def clear_data():
    session = db.session()
    meta = db.metadata
    for table in reversed(meta.sorted_tables):
        print('Clear table %s' % table)
        session.execute(table.delete())
    session.commit()


@manager.command
def reload_data():
    clear_data()
    load_data()


@manager.command
def debug():
    breakpoint()


if __name__ == '__main__':
    manager.run()
