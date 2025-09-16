from fastapi import FastAPI
from pydantic import BaseModel
from datetime import datetime
from pymongo import MongoClient
import random

# חיבור ל-MongoDB (אם התקנת Atlas תחליף את ה-URI כאן)
client = MongoClient("mongodb+srv://ronenmelihov_db_user:7Sl1zMKo2uNKhkvQ@expensetrackercluster.bnjximj.mongodb.net/?retryWrites=true&w=majority&appName=ExpenseTrackerCluster")
db = client["expense_tracker"]
expenses_collection = db["expenses"]

app = FastAPI()

class Expense(BaseModel):
    description: str
    category: str
    amount: float
    date: datetime = datetime.now()

@app.post("/expenses")
def add_expense(expense: Expense):
    result = expenses_collection.insert_one(expense.dict())
    return {"id": str(result.inserted_id)}

@app.get("/expenses")
def get_expenses():
    expenses = list(expenses_collection.find())
    for e in expenses:
        e["_id"] = str(e["_id"])
    return expenses

@app.get("/reports/monthly")
def monthly_report():
    pipeline = [
        {"$group": {"_id": {"month": {"$month": "$date"}}, "total": {"$sum": "$amount"}}}
    ]
    return list(expenses_collection.aggregate(pipeline))

@app.get("/reports/top-category")
def top_category():
    pipeline = [
        {"$group": {"_id": "$category", "total": {"$sum": "$amount"}}},
        {"$sort": {"total": -1}}, {"$limit": 1}
    ]
    result = list(expenses_collection.aggregate(pipeline))
    return result[0] if result else {}

@app.get("/reports/ai-tip")
def ai_tip():
    categories = list(expenses_collection.aggregate([
        {"$group": {"_id": "$category", "total": {"$sum": "$amount"}}}
    ]))
    if not categories:
        return {"tip": "אין עדיין נתונים"}
    top = max(categories, key=lambda x: x["total"])
    tips = [
        f"הוצאת הרבה על {top['_id']}. אולי תנסה לקבוע תקציב חודשי.",
        f"{top['_id']} לקח לך את רוב התקציב – שווה לשקול לצמצם.",
        f"שים לב, {top['_id']} זו ההוצאה העיקרית שלך."
    ]
    return {"tip": random.choice(tips)}
