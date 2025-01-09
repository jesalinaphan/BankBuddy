import datetime
from sqlalchemy import Column, Integer, Float, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base
from app.models.user_model import User
from app.models.account_model import Account

class Transaction(Base):
    __tablename__ = "transactions"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey(User.id))
    account_id = Column(Integer, ForeignKey(Account.id))
    amount = Column(Float)
    date = Column(DateTime, default=datetime.timezone.utc)
    merchant = Column(String)
    category = Column(String)  # food, shopping, etc.
    description = Column(String)

    user = relationship("User", backref="transactions")
    account = relationship("Account", backref="transactions")
