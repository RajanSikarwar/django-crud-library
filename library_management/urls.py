"""
URL configuration for library_management project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('books.urls')),
    path('api/accounts/', include('accounts.urls')),
    path('', views.home, name='home'),
    path('login.html', views.login_view, name='login'),
    path('register.html', views.register_view, name='register'),
    path('admin_dashboard.html', views.admin_dashboard, name='admin_dashboard'),
    path('student_dashboard.html', views.student_dashboard, name='student_dashboard'),
]