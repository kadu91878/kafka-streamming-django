# users/entry_adder.py

import random
import string
from .models import User
from .producer import produce_user_data

def add_entries():
    for _ in range(10):
        user_data = {
            'user_name': ''.join(random.choices(string.ascii_letters, k=5)),
            'user_last_name': ''.join(random.choices(string.ascii_letters, k=5)),
            'email': ''.join(random.choices(string.ascii_letters, k=5)) + '@example.com',
            'password': ''.join(random.choices(string.ascii_letters + string.digits, k=8)),
            'validation': 'PENDING'
        }
        
        user = User.objects.create(**user_data)
        produce_user_data(user_data)
