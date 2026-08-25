# 🚀 Web Application Development with Python

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/Django-6.1-092E20?style=for-the-badge&logo=django&logoColor=white" alt="Django">
  <img src="https://img.shields.io/badge/SQLite-Database-003B57?style=for-the-badge&logo=sqlite&logoColor=white" alt="SQLite">
  <img src="https://img.shields.io/badge/Git-GitHub-F05032?style=for-the-badge&logo=git&logoColor=white" alt="Git">
  <img src="https://img.shields.io/badge/Bootstrap-5-7952B3?style=for-the-badge&logo=bootstrap&logoColor=white" alt="Bootstrap">
</p>

<p align="center">
  <strong>Web Application Development with Python</strong>
</p>

<p align="center">
  A practical, class-wise repository containing Django projects, CRUD operations,
  authentication systems, forms, image handling, database relationships,
  and real-world web application development practice.
</p>

---

# 📖 Context

This repository contains my learning journey and practical work from the **Web Application Development with Python** course.

The repository is organized class-wise and project-wise so that each topic can be studied independently while keeping the complete development journey connected.

The main focus of this repository is **Python-based web application development using Django**.

Throughout the classes and projects, the repository covers:

- Python and Django development environment setup
- Django project and application structure
- Models and database operations
- Django Admin
- URL routing
- Views
- Templates
- CRUD operations
- HTML form handling
- Image upload and management
- Custom user model
- User registration and authentication
- Login and logout
- Protected pages using `login_required`
- Django Model Forms
- Crispy Forms
- Bootstrap 5 form rendering
- ForeignKey relationships
- User-specific data filtering
- Practical web application projects

---

# 🎯 Learning Objectives

The purpose of this repository is to build a strong practical foundation in Django web application development.

By working through these classes and projects, I am learning how to:

- Understand Django project architecture
- Create Django projects and applications
- Configure Django environments
- Design database models
- Perform database operations using Django ORM
- Register and manage models through Django Admin
- Create URL patterns
- Develop Django views
- Render dynamic data using templates
- Process HTML form submissions
- Implement Create, Read, Update and Delete operations
- Upload and manage images
- Build custom user models
- Implement user registration
- Implement login and logout functionality
- Protect pages using authentication
- Build reusable Django forms
- Use Django ModelForm
- Customize form widgets
- Integrate Crispy Forms
- Use Bootstrap 5 with Django forms
- Create relationships between database models
- Build practical Django applications

---

# 🛠️ Technologies & Tools

| Technology / Tool | Purpose |
|---|---|
| 🐍 Python | Programming Language |
| 🚀 Django 6.1 | Web Framework |
| 🗄️ SQLite | Database |
| 🎨 Bootstrap 5 | Frontend UI |
| 📝 Django Forms | Form Handling |
| 🧩 Django ModelForm | Database-backed Forms |
| ✨ django-crispy-forms | Form Rendering |
| 🎨 crispy-bootstrap5 | Bootstrap 5 Integration |
| 🖼️ Pillow | Image Processing |
| 🔀 Git | Version Control |
| 🐙 GitHub | Repository Hosting |
| 💻 VS Code | Development Environment |

---

# 📚 Course Contents

The current repository is organized into the following major learning stages.

## 1. 🏗️ Django Fundamentals

- Django installation
- Virtual environment
- Django project creation
- Django application creation
- Project structure
- Models
- Database
- Django Admin
- Views
- URLs
- Templates
- Reading data from database

---

## 2. 📝 HTML Form Based CRUD

- HTML form handling
- POST request
- GET request
- Creating database records
- Reading database records
- Updating records
- Deleting records
- Student management
- Teacher management

---

## 3. 🖼️ CRUD with Image Upload

- ImageField
- File upload
- `request.FILES`
- Media files
- Profile image
- Create operation
- Read operation
- Update operation
- Delete operation

---

## 4. 👤 Custom User & Signup

- Django `AbstractUser`
- Custom user model
- User type
- Gender
- Education information
- User registration
- Password confirmation
- Custom authentication model configuration

---

## 5. 🔐 Authentication

- User authentication
- Login
- Logout
- `authenticate()`
- `login()`
- `logout()`
- `login_required`
- Protected dashboard

---

## 6. 🔗 Database Relationships & Todo Application

- Custom User Model
- Task Model
- ForeignKey relationship
- User-specific tasks
- Task status
- Due date
- Created date
- Create Task
- Edit Task
- Delete Task
- Task listing
- User registration
- User login/logout

---

## 7. 🧩 Django ModelForm

- Django Forms
- ModelForm
- Form validation
- Form rendering
- Create operation using ModelForm
- Update operation using ModelForm
- Delete operation
- File upload through ModelForm

---

## 8. ✨ Crispy Forms & Widgets

- Django Crispy Forms
- Crispy Bootstrap 5
- Form rendering
- Bootstrap 5 integration
- Form widgets
- Custom form presentation

---

# 📂 Repository Structure

The repository currently follows a practical class/project-based structure:

```text
WADP_B-01/
│
├── README.md
│
├── requirements.txt
│
├── .gitignore
│
├── myProject
│   (Django installation. Environment and project create,
│    Model, admin, views, urls, and Read Data)/
│   │
│   ├── manage.py
│   ├── db.sqlite3
│   │
│   ├── myProject/
│   │   ├── settings.py
│   │   ├── urls.py
│   │   ├── asgi.py
│   │   └── wsgi.py
│   │
│   └── myApp/
│       ├── models.py
│       ├── views.py
│       ├── urls.py
│       ├── admin.py
│       ├── migrations/
│       └── templates/
│
├── project1
│   (CRUD Operation using HTML Form)/
│   │
│   ├── manage.py
│   ├── db.sqlite3
│   │
│   ├── project1/
│   │   ├── settings.py
│   │   ├── urls.py
│   │   ├── asgi.py
│   │   └── wsgi.py
│   │
│   └── projectApp/
│       ├── models.py
│       ├── views.py
│       ├── urls.py
│       ├── admin.py
│       ├── migrations/
│       └── templates/
│
├── Day-6(CRUD Operation with Image)/
│   │
│   └── myProject/
│       ├── manage.py
│       ├── db.sqlite3
│       │
│       ├── myProject/
│       │   ├── settings.py
│       │   ├── urls.py
│       │   ├── asgi.py
│       │   └── wsgi.py
│       │
│       └── myApp/
│           ├── models.py
│           ├── views.py
│           ├── urls.py
│           ├── admin.py
│           ├── migrations/
│           └── templates/
│
├── Day-7(Django Signup operation using Abstract User)/
│   │
│   └── authProject/
│       ├── manage.py
│       │
│       ├── authProject/
│       │   ├── settings.py
│       │   ├── urls.py
│       │   ├── asgi.py
│       │   └── wsgi.py
│       │
│       └── authApp/
│           ├── models.py
│           ├── views.py
│           ├── urls.py
│           ├── admin.py
│           ├── migrations/
│           └── templates/
│
├── Day-8(Login ,Logout and Login_required method)/
│   │
│   └── authProject/
│       ├── manage.py
│       │
│       ├── authProject/
│       │   ├── settings.py
│       │   ├── urls.py
│       │   ├── asgi.py
│       │   └── wsgi.py
│       │
│       └── authApp/
│           ├── models.py
│           ├── views.py
│           ├── urls.py
│           ├── admin.py
│           ├── migrations/
│           └── templates/
│
├── todo_project
│   (To Do Project using ForeignKey relationship)/
│   │
│   ├── manage.py
│   ├── db.sqlite3
│   │
│   ├── todo_project/
│   │   ├── settings.py
│   │   ├── urls.py
│   │   ├── asgi.py
│   │   └── wsgi.py
│   │
│   └── tasks/
│       ├── models.py
│       ├── views.py
│       ├── forms.py
│       ├── urls.py
│       ├── admin.py
│       ├── migrations/
│       └── templates/
│
├── Day-10(Crud Operation using Django Form)/
│   │
│   └── formProject/
│       ├── manage.py
│       │
│       ├── formProject/
│       │   ├── settings.py
│       │   ├── urls.py
│       │   ├── asgi.py
│       │   └── wsgi.py
│       │
│       └── formApp/
│           ├── models.py
│           ├── views.py
│           ├── forms.py
│           ├── urls.py
│           ├── admin.py
│           ├── migrations/
│           └── templates/
│
└── Day-11 (Crispy form and widgets)/
    │
    └── formProject/
        ├── manage.py
        │
        ├── formProject/
        │   ├── settings.py
        │   ├── urls.py
        │   ├── asgi.py
        │   └── wsgi.py
        │
        └── formApp/
            ├── models.py
            ├── views.py
            ├── forms.py
            ├── urls.py
            ├── admin.py
            ├── migrations/
            └── templates/