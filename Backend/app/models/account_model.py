from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base
from app.models.user_model import User

class Account(Base):
    __tablename__ = "accounts"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey(User.id))
    institution_name = Column(String)
    account_type = Column(String) # checking, savings, credit card, etc. 
    access_token = Column(String)  # from Plaid 
    current_balance = Column(Float, default=0.0)

    user = relationship("User", backref="accounts")
