# 📈 OneTradeAI - AI Trading Dashboard

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=0:020617,50:3b82f6,100:8b5cf6&height=220&section=header&text=OneTradeAI&fontSize=58&fontColor=ffffff&animation=fadeIn&fontAlignY=38&desc=React%20%7C%20Flask%20%7C%20SQLite%20%7C%20Machine%20Learning%20Trading%20Dashboard&descAlignY=60&descAlign=50&descSize=18" />
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Frontend-React-61DAFB?style=for-the-badge&logo=react&logoColor=black" />
  <img src="https://img.shields.io/badge/Backend-Flask-111827?style=for-the-badge&logo=flask&logoColor=white" />
  <img src="https://img.shields.io/badge/Database-SQLite-003B57?style=for-the-badge&logo=sqlite&logoColor=white" />
  <img src="https://img.shields.io/badge/ML-TensorFlow-FF6F00?style=for-the-badge&logo=tensorflow&logoColor=white" />
  <img src="https://img.shields.io/badge/Trading-AI%20Dashboard-22c55e?style=for-the-badge" />
</p>

<p align="center">
  A full-stack AI-based trading dashboard where users can sign up, log in, add trade entries, track recent trades, and get market prediction suggestions from a Flask-based ML backend.
</p>

---

## 🚀 Project Overview

**OneTradeAI** is a demo/training-style AI trading dashboard built using **React**, **Flask**, **SQLite**, and **Python ML libraries**.

The application allows users to:

* Create an account
* Log in securely
* Add trade entries
* Set profit target limits
* Set stop-loss limits
* View recent trade history
* Run backend prediction logic for pending trades
* Use market data to generate AI-based buy/sell suggestions

> ⚠️ This project is created for learning and portfolio purposes only. It is not financial advice and should not be used for real-money trading decisions.

---

## ✨ Key Features

* 🔐 User signup and login
* 📊 Trading dashboard
* ➕ Add new trade entries
* 🎯 Profit target tracking
* 🛡️ Stop-loss tracking
* 📜 Recent trade history
* 🤖 AI/ML-based prediction endpoint
* 📈 Market data fetching using `yfinance`
* 🧠 LSTM/TensorFlow-based prediction logic
* 💾 SQLite database integration
* 🌐 React frontend with Flask REST API backend
* 🎨 Premium dark UI design

---

## 🧰 Tech Stack

<p align="center">
  <img src="https://skillicons.dev/icons?i=react,js,python,flask,sqlite,html,css,bootstrap,github,git,vscode" />
</p>

### Frontend

* React
* React Bootstrap
* React Router
* JavaScript
* HTML/CSS

### Backend

* Flask
* Flask RESTful
* Flask SQLAlchemy
* Flask CORS
* SQLite

### Machine Learning / Prediction

* Python
* TensorFlow / Keras
* pandas
* yfinance
* TA-Lib
* LSTM model logic

---

## 📂 Project Structure

```text
OneTrade-AI/
│
├── README.md
├── Paper.txt
│
├── backend/
│   └── backend/
│       ├── main.py
│       ├── requirements.txt
│       ├── database.db
│       │
│       ├── controllers/
│       │   ├── auth.py
│       │   ├── trade.py
│       │   └── predict.py
│       │
│       ├── models/
│       │   ├── User.py
│       │   └── Trades.py
│       │
│       └── lib/
│           └── db.py
│
├── frontend/
│   └── frontend/
│       ├── package.json
│       ├── public/
│       └── src/
│           ├── App.js
│           ├── index.js
│           │
│           └── components/
│               ├── AppNavbar.js
│               ├── Home.js
│               ├── Login.js
│               ├── SignUp.js
│               ├── Dashboard.js
│               ├── Features.js
│               ├── Pricing.js
│               ├── Contact.js
│               ├── MyProfile.js
│               ├── Settings.js
│               └── style.css
│
└── back_algo/
    └── back_algo/
        └── crypto prediction notebooks / experiments
```

---

## ⚙️ How the App Works

```text
User opens React frontend
        ↓
User signs up or logs in
        ↓
Session data is stored in localStorage
        ↓
User adds trade details from dashboard
        ↓
Flask backend stores trade in SQLite database
        ↓
Dashboard fetches recent trades
        ↓
Prediction endpoint checks pending trades
        ↓
ML logic analyzes market movement
        ↓
Trade status can be updated based on prediction
```

---

## 🔗 API Endpoints

| Method | Endpoint                    | Description                             |
| ------ | --------------------------- | --------------------------------------- |
| POST   | `/login`                    | Login existing user                     |
| POST   | `/sign_up`                  | Create new user                         |
| POST   | `/add_trade`                | Add a new trade                         |
| GET    | `/recent_trades?userId=...` | Fetch recent trades for a user          |
| GET    | `/predict`                  | Run prediction logic for pending trades |

---

## 🧪 API Testing Examples

### Signup

```http
POST http://127.0.0.1:5000/sign_up
```

```json
{
  "email": "test@gmail.com",
  "password": "123456",
  "confirm_password": "123456"
}
```

### Login

```http
POST http://127.0.0.1:5000/login
```

```json
{
  "email": "test@gmail.com",
  "password": "123456"
}
```

### Add Trade

```http
POST http://127.0.0.1:5000/add_trade
```

```json
{
  "symbol": "BTC-USD",
  "amount": 1000,
  "profitLimit": 10,
  "stopLoss": 5,
  "userId": 1,
  "time": "2026-06-22T10:00:00.000Z"
}
```

### Recent Trades

```http
GET http://127.0.0.1:5000/recent_trades?userId=1
```

---

## 📦 Installation

Clone the repository:

```bash
git clone https://github.com/Adityakhare123/OneTrade-AI.git
cd OneTrade-AI
```

---

## ▶️ Backend Setup

Go to backend folder:

```bash
cd backend/backend
```

Create virtual environment:

```bash
python -m venv venv
```

Activate virtual environment:

### Windows

```bash
venv\Scripts\activate
```

### macOS/Linux

```bash
source venv/bin/activate
```

Install backend dependencies:

```bash
pip install -r requirements.txt
```

If `requirements.txt` is missing or incomplete, install common packages manually:

```bash
pip install flask flask-restful flask-sqlalchemy flask-cors requests pandas yfinance tensorflow
```

Run backend:

```bash
python main.py
```

Backend will start at:

```text
http://127.0.0.1:5000
```

Test backend home route:

```text
http://127.0.0.1:5000/
```

Expected response:

```json
{
  "message": "OneTradeAI backend is running",
  "status": "success"
}
```

---

## ▶️ Frontend Setup

Open a new terminal and go to frontend folder:

```bash
cd frontend/frontend
```

Install frontend dependencies:

```bash
npm install
```

Start React app:

```bash
npm start
```

Frontend will run at:

```text
http://localhost:3000
```

---

## 🧠 Prediction Logic

The prediction module is located in:

```text
backend/backend/controllers/predict.py
```

The prediction logic:

* Fetches pending trades
* Downloads market data using `yfinance`
* Uses technical indicators like RSI
* Applies TensorFlow/Keras LSTM model logic
* Compares predicted direction with profit and stop-loss rules
* Updates trade status after evaluation

> Note: The `/predict` endpoint may require additional ML dependencies like TensorFlow, yfinance, pandas, and TA-Lib. TA-Lib can be difficult to install on Windows, so prediction logic may need separate setup or cleanup.

---

## 🖥️ Frontend Pages

| Route        | Page              |
| ------------ | ----------------- |
| `/`          | Home page         |
| `/login`     | Login page        |
| `/signup`    | Signup page       |
| `/dashboard` | Trading dashboard |
| `/features`  | Features page     |
| `/pricing`   | Pricing page      |
| `/contact`   | Contact page      |
| `/profile`   | User profile      |
| `/settings`  | Settings page     |

---

## 🎨 UI Design

The project includes a premium dark trading dashboard UI with:

* Glassmorphism cards
* Gradient buttons
* Modern navbar
* Dark background
* Trading stats cards
* Clean login/signup screens
* Responsive layout
* Premium SaaS-style design

---

## 🧪 Testing Checklist

Use this checklist to verify the project:

```text
1. Start Flask backend
2. Open http://127.0.0.1:5000/
3. Start React frontend
4. Open http://localhost:3000
5. Create account from signup page
6. Login with created user
7. Open dashboard
8. Add trade using BTC-USD
9. Check recent trades table
10. Test /recent_trades API
11. Test /predict endpoint separately
```

Recommended test trade:

```text
Symbol: BTC-USD
Stop Loss: 5
Profit Target: 10
Amount: 1000
```

---

## 📋 Requirements

### Backend

```txt
flask
flask-restful
flask-sqlalchemy
flask-cors
requests
pandas
yfinance
tensorflow
keras
TA-Lib
```

### Frontend

```txt
react
react-bootstrap
bootstrap
react-router-dom
axios
```

---

## 🛠️ Common Issues

### 1. `ModuleNotFoundError: No module named flask_cors`

Fix:

```bash
pip install flask-cors
```

### 2. `ModuleNotFoundError: No module named requests`

Fix:

```bash
pip install requests
```

### 3. Frontend not connecting to backend

Make sure Flask backend is running:

```text
http://127.0.0.1:5000
```

Also confirm frontend API calls are using:

```text
http://127.0.0.1:5000
```

### 4. Database table error

Make sure `main.py` contains:

```python
with app.app_context():
    db.create_all()
```

### 5. Prediction endpoint failing

Install ML dependencies or test normal app flow first:

```text
signup → login → add trade → recent trades
```

Then debug `/predict`.

---

## 🚀 Future Improvements

* Improve prediction endpoint response handling
* Add JWT-based authentication
* Add password hashing
* Replace SQLite with PostgreSQL
* Add real-time market charts
* Add candlestick chart visualization
* Add trade type: Buy/Sell
* Add portfolio summary
* Add profit/loss analytics
* Add loading skeletons
* Deploy frontend on Vercel
* Deploy backend on Render/Railway
* Add Docker support
* Add unit tests for APIs
* Add README screenshots
* Add live demo link

---

## 📌 Current Project Status

The current project supports:

* React frontend
* Flask backend
* SQLite database
* User signup/login
* Add trade functionality
* Recent trade display
* Premium dashboard UI
* Basic ML prediction flow

Some areas may still need cleanup:

* Prediction logic
* API response consistency
* Production authentication
* Error handling
* Deployment configuration

---

## 👨‍💻 Author

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=soft&color=0:020617,100:3b82f6&height=120&section=footer&text=Aditya%20Khare&fontSize=36&fontColor=ffffff&animation=fadeIn" />
</p>

**Aditya Khare**

<p>
  <a href="https://github.com/Adityakhare123">
    <img src="https://img.shields.io/badge/GitHub-Adityakhare123-181717?style=for-the-badge&logo=github&logoColor=white" />
  </a>
  <a href="https://github.com/Adityakhare123/OneTrade-AI">
    <img src="https://img.shields.io/badge/Project-OneTrade--AI-3b82f6?style=for-the-badge&logo=github&logoColor=white" />
  </a>
</p>

---

## ⭐ Support

If you like this project, consider giving it a ⭐ on GitHub.

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=0:8b5cf6,50:3b82f6,100:020617&height=120&section=footer" />
</p>
