# Django Authentication Project

[![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Django](https://img.shields.io/badge/Django-6.1-092E20?style=for-the-badge&logo=django&logoColor=white)](https://www.djangoproject.com/)
[![SQLite](https://img.shields.io/badge/SQLite-Local%20database-003B57?style=for-the-badge&logo=sqlite&logoColor=white)](https://www.sqlite.org/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)]

## Description

A focused Django authentication project for learning and demonstrating custom-user registration, session-based login and logout, and protected views. It is intended for students and Django developers who want a small, runnable reference for authentication fundamentals.

## Key Features

- **Custom user model:** Extends Django's `AbstractUser` with user type, gender, and education fields.
- **User registration:** Creates accounts with profile information and password confirmation.
- **Session authentication:** Authenticates users with Django's built-in `authenticate()` and `login()` utilities.
- **Protected dashboard:** Uses `@login_required` to restrict dashboard access to signed-in users.
- **Logout flow:** Clears the authenticated session and redirects users to the sign-in page.
- **Django Admin:** Registers the custom user model for administrative management.
- **SQLite persistence:** Includes a local SQLite database for development and classroom use.

## Tech Stack

| Technology       | Purpose                                 |
| ---------------- | --------------------------------------- |
| Python 3.x       | Programming language                    |
| Django 6.1       | Web framework and authentication system |
| SQLite           | Local development database              |
| Django Templates | Server-rendered user interface          |

## Django Template Setup

Enable Django's template engine to discover templates stored inside an installed app:

```python
# authProject/settings.py
TEMPLATES = [
	{
		'BACKEND': 'django.template.backends.django.DjangoTemplates',
		'DIRS': [],
		'APP_DIRS': True,
	},
]
```

With `APP_DIRS=True`, Django searches the `templates/` directory inside `authApp`. The shared layout is loaded by child templates with template inheritance:

```django
{# authApp/templates/dashboard.html #}
{% extends 'master/base.html' %}

{% block content %}
  <h1>Profile Information</h1>
{% endblock %}
```

The base template includes the reusable navigation on every page:

```django
{# authApp/templates/master/base.html #}
{% include 'master/nav.html' %}
{% block content %}{% endblock content %}
```

## Context Data

Views render templates with `render()`. The dashboard uses Django's authentication context processor, so the signed-in user is available as `user` without manually adding it to the view context:

```python
# authApp/views.py
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

@login_required
def dashboard(request):
	return render(request, 'dashboard.html')
```

Read the authenticated user's data in the template with Django template variables:

```django
<p>{{ user.first_name }} {{ user.last_name }}</p>
<p>{{ user.email }}</p>
<p>{{ user.Education }}</p>
```

For page-specific values, pass a context dictionary from the view:

```python
return render(
	request,
	'contacts.html',
	{'page_title': 'Contacts'},
)
```

```django
<h1>{{ page_title }}</h1>
```

## Navigation Page Using URL Names

Define a stable name for each route in the app URL configuration:

```python
# authApp/urls.py
from django.urls import path
from authApp.views import contacts

urlpatterns = [
	path('contacts/', contacts, name='contacts'),
]
```

Use the `{% url %}` template tag instead of hard-coding the path. The Contacts link is the first item in the navigation menu:

```django
{# authApp/templates/master/nav.html #}
<a class="nav-link" href="{% url 'contacts' %}">Contacts</a>
```

If the URL path changes later, templates using the route name continue to work as long as `name='contacts'` remains unchanged.

## Getting Started

### Prerequisites

- Python 3.x
- Git
- PowerShell on Windows or a POSIX-compatible shell on macOS/Linux

### Installation

From the repository root, create and activate a virtual environment and install the shared dependencies:

```powershell
python -m venv env
.\env\Scripts\Activate.ps1
pip install -r requirements.txt
```

For macOS or Linux:

```bash
python3 -m venv env
source env/bin/activate
pip install -r requirements.txt
```

Change to this project's directory before running Django commands:

```bash
cd "Day-8(Login ,Logout and Login_required method)/authProject"
```

### Run the Project

Apply database migrations and start Django's development server:

```bash
python manage.py migrate
python manage.py runserver
```

Open [http://127.0.0.1:8000/](http://127.0.0.1:8000/) in a browser. Stop the server with `Ctrl+C`.

To create an administrator account:

```bash
python manage.py createsuperuser
```

Then open [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/).

## Environment Variables

This project does not currently read environment variables. Its secret key, debug mode, allowed hosts, and SQLite database configuration are defined directly in `authProject/settings.py`.

For production deployment, move the secret key and other deployment settings to environment variables, set `DEBUG=False`, configure `ALLOWED_HOSTS`, and use a production-ready database and web server.

## Usage

### Usage Details

1. Open `/signup/` and submit a username, password, password confirmation, and profile details.
2. Open `/` to sign in with the newly created account.
3. After authentication, Django redirects to `/dashboard/`.
4. Open `/contacts/` from the first navigation menu item.
5. Visit `/logout/` to end the session and return to the sign-in page.

The contacts page is protected in the same way as the dashboard:

```python
from django.contrib.auth.decorators import login_required

@login_required
def contacts(request):
	return render(request, 'contacts.html')
```

Unauthenticated users are redirected to the sign-in route configured by `LOGIN_URL = 'signin'`.

### Available Routes

| Route         | Purpose                             | Access          |
| ------------- | ----------------------------------- | --------------- |
| `/`           | Sign-in form and login submission   | Public          |
| `/signup/`    | Create a user account               | Public          |
| `/contacts/`  | Display the contacts page           | Signed-in users |
| `/dashboard/` | Display the authenticated dashboard | Signed-in users |
| `/logout/`    | Log out the current user            | Signed-in users |
| `/admin/`     | Django administration               | Staff users     |

## License

This project is licensed under the MIT License.
