from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.services.plaid_service import exchange_public_token, fetch_accounts
from app.models.account_model import Account
from app.models.user_model import User

router = APIRouter()

@router.post("/link")
def link_bank_account(user_id: int, public_token: str, db: Session = Depends(get_db)):
    access_token = exchange_public_token(public_token)
    if not access_token:
        raise HTTPException(status_code=400, detail="Invalid token exchange.")
    # fetch the plaid accounts
    plaid_accts = fetch_accounts(access_token)
    # For each plaid account, store in the DB
    created_accts = []
    for acct in plaid_accts:
        new_acc = Account(
            user_id=user_id,
            institution_name=acct.get("institution_type", "Unknown"),
            account_type=acct.get("type", "checking"),
            access_token=access_token,
            current_balance=acct.get("balances", {}).get("current", 0.0)
        )
        db.add(new_acc)
        db.commit()
        db.refresh(new_acc)
        created_accts.append(new_acc.id)
    return {"linked_account_ids": created_accts}
