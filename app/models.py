from sqlalchemy import Column, Float, Integer, String
from .database import Base


class Expense(Base):
    __tablename__ = "expenses"
    id = Column(Integer, primary_key=True, nullable=False, index=True)
    date = Column(String, nullable=False)
    amount = Column(Float, nullable=False)
    payment_method = Column(String, nullable=False)
    category = Column(String, nullable=False)
