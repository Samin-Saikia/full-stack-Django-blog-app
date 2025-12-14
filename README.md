# 📝 Full-Stack Django Blog App

A modern **full-stack blog platform** built with **Django**, featuring authentication, post creation, editing, categories, tags, user dashboards, and a premium responsive UI.

This project is designed to be **portfolio-ready**, **freelance-ready**, and easily extendable.

---

## 🚀 Features

### 🔐 Authentication
- User registration & login
- Secure logout
- Session-based authentication

### 📝 Blog System
- Create new blog posts
- Edit own posts
- Delete posts
- Publish & draft system
- Slug-based URLs for SEO

### 👤 User Permissions
- Any logged-in user can write blogs
- Users can edit **their own posts**
- Superusers can edit & delete **any post**

### 🗂 Content Organization
- Categories
- Tags
- Filter posts by category or tag

### 📊 Dashboard
- “My Posts” dashboard for each user
- Manage personal blog posts easily

### 🎨 UI / UX
- Premium card-based layout
- Gradient theme
- Responsive design (mobile + desktop)
- Clean and modern styling

---

## 🛠 Tech Stack

| Layer        | Technology |
|-------------|------------|
| Backend      | Django (Python) |
| Frontend     | HTML, CSS, Vanilla JavaScript |
| Database     | MySQL / SQLite |
| Auth         | Django Authentication |
| Styling      | Custom CSS (No frameworks) |
| Version Ctrl | Git & GitHub |

---

## 📁 Project Structure

blog_platform/
│
├── accounts/ # Authentication logic
├── blog/ # Blog app (posts, categories, tags)
├── templates/ # HTML templates
├── static/ # CSS, JS, assets
├── blog_platform/ # Project settings
├── .env # Environment variables (ignored)
├── manage.py
├── requirements.txt
└── README.md

yaml
Copy code

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the repository
```bash
git clone https://github.com/YOUR_USERNAME/full-stack-Django-blog-app.git
cd full-stack-Django-blog-app
2️⃣ Create virtual environment
bash
Copy code
python -m venv venv
Activate it:

Windows

bash
Copy code
venv\Scripts\activate
Linux / Mac

bash
Copy code
source venv/bin/activate

#3️⃣ Install dependencies

bash
Copy code
pip install -r requirements.txt

#4️⃣ Environment variables
Create a .env file in the root:

env
Copy code
SECRET_KEY=your_secret_key_here
DEBUG=True
DB_NAME=blog_db
DB_USER=root
DB_PASSWORD=your_password
DB_HOST=localhost
DB_PORT=3306
#5️⃣ Database migration
bash
Copy code
python manage.py makemigrations
python manage.py migrate
6️⃣ Create superuser
bash
Copy code
python manage.py createsuperuser
#7️⃣ Run the server
bash
Copy code
python manage.py runserver
Visit:

cpp
Copy code
http://127.0.0.1:8000/
#🔒 Security Notes
.env is excluded using .gitignore

SECRET_KEY is never exposed

Role-based permissions enforced at view level
#👨‍💻 Author

Samin Saikia
Full-Stack Developer
Python • Django • Web Applications
