# 💸 Expense Tracker — Backend

A RESTful backend API for the Expense Tracker app, built with **Django** and **Django REST Framework**. Handles user authentication, expense management, and AI-powered features via Google GenAI.

🔗 **Frontend:** [https://haca-py04-expensetracker.netlify.app](https://haca-py04-expensetracker.netlify.app)
📁 **Repo:** [https://github.com/Vichithra2000/Vichithra2000-haca-py04-expensetracker-BE](https://github.com/Vichithra2000/Vichithra2000-haca-py04-expensetracker-BE)

---

## Tech Stack

| Layer        | Technology                          |
|--------------|-------------------------------------|
| Framework    | Django 6.0.4                        |
| API          | Django REST Framework 3.17.1        |
| Auth         | JWT via `djangorestframework_simplejwt` |
| AI           | Google GenAI 2.10.0                 |
| Database     | SQLite3                             |
| CORS         | django-cors-headers                 |

---

## Project Structure

```
├── expense_tracker_backend/   # Django project settings
├── expenses/                  # Expenses app (models, views, urls)
├── users/                     # Users app (auth, registration)
├── manage.py
├── requirements.txt
└── db.sqlite3
```

---

## Getting Started

### 1. Clone the repo

```bash
git clone https://github.com/Vichithra2000/Vichithra2000-haca-py04-expensetracker-BE.git
cd Vichithra2000-haca-py04-expensetracker-BE
```

### 2. Create a virtual environment

```bash
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Set up environment variables

Create a `.env` file in the root:

```env
SECRET_KEY=your_django_secret_key
DEBUG=True
GOOGLE_API_KEY=your_google_genai_api_key
```

### 5. Run migrations

```bash
python manage.py migrate
```

### 6. Start the server

```bash
python manage.py runserver
```

API will be available at `http://127.0.0.1:8000/`

---

## API Overview

| Method | Endpoint              | Description              |
|--------|-----------------------|--------------------------|
| POST   | `/users/register/`    | Register a new user      |
| POST   | `/users/login/`       | Login & get JWT tokens   |
| POST   | `/users/token/refresh/` | Refresh access token   |
| GET    | `/expenses/`          | List all expenses        |
| POST   | `/expenses/`          | Create a new expense     |
| GET    | `/expenses/<id>/`     | Get a single expense     |
| PUT    | `/expenses/<id>/`     | Update an expense        |
| DELETE | `/expenses/<id>/`     | Delete an expense        |

> All `/expenses/` endpoints require `Authorization: Bearer <token>` header.

---

## Authentication

- **JWT** - obtain tokens via `/api/token/`, refresh via `/api/token/refresh/`
- **Google OAuth** - sign in with Google via the `users` app endpoints

## Key Dependencies

- `Django` — web framework
- `djangorestframework` — REST API toolkit
- `djangorestframework_simplejwt` — JWT authentication
- `django-cors-headers` — cross-origin request support for frontend
- `google-genai` — AI-powered features
- `python-dotenv` — environment variable management

---

Built with care from HACA