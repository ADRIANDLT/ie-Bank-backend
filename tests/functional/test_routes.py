from iebank_api import app
import pytest
import json

def test_get_accounts(testing_client):
    """
    GIVEN a Flask application
    WHEN the '/accounts' page is requested (GET)
    THEN check the response is valid
    """
    response = testing_client.get('/accounts')
    assert response.status_code == 200

def test_dummy_wrong_path():
    """
    GIVEN a Flask application
    WHEN the '/wrong_path' page is requested (GET)
    THEN check the response is valid
    """
    with app.test_client() as client:
        response = client.get('/wrong_path')
        assert response.status_code == 404

def test_create_account(testing_client):
    """
    GIVEN a Flask application
    WHEN the '/accounts' page is posted to (POST)
    THEN check the response is valid
    """
    response = testing_client.post('/accounts', json={'name': 'John Doe', 'currency': '€', 'country': 'Spain'})
    assert response.status_code == 200

def test_get_account_by_account_id(testing_client):
    """
    GIVEN a Flask application
    WHEN the '/accounts' page is requested (GET)
    THEN check the response is valid
    """
    # Query all existing accounts
    response_all = testing_client.get('/accounts')
    assert response_all.status_code == 200

    # Parse the JSON response
    accounts = json.loads(response_all.data)
    
    # Ensure there are accounts in the response
    assert len(accounts) > 0

    # Get the first account
    first_account = accounts['accounts'][0]
    
    # Perform assertions on the first account
    assert 'id' in first_account
    assert 'account_number' in first_account
    assert 'name' in first_account
    assert 'currency' in first_account
    assert 'country' in first_account

    # Now we can test get by account number
    response_single = testing_client.get('/accounts/' + str(first_account['id']))
    assert response_single.status_code == 200

# test update/put to the by default account id=1
def test_put_account(testing_client):
    """
    GIVEN a Flask application
    WHEN the '/accounts' page is updated (PUT)
    THEN check the response is valid
    """
    response = testing_client.put('/accounts/1', json={'name': 'John Doe', 'currency': '€', 'country': 'Spain'})
    assert response.status_code == 200

# test_delete_account would delete the by default created account with id=1
def test_delete_account(testing_client):
    """
    GIVEN a Flask application
    WHEN the '/accounts' page is deleted (DELETE)
    THEN check the response is valid
    """
    response = testing_client.delete('/accounts/1')
    assert response.status_code == 200

# def test_skull(testing_client):
#    """
#    GIVEN a Flask application
#    WHEN the '/skull' page is requested (GET)
#    THEN check the response is valid
#    """
#    response = testing_client.get('/skull')
#    assert response.status_code == 200

def test_hello_world(testing_client):
    """
    GIVEN a Flask application
    WHEN the '/hello' page is requested (GET)
    THEN check the response is valid
    """
    response = testing_client.get('/')
    assert response.status_code == 200

def test_skull(testing_client, mocker):
    """
    GIVEN a Flask application
    WHEN the '/skull' page is requested (GET)
    THEN check the response is valid and contains the expected content
    """
    # Mock the db.engine.url attributes
    mock_url = mocker.patch('iebank_api.db.engine.url')
    mock_url.database = 'test_db'
    mock_url.host = 'localhost'
    mock_url.port = '80'
    mock_url.username = 'test_user'
    mock_url.password = 'test_pass'

    response = testing_client.get('/skull')
    assert response.status_code == 200
    assert 'Hi! This is the BACKEND SKULL! 💀' in response.data.decode()
    assert 'Database URL:test_db' in response.data.decode()
    assert 'Database host:localhost' in response.data.decode()
    assert 'Database port:' in response.data.decode()
    assert 'Database user:' in response.data.decode()
    assert 'Database password:' in response.data.decode()