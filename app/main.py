from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

expenses = [
    {
        "id": 1,
        "date": "8-Abr-2026",
        "amount": 344.97,
        "payment_method": "credit card",
        "category": "food",
    },
    {
        "id": 2,
        "date": "14-Abr-2026",
        "amount": 390,
        "payment_method": "cash",
        "category": "clothes",
    },
    {
        "id": 3,
        "date": "12-Abr-2026",
        "amount": 213,
        "payment_method": "transfer",
        "category": "gas",
    },
]


class Expense(BaseModel):
    id: int
    date: str
    amount: float
    payment_method: str
    category: str


@app.get("/home")
def hello_world():
    return {"message": "hello World"}


@app.get("/expenses")
def get_expenses():
    return expenses


@app.get("/expense/{expense_id}")
def get_expense_by_id(expense_id: int):
    for expense in expenses:
        if expense_id == expense["id"]:
            return expense

    return {"Error": f"The expense {expense_id} was not found"}


@app.post("/create-expense")
def create_response(expense: Expense):
    for exp in expenses:
        if expense.id == exp["id"]:
            return {"Error": f"That expense id is duplicated"}

    expenses.append(expense.model_dump())

    return {"Success": "The expense was appended sucessfully"}


@app.put("/update-expense/{expense_id}")
def update_expense(expense_id: int, expense: Expense):
    for exp in expenses:
        if expense_id == exp["id"]:
            exp.update(expense.model_dump())
            return {"Success": "The expense was updated sucessfully"}

    return {"Error": f"The expense {expense_id} was not found"}


@app.delete("/delete-expense/{expense_id}")
def delete_expense(expense_id: int):
    for exp in expenses:
        if expense_id == exp["id"]:
            expenses.remove(exp)
            return {"Success": "The expense was deleted sucessfully"}

    return {"Error": f"The expense {expense_id} was not found"}


"""
** Expenses **
id: uuid
date: datetieme
expense_amount: float
payment_method:str
expense_category: str

** Income **
id: uuid
date: datetieme
expense_amount: float
payment_method:str
expense_category: str


{
  "id": 4,
  "date": "17-abr-2026",
  "amount": 899,
  "payment_method": "credit card",
  "category": "food"
}

"""
