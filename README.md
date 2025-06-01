# Library Management System
The Library Management System is a web-based application developed using Django and Django REST Framework with a MySQL database. It provides RESTful API endpoints that allow administrators to perform full CRUD operations on book records after registering and logging in with a unique email and password. Admins can add, view, update, and delete books securely through authenticated endpoints. Additionally, the system offers a student-facing API endpoint that allows anyone to view the list of available books without requiring authentication.

## Project Overview

A comprehensive Django-based web application for managing library operations, providing features for book management, user authentication, and role-based access control.

## Features

- User Registration and Authentication
- Admin and Student Roles
- Book Management
- Token-based Authentication
- Responsive Web Interface

## Prerequisites

- Python 3.11+
- Django 5.1.7
- MySQL Database

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/RajanSikarwar/django-crud-library.git
cd django-crud-library
```

### 2. Create Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Database Setup

```bash
# Create MySQL Database
mysql -u root -p
CREATE DATABASE library_db;
EXIT;

# Update database settings in settings.py
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'library_db',
        'USER': 'your_username_here',
        'PASSWORD': 'your_password_here',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
```

### 5. Run Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 6. Run Development Server

```bash
python manage.py runserver
```

## Project Structure

```
library_management/
│
├── accounts/             # User authentication app
│   ├── models.py
│   ├── views.py
│   └── serializers.py
│
├── books/                # Book management app
│   ├── models.py
│   ├── views.py
│   └── serializers.py
│
├── library_management/   # Project configuration
│   ├── settings.py
│   └── urls.py
│
├── templates/            # HTML templates
│   ├── base.html
│   ├── register.html
│   └── login.html
│
├── requirements.txt
└── manage.py
```

## User Roles

- **Admin**:
  - Add/Edit/Delete Books

- **Student**:
  - View Available Books

## Authentication

The system uses Token-based authentication with Django REST Framework.

## Contact

Rajan Sikarwar - rajansikarwar.ravindra@gmail.com

Project Link: [https://github.com/RajanSikarwar/django-crud-library.git](https://github.com/RajanSikarwar/django-crud-library.git)
```
