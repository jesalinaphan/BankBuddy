from plaid import Client
from app.config import settings

plaid_client = Client(
    client_id=settings.PLAID_CLIENT_ID,
    secret=settings.PLAID_SECRET,
    environment=settings.PLAID_ENV,
    api_version='2019-05-29'
)

def exchange_public_token(public_token: str) -> str:
    response = plaid_client.Item.public_token.exchange(public_token)
    return response['access_token']

def fetch_accounts(access_token: str):
    response = plaid_client.Accounts.get(access_token)
    return response['accounts']

def fetch_transactions(access_token: str, start_date: str, end_date: str):
    response = plaid_client.Transactions.get(access_token, start_date, end_date)
    return response['transactions']
"""
def initiate_transfer(...):
    # Where we would call Plaid's /sandbox/processor/stripe-ach endpoint
    pass
"""