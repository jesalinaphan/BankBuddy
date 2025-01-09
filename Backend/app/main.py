from fastapi import FastAPI
from app.database import Base, engine
from app.routes import (
    user_routes,
    account_routes,
    transaction_routes,
    finance_actions,
    ai_routes
)

def create_app():
    # For local dev only; in production, use Alembic migrations
    Base.metadata.create_all(bind=engine)

    app = FastAPI(title="SpendWise (Free LLM Edition)")

    app.include_router(user_routes.router, prefix="/users", tags=["Users"])
    app.include_router(account_routes.router, prefix="/accounts", tags=["Accounts"])
    app.include_router(transaction_routes.router, prefix="/transactions", tags=["Transactions"])
    app.include_router(finance_actions.router, prefix="/finance", tags=["Finance"])
    app.include_router(ai_routes.router, prefix="/ai", tags=["AI"])

    return app

app = create_app()
