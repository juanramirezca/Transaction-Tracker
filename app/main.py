from fastapi import FastAPI

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


@app.get("/home")
def hello_world():
    return {"message": "hello World"}


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


{"date": "8-Abr-2026",
        "amount": 214.00
        "payment_method": "credit card",
        "category": "delivery"},{"date": "13-Abr-2026",
        "amount": 390.00
        "payment_method": "credit card",
        "category": "clothes"}

"""
