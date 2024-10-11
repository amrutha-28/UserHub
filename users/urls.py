from django.urls import path
from .views import user_list  # Import the user_list view

urlpatterns = [
    path('', user_list, name='user_list'),  # Base URL for users app
]