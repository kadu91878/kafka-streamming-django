# users/models.py

from django.db import models
from django.core.validators import EmailValidator
from django.core.exceptions import ValidationError

class User(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    email = models.EmailField(validators=[EmailValidator()])
    is_valid = models.BooleanField(default=True)

    def clean(self):
        if not self.name:
            raise ValidationError('Name cannot be empty')
        if not self.email:
            raise ValidationError('Email cannot be empty')

def __str__(self):
        return self.username

