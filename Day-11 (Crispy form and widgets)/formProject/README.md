# Django Product Form CRUD

[![Python](https://img.shields.io/badge/Python-3.12%2B-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![Django](https://img.shields.io/badge/Django-6.1-092E20?logo=django&logoColor=white)](https://www.djangoproject.com/)
[![Bootstrap](https://img.shields.io/badge/Bootstrap-5.3-7952B3?logo=bootstrap&logoColor=white)](https://getbootstrap.com/)
[![Crispy Forms](https://img.shields.io/badge/django--crispy--forms-2.7-0C4B33)](https://django-crispy-forms.readthedocs.io/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](#license)

## Description

A focused Django CRUD application for managing products through reusable Django templates and a styled `ModelForm`. It is intended for learners and developers practicing database-backed forms, image uploads, Bootstrap 5 widgets, and named URL navigation.

## Contents

- [Key Features](#key-features)
- [Tech Stack](#tech-stack)
- [Getting Started](#getting-started)
- [Environment Variables](#environment-variables)
- [Usage](#usage)
- [Django Template Setup](#django-template-setup)
- [Context Data](#context-data)
- [Navigation Page Using URL Names](#navigation-page-using-url-names)
- [License](#license)

## Key Features

- **Product CRUD:** Create, view, update, and delete product records.
- **Image uploads:** Store product images with `ImageField` and serve them during development.
- **Model-backed forms:** Generate form fields from `productModel` with `productForm`.
- **Crispy rendering:** Render forms with `django-crispy-forms` and the Bootstrap 5 template pack.
- **Reusable templates:** Share layout and navigation through `master/base.html` and included templates.
- **Named navigation:** Use Django URL names such as `productList` and `addProduct` from templates and views.
- **SQLite database:** Start quickly with the included `db.sqlite3` database configuration.

## Tech Stack

| Technology          | Purpose                       |
| ------------------- | ----------------------------- |
| Python              | Application runtime           |
| Django 6.1          | Web framework and ORM         |
| SQLite              | Local database                |
| Pillow              | Image field support           |
| django-crispy-forms | Form rendering                |
| crispy-bootstrap5   | Bootstrap 5 Crispy Forms pack |
| Bootstrap 5.3       | Interface styling             |

## Getting Started

### Prerequisites

- Python 3.12 or newer
- `pip`
- A terminal opened in this directory: `Day-11 (Crispy form and widgets)/formProject`

### Installation

From the project directory, create and activate a virtual environment, then install the dependencies:

```bash
python -m venv .venv
```

Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

macOS/Linux:

```bash
source .venv/bin/activate
```

Install the required packages:

```bash
python -m pip install -r ../../requirements.txt
```

Before running image uploads, add the following development media settings to `formProject/settings.py`:

```python
MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"
```

Apply migrations:

```bash
python manage.py migrate
```

### Run

Start Django's development server:

```bash
python manage.py runserver
```

Open [http://127.0.0.1:8000/](http://127.0.0.1:8000/) to view the product list. The Django admin is available at [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/).

Create an administrator when needed:

```bash
python manage.py createsuperuser
```

## Environment Variables

This learning project currently uses hard-coded development settings and does not require environment variables. For production, move `SECRET_KEY`, `DEBUG`, `ALLOWED_HOSTS`, database credentials, and media storage configuration into environment variables before deployment.

Example production configuration:

```env
DJANGO_SECRET_KEY=replace-with-a-secure-secret
DJANGO_DEBUG=False
DJANGO_ALLOWED_HOSTS=example.com,www.example.com
```

## Usage

1. Visit `/` to review all saved products.
2. Select **Add Product**, complete the form, and optionally upload an image.
3. Select **Edit** to update a product.
4. Select **Delete** to remove a product.

The form accepts these model fields:

```text
product_name
product_price
product_description
product_qty
product_img
```

## Django Template Setup

Templates are discovered inside the app because `APP_DIRS` is enabled. A shared base template provides the document shell, Bootstrap assets, and a navigation include:

```python
# formProject/settings.py
TEMPLATES = [
	{
		"BACKEND": "django.template.backends.django.DjangoTemplates",
		"DIRS": [],
		"APP_DIRS": True,
	},
]
```

Extend the base template from a page template:

```django
{% extends "master/base.html" %}

{% block content %}
  <h1>Product List</h1>
{% endblock %}
```

Render the Crispy Forms form with CSRF protection and multipart encoding for image uploads:

```django
{% load crispy_forms_tags %}

<form method="post" enctype="multipart/form-data">
  {% csrf_token %}
  {{ form_data|crispy }}
  <button type="submit">Save</button>
</form>
```

## Context Data

Views pass values to templates through a context dictionary. The list page receives the product queryset:

```python
def productList(request):
	products = productModel.objects.all()
	return render(request, "productList.html", {"products": products})
```

The shared form template receives the form instance and display labels:

```python
context = {
	"form_data": productForm(),
	"form_heading": "Add Product Form",
	"form_btn": "Add Product",
}
return render(request, "master/base-form.html", context)
```

Read context values in a template with Django's variable syntax:

```django
<h2>{{ form_heading }}</h2>
{{ form_data|crispy }}
<button type="submit">{{ form_btn }}</button>
```

## Navigation Page Using URL Names

The app defines named routes in `formApp/urls.py`:

```python
from django.urls import path
from formApp.views import addProduct, deleteProduct, editProduct, productList

urlpatterns = [
	path("", productList, name="productList"),
	path("add-product/", addProduct, name="addProduct"),
	path("edit-product/<str:p_id>", editProduct, name="editProduct"),
	path("delete-product/<str:p_id>", deleteProduct, name="deleteProduct"),
]
```

Use the URL names instead of hard-coding paths in templates:

```django
<a href="{% url 'productList' %}">Products</a>
<a href="{% url 'addProduct' %}">Add Product</a>
<a href="{% url 'editProduct' product.id %}">Edit</a>
<a href="{% url 'deleteProduct' product.id %}">Delete</a>
```

Redirect to a named route after a successful form submission:

```python
return redirect("productList")
```

## License

This project is licensed under the MIT License. Add an `LICENSE` file containing the standard MIT license text before distributing the project.
