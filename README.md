#Django Project
---
## 🐦 Twitter-Like Web Application (Django)

A full-featured, Twitter-inspired web application built from scratch using **Django**.  
This project demonstrates **end-to-end web development** — from backend database design and authentication to frontend UI rendering and CRUD operations.

---

## 🚀 Features

- **User Authentication:**  
  Secure user registration, login, and logout using Django's built-in authentication system.

- **Tweet Management (CRUD):**  
  Users can create, edit, delete, and view text-based tweets with optional image uploads.

- **User-Specific Permissions:**  
  Only the tweet creator can modify or delete their posts.

- **Image Uploads:**  
  Tweets support image attachments stored and served via Django’s media management system.

---

## 🧰 Tech Stack

| Layer | Technologies Used |
|-------|--------------------|
| **Backend** | Python, Django, Django ORM |
| **Frontend** | HTML, Tailwind CSS, Jinja2 Templates |
| **Database** | SQLite (default) |
| **Version Control** | Git & GitHub |
| **Environment** | Virtualenv, Django Development Server |

---

## 📁 Project Structure

```markdown
tweet_app/
├── tweet/                     # Main app for handling tweet CRUD operations
│   ├── migrations/              # Database migrations
│   ├── templates/               # HTML templates for tweets
│   ├── admin.py                 # Admin panel configuration
│   ├── apps.py                  # App configuration
│   ├── forms.py                 # Django forms for creating/editing tweets
│   ├── models.py                # Database models
│   ├── tests.py                 # Unit tests
│   ├── urls.py                  # App-level URLs
│   └── views.py                 # View logic for CRUD operations
│
├── tweet_app/               # Project-level settings and URLs
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py              # Main project settings
│   ├── urls.py                  # Root URL configurations
│   └── wsgi.py
│
├── media/                       # Uploaded images (auto-created)
├── static/                      # Static files (CSS, JS)
├── templates/                   # Global templates
      └── registration           # register, login, logged_out pages
├── photos/                      # Tweet photos
├── manage.py                    # Django management script
├── requirements.txt             # Project dependencies
└── README.md                    # Project documentation
```

### 1️⃣ Clone the repository
git clone https://github.com/yourusername/twitter-clone-django.git
cd twitter-clone-django

### 2️⃣ Create and activate a virtual environment
python -m venv venv
venv\Scripts\activate        # On Windows
# source venv/bin/activate   # On macOS/Linux

### 3️⃣ Install dependencies
pip install -r requirements.txt

### 4️⃣ Apply migrations and create a superuser
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser

### 5️⃣ Run the development server
python manage.py runserver

### You can store sensitive information in a .env file:
SECRET_KEY=your_secret_key
ALLOWED_HOSTS=127.0.0.1,localhost


