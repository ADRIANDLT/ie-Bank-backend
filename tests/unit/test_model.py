from iebank_api.models import Account
from iebank_api import db
import pytest

def test_create_object_account():
    # This test is in memory not creating in the database
    """
    GIVEN a Account model
    WHEN a new Account is created
    THEN check the name, account_number, balance, currency, status and created_at fields are defined correctly
    """
    # (ADLT) Added test coverage for the country field
    account = Account(name='Adrian', country='Spain', currency='€')
    assert account.name == 'Adrian'
    assert account.country == 'Spain'
    assert account.currency == '€'
    assert account.account_number != None
    assert account.balance == 0.0
    assert account.status == 'Active'

def test_create_account_in_database(testing_client):
    """
    GIVEN a Account model
    WHEN a new Account is created
    THEN check the account is in the database
    """
    with testing_client.application.app_context():  # Ensure the app context is active
        account = Account(name='Adrian', country='Spain', currency='€')
        db.session.add(account)
        db.session.commit()
        assert Account.query.filter_by(name='Adrian').first() == account

def test_query_account(testing_client):
    """
    GIVEN a Account model
    WHEN a new Account is created
    THEN check the account is in the database
    """
    with testing_client.application.app_context():  # Ensure the app context is active
        account = Account(name='Julio', currency='€', country='Spain')
        db.session.add(account)
        db.session.commit()
        assert Account.query.filter_by(name='Julio').first() == account

def test_default_query_account(testing_client):
    """
    GIVEN a Account model
    SINCE there was a default account created in the conftest.py
    THEN check the account is in the database
    """
    with testing_client.application.app_context():  # Ensure the app context is active
        assert Account.query.filter_by(name='By Default Test Account').first() != None

def test_update_account(testing_client):
    """
    GIVEN a Account model
    WHEN a new Account is created
    THEN check the account is in the database
    WHEN the account is updated
    THEN check the account is updated in the database
    """
    with testing_client.application.app_context():  # Ensure the app context is active
        account = Account(name='Jose', currency='€', country='Spain')
        acc_number = account.account_number
        db.session.add(account)
        db.session.commit()

        account2 = Account.query.filter_by(account_number=acc_number).first()
        account2.name = 'Jose Miguel'
        db.session.commit()
        assert Account.query.filter_by(account_number=acc_number).first() == account2

        account3 = Account.query.filter_by(account_number=acc_number).first()
        assert account3.name == 'Jose Miguel'

def test_delete_account(testing_client):
    """
    GIVEN a Account model
    WHEN a new Account is created
    THEN check the account is in the database
    WHEN the account is deleted
    THEN check the account is not in the database
    """
    with testing_client.application.app_context():  # Ensure the app context is active
        account = Account(name='Andres', currency='€', country='Spain')
        acc_number = account.account_number
        db.session.add(account)
        db.session.commit()

        account2 = Account.query.filter_by(account_number=acc_number).first()
        db.session.delete(account2)
        db.session.commit()
        assert Account.query.filter_by(account_number=acc_number).first() == None