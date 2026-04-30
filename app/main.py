from fastapi import Depends, FastAPI, HTTPException, status, Response

from sqlalchemy.orm import Session

from app import models

from .database import engine, get_db
from .schemas import Expense, ExpenseResponse

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# TODO: Review that the responses and exceptions are working correctly
# TODO: Start using some real data to see what are we missing so far:
# 1. Change to datetime instead of a string. Can we use a calendar?
# 2. Can we use a dropdown to select the expense method?


@app.get("/expenses", response_model=list[Expense])
def get_expenses(db: Session = Depends(get_db)):
    return db.query(models.Expense).all()


@app.get("/expense/{expense_id}", response_model=Expense)
def get_expense_by_id(expense_id: int, db: Session = Depends(get_db)):

    expense = db.query(models.Expense).filter(models.Expense.id == expense_id).first()

    if not expense:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Expense with id {expense_id} not found!",
        )

    return expense


@app.post(
    "/create-expense",
    status_code=status.HTTP_201_CREATED,
    response_model=ExpenseResponse,
)
def create_response(expense: Expense, db: Session = Depends(get_db)):
    try:
        new_expense = models.Expense(**expense.model_dump())
        db.add(new_expense)
        db.commit()
        db.refresh(new_expense)

        return new_expense

    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error while creating a new post: {e}",
        )


@app.put("/update-expense/{expense_id}", status_code=status.HTTP_204_NO_CONTENT)
def update_expense(expense_id: int, expense: Expense, db: Session = Depends(get_db)):
    query = db.query(models.Expense).filter(models.Expense.id == expense_id)

    updated_expense = query.first()

    if not updated_expense:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Expense with id {expense_id} not found!",
        )

    query.update(expense.model_dump())
    db.commit()


@app.delete("/delete-expense/{expense_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_expense(expense_id: int, db: Session = Depends(get_db)):
    query = db.query(models.Expense).filter(models.Expense.id == expense_id)
    deleted_expense = query.first()

    if not deleted_expense:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Expense with id {expense_id} not found!",
        )

    query.delete()
    db.commit()


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
