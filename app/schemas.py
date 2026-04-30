from pydantic import BaseModel
from uuid import UUID


class Expense(BaseModel):
    date: str
    amount: float
    payment_method: str
    category: str


class ExpenseResponse(BaseModel):
    id: UUID
    date: str
    amount: float
    payment_method: str
    category: str
