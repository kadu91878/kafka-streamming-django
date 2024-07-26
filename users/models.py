# users/models.py

from django.db import models
from django.core.validators import EmailValidator
from django.core.exceptions import ValidationError
import uuid

class User(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.UUID, editable=False)
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    is_valid = models.BooleanField(default=True)

    def clean(self):
        if not self.name:
            raise ValidationError('Name cannot be empty')
        if not self.email:
            raise ValidationError('Email cannot be empty')

def __str__(self):
        return self.username

