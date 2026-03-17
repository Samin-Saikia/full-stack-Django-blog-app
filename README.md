# 📝 Full-Stack Django Blog Platform

> A complete blog platform built with Django — authentication, post management, categories, tags, role-based permissions, and a custom responsive UI. No frameworks, pure CSS.

[![Python](https://img.shields.io/badge/Python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)](https://python.org)
[![Django](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white)](https://djangoproject.com)
[![MySQL](https://img.shields.io/badge/MySQL-4479A1?style=for-the-badge&logo=mysql&logoColor=white)](https://mysql.com)
[![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)](https://developer.mozilla.org)

---

## Overview

A full-stack blog application with a complete content management system. Users can register, write and manage their own posts, and browse content filtered by category or tag. Superusers have full moderation control. Built end-to-end — backend, frontend, and database — with no third-party UI frameworks.

---

## Features

### Authentication
- User registration and login
- Secure session-based authentication
- Password protection and logout

### Blog System
- Create, edit, and delete blog posts
- Publish and draft system — control post visibility
- Slug-based URLs for clean, SEO-friendly links
- Rich content support

### Role-Based Permissions
- Any registered user can write and manage their own posts
- Users can only edit and delete their own content
- Superusers have full control — edit or delete any post on the platform

### Content Organisation
- Categories — group posts by topic
- Tags — flexible multi-label system
- Filter and browse posts by category or tag

### User Dashboard
- Personal "My Posts" dashboard per user
- Overview of all owned posts with quick edit and delete actions

### UI / UX
- Card-based responsive layout
- Custom CSS — no Bootstrap or Tailwind, written from scratch
- Clean gradient theme, works on mobile and desktop

---

## Tech Stack

| Layer | Technology |
|:---|:---|
| Backend | Django (Python) |
| Frontend | HTML5, CSS3, Vanilla JavaScript |
| Database | MySQL / SQLite |
| Authentication | Django built-in auth system |
| Styling | Custom CSS — no frameworks |
| Version Control | Git & GitHub |

---

## Project Structure

```
blog_platform/
├── accounts/              # Registration, login, logout views
├── blog/                  # Posts, categories, tags, slugs
│   ├── models.py          # Post, Category, Tag models
│   ├── views.py           # CRUD views with permission checks
│   ├── urls.py            # Slug-based URL routing
│   └── admin.py           # Admin registration
├── templates/
│   ├── base.html          # Base layout
│   ├── blog/              # Post list, detail, create, edit
│   └── accounts/          # Login, register pages
├── static/
│   ├── css/style.css      # All custom styles
│   └── js/main.js         # UI interactions
├── blog_platform/         # Django project settings
├── .env                   # Secret key and DB credentials
├── manage.py
└── requirements.txt
```

---

## Local Setup

### 1. Clone the repository

```bash
git clone https://github.com/Samin-Saikia/full-stack-Django-blog-app.git
cd full-stack-Django-blog-app
```

### 2. Create and activate virtual environment

```bash
python -m venv venv

# Windows
venv\Scripts\activate

# Linux / Mac
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Create `.env` file

```env
SECRET_KEY=your_secret_key_here
DEBUG=True
DB_NAME=blog_db
DB_USER=root
DB_PASSWORD=your_password
DB_HOST=localhost
DB_PORT=3306
```

### 5. Run migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 6. Create superuser

```bash
python manage.py createsuperuser
```

### 7. Start the server

```bash
python manage.py runserver
```

Visit `http://127.0.0.1:8000/`

---

## Security

- `SECRET_KEY` stored in `.env` — never committed
- `.gitignore` protects credentials, virtual environment, and cache files
- Role-based permissions enforced at the view level — users cannot modify others' content
- Superuser moderation access controlled via Django's permission system

---

## Author

**Samin Saikia** — Python Developer · Django · Full-Stack · Backend Systems

[![GitHub](https://img.shields.io/badge/GitHub-0d1117?style=for-the-badge&logo=github&logoColor=white)](https://github.com/Samin-Saikia)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://linkedin.com/in/samin-saikia-b7660b3a1)
