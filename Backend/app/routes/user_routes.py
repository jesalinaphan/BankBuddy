from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.user_model import User
from passlib.hash import bcrypt

router = APIRouter()

@router.post("/register")
def register_user(email: str, password: str, db: Session = Depends(get_db)):
    existing = db.query(User).filter(User.email == email).first()
    if existing:
        raise HTTPException(status_code=400, detail="Email already registered.")
    hashed = bcrypt.hash(password)
    new_user = User(email=email, hashed_password=hashed)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return {"id": new_user.id, "email": new_user.email}

@router.post("/login")
def login_user(email: str, password: str, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.email == email).first()
    if not user:
        raise HTTPException(status_code=401, detail="Invalid credentials.")
    if not bcrypt.verify(password, user.hashed_password):
        raise HTTPException(status_code=401, detail="Invalid credentials.")
    return {"msg": "Logged in", "user_id": user.id}
