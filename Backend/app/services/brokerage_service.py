"""
brokerage_service.py

Example service for placing dummy stock trades. 

"""

import requests

def buy_stock(user_id: int, from_account_id: int, symbol: str, quantity: float):
    # Placeholder for a real brokerage API call
    print(f"Stub: Buying {quantity} of {symbol} for user {user_id} using account {from_account_id}")
