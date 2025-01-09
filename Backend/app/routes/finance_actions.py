from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.account_model import Account
from app.models.transaction_model import Transaction
from app.services.brokerage_service import buy_stock
from app.services.credit_service import pay_credit_card
import datetime

router = APIRouter()

@router.post("/transfer")
def transfer_funds(from_account_id: int, to_account_id: int, amount: float, db: Session = Depends(get_db)):
    if amount <= 0:
        raise HTTPException(status_code=400, detail="Amount must be positive.")
    from_acc = db.query(Account).filter(Account.id == from_account_id).first()
    to_acc = db.query(Account).filter(Account.id == to_account_id).first()
    if not from_acc or not to_acc:
        raise HTTPException(status_code=404, detail="Account not found.")
    if from_acc.current_balance < amount:
        raise HTTPException(status_code=400, detail="Insufficient funds.")

    # Subtract from one, add to the other
    from_acc.current_balance -= amount
    to_acc.current_balance += amount

    # Log a transaction
    txn_out = Transaction(
        user_id=from_acc.user_id,
        account_id=from_acc.id,
        amount=amount,
        date=datetime.datetime.utcnow(),
        merchant="Internal Transfer",
        category="Transfer",
        description=f"Transfer to Account {to_acc.id}"
    )
    db.add(txn_out)

    txn_in = Transaction(
        user_id=to_acc.user_id,
        account_id=to_acc.id,
        amount=amount,
        date=datetime.datetime.utcnow(),
        merchant="Internal Transfer",
        category="Transfer",
        description=f"Transfer from Account {from_acc.id}"
    )
    db.add(txn_in)

    db.commit()
    return {"message": "Transfer successful"}

@router.post("/pay_credit_card")
def credit_card_payment(credit_account_id: int, from_account_id: int, amount: float, db: Session = Depends(get_db)):
    # Placeholder
    pay_credit_card(credit_account_id, from_account_id, amount)
    return {"message": "Credit card paid off (stub)."}

@router.post("/buy_stock")
def buy_stock_route(user_id: int, from_account_id: int, symbol: str, quantity: float, db: Session = Depends(get_db)):
    # Placeholder
    buy_stock(user_id, from_account_id, symbol, quantity)
    return {"message": "Stock purchase (stub)."}
