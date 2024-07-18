# users/consumer.py

import json
from kafka import KafkaConsumer
from django.conf import settings
from .models import UserValidation
from django.core.exceptions import ValidationError

consumer = KafkaConsumer(
    'user_validations',
    bootstrap_servers=[settings.KAFKA_BOOTSTRAP_SERVERS],
    auto_offset_reset='earliest',
    enable_auto_commit=True,
    group_id='my-group',
    value_deserializer=lambda x: json.loads(x.decode('utf-8'))
)

for message in consumer:
    user_data = message.value
    try:
        user_validation = UserValidation(**user_data)
        user_validation.full_clean()  # Validate model data
        user_validation.save()
        print(f"User validation saved: {user_validation}")
    except ValidationError as e:
        print(f"Invalid data: {user_data}, errors: {e}")
