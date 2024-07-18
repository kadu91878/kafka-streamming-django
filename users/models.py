# users/models.py

from django.db import models

class User(models.Model):
    user_name = models.CharField(max_length=100)
    user_last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)
    validation = models.CharField(max_length=50, default="PENDING")

    def __str__(self):
        return self.email
