from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def login_view(request):
    return render(request, 'login.html')

def register_view(request):
    return render(request, 'register.html')

def admin_dashboard(request):
    return render(request, 'admin_dashboard.html')

def student_dashboard(request):
    return render(request, 'student_dashboard.html')