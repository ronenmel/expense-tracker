
Users can add expenses, categorize them (Food, Transport, Entertainment, etc.), and generate reports.
Includes a small AI-powered tip feature to provide budget advice.

🚀 Features

Add new expenses with description, category, amount, and date

Get all expenses

Monthly spending reports

Find the top spending category

AI-generated budgeting tips

🛠 Tech Stack

Python 3.13+

FastAPI

MongoDB (Atlas or local)

Pydantic

Uvicorn

📦 Installation

Clone the repository:

git clone https://github.com/ronenmel/expense-tracker.git
cd expense-tracker-api


Create and activate virtual environment:

py -m venv venv
venv\Scripts\activate


Install dependencies:

pip install -r requirements.txt


Set up your MongoDB connection string in a .env file:

MONGO_URI="mongodb+srv://ronenmelihov_db_user:7Sl1zMKo2uNKhkvQ@expensetrackercluster.bnjximj.mongodb.net/?retryWrites=true&w=majority&appName=ExpenseTrackerCluster"

▶️ Running the API

Start the server:

uvicorn main:app --reload


The API will be available at:
👉 http://127.0.0.1:8000/docs
 (Swagger UI)
