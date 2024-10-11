from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):  # Extending Django's default user model
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    staff_status = models.BooleanField(default=False)

    def __str__(self):
        return self.username  # Default field 'username' from AbstractUser
