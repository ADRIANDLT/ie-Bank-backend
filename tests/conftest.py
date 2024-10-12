import pytest
import os

# Set environment variables
os.environ['FLASK_APP'] = 'app.py'
os.environ['FLASK_DEBUG'] = '1'
os.environ['FLASK_RUN_PORT'] = '5000'
os.environ['ENV'] = 'local'    # Using SQLite
os.environ['DBUSER'] = 'testuser'
os.environ['DBPASS'] = 'testpass'
os.environ['DBHOST'] = 'localhost'
os.environ['DBNAME'] = 'testdb'

from iebank_api.models import Account
from iebank_api import db, app

@pytest.fixture(scope='module')
def testing_client():
    with app.app_context():
        # Create empty database with our model
        db.create_all()

        # Create a by default test account for unit tests
        account = Account('By Default Test Account', '€', 'Spain')
        db.session.add(account)
        db.session.commit()

    with app.test_client() as testing_client:
        with app.app_context():  # Ensure the app context is active
            yield testing_client

    with app.app_context():
        db.drop_all()
    