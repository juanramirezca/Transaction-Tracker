import uuid
from sqlalchemy import Column, Float, Integer, String
from .database import Base


class Expense(Base):
    __tablename__ = "expenses"
    id = Column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    date = Column(String, nullable=False)
    amount = Column(Float, nullable=False)
    payment_method = Column(String, nullable=False)
    category = Column(String, nullable=False)
