# Library Management System
A comprehensive Django-based web application for managing library operations

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

## API Endpoints

- `/api/accounts/register/` - User Registration
- `/api/accounts/login/` - User Login
- `/api/accounts/logout/` - User Logout
- `/api/books/` - Book Management

## Authentication

The system uses Token-based authentication with Django REST Framework.

## Security Features

- Password Hashing
- Token-based Authentication
- Role-based Access Control
- CSRF Protection

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

Distributed under the MIT License. See `LICENSE` for more information.

## Contact

Name - rajansikarwar.ravindra@gmail.com

Project Link: [https://github.com/RajanSikarwar/django-crud-library.git](https://github.com/RajanSikarwar/django-crud-library.git)
```