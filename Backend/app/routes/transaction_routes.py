from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from datetime import datetime, timedelta
from app.database import get_db
from app.services.plaid_service import fetch_transactions
from app.models.transaction_model import Transaction
from app.models.account_model import Account
from app.ml.ml_model import categorize_transaction

router = APIRouter()

@router.post("/sync")
def sync_transactions(
    account_id: int,
    start_date: str = None,
    end_date: str = None,
    db: Session = Depends(get_db)
):
    account = db.query(Account).filter(Account.id == account_id).first()
    if not account:
        return {"error": "Account not found."}
    if not start_date:
        start_date = (datetime.now() - timedelta(days=30)).strftime("%Y-%m-%d")
    if not end_date:
        end_date = datetime.now().strftime("%Y-%m-%d")

    # call plaid
    txn_data = fetch_transactions(account.access_token, start_date, end_date)
    inserted_count = 0
    for t in txn_data:
        existing = db.query(Transaction).filter(
            Transaction.account_id == account_id,
            Transaction.date == t["date"],
            Transaction.amount == abs(t["amount"])
        ).first()
        if existing:
            continue  

        cat = categorize_transaction(t.get("name", ""), t["amount"])
        new_txn = Transaction(
            user_id=account.user_id,
            account_id=account_id,
            amount=abs(t["amount"]),
            date=datetime.strptime(t["date"], "%Y-%m-%d"),
            merchant=t.get("name", ""),
            category=cat,
            description=t.get("name", "")
        )
        db.add(new_txn)
        inserted_count += 1

    db.commit()
    return {"inserted_transactions": inserted_count}
