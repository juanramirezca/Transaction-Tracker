from pydantic import BaseModel


class Expense(BaseModel):
    id: int
    date: str
    amount: float
    payment_method: str
    category: str


class ExpenseResponse(BaseModel):
    date: str
    amount: float
    payment_method: str
    category: str
