# Django Custom User Signup

[![Python](https://img.shields.io/badge/Python-3.12%2B-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![Django](https://img.shields.io/badge/Django-6.1-092E20?logo=django&logoColor=white)](https://www.djangoproject.com/)
[![Database](https://img.shields.io/badge/Database-SQLite-003B57?logo=sqlite&logoColor=white)](https://www.sqlite.org/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](#license)

## Description

A focused Django authentication project that demonstrates user registration with a custom user model based on `AbstractUser`. It is intended for Django learners and developers who need a starting point for collecting profile fields such as user type, gender, and education alongside the standard account details.

## Key Features

- **Custom user model:** Extends Django's `AbstractUser` with `UserType`, `Gender`, and `Education` fields.
- **Signup workflow:** Creates users with Django's password hashing through `create_user()`.
- **Profile choices:** Restricts user type to Teacher or Student and gender to Male or Female.
- **CSRF protection:** Includes Django CSRF tokens in the registration form.
- **Admin integration:** Registers the custom user model with the Django admin site.
- **SQLite development database:** Runs with the included `db.sqlite3` configuration.

## Tech Stack

| Technology | Version / Purpose          |
| ---------- | -------------------------- |
| Python     | 3.12+ recommended          |
| Django     | 6.1                        |
| SQLite     | Local development database |
| Bootstrap  | 5.3 via CDN                |

## Getting Started

### Prerequisites

- Python 3.12 or newer
- `pip`
- A terminal with permission to create a virtual environment

### Installation

Run these commands from the repository root:

```bash
cd "Day-7(Django Signup operation using Abstract User)/authProject"
python -m venv .venv
```

Activate the virtual environment:

```powershell
# Windows PowerShell
.venv\Scripts\Activate.ps1
```

```bash
# macOS or Linux
source .venv/bin/activate
```

Install the shared project dependencies:

```bash
python -m pip install --upgrade pip
python -m pip install -r ../../requirements.txt
```

### Run the Application

Apply migrations and start Django's development server:

```bash
python manage.py migrate
python manage.py runserver
```

Open [http://127.0.0.1:8000/](http://127.0.0.1:8000/) in a browser.

To access the admin site, create an administrator account first:

```bash
python manage.py createsuperuser
```

Then open [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/).

## Environment Variables

No environment variables are required by the current implementation. The development settings currently define `SECRET_KEY`, `DEBUG`, and `ALLOWED_HOSTS` directly in `authProject/settings.py`.

For any deployment beyond local development, move those values to environment variables and set `DEBUG=False` before exposing the application publicly.

## Usage

### Register a User

Visit the signup page:

```text
http://127.0.0.1:8000/
```

The form submits these fields using `POST`:

```html
<form method="POST">
  {% csrf_token %}
  <input name="fname" type="text" />
  <input name="lname" type="text" />
  <input name="username" type="text" />
  <input name="email" type="email" />
  <input name="password" type="password" />
  <input name="conf_password" type="password" />
  <select name="userType">
    ...
  </select>
  <select name="gender">
    ...
  </select>
  <input name="education" type="text" />
  <button type="submit">Signup</button>
</form>
```

The signup view validates that both password fields match, creates the account with Django's password hashing, saves the additional profile fields, and redirects to `/signin/`:

```python
if password == conf_password:
		user = custumModel.objects.create_user(
				username=username,
				password=conf_password,
		)
		user.first_name = fname
		user.last_name = lname
		user.email = email
		user.UserType = userType
		user.Gender = gender
		user.Education = education
		user.save()
		return redirect("signin")
```

For a successful browser submission, choose `Teacher` or `Student` for `userType` and `Male` or `Female` for `gender`. A password mismatch redirects back to `/`.

### Inspect Users in Admin

Create a superuser and open the admin site:

```bash
python manage.py createsuperuser
```

```text
http://127.0.0.1:8000/admin/
```

The `/signin/` route is currently a placeholder view and does not authenticate users yet.

The `/signin/` route is currently a placeholder view and does not authenticate users yet.

## License

This project is licensed under the MIT License. Add a `LICENSE` file containing the full MIT License text before distributing the project.
