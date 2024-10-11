
# users/views.py
from django.shortcuts import render
from .models import User # Import your User model

def user_list(request):
    users = User.objects.all()  # Fetch all users
    return render(request, 'users/user_list.html', {'users': users})  # Pass users to the template
