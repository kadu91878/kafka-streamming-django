import json
import random
import time
from kafka import KafkaProducer
from django.conf import settings

producer = KafkaProducer(
    bootstrap_servers=[settings.KAFKA_BOOTSTRAP_SERVERS],
    value_serializer=lambda v: json.dumps(v).encode('utf-8'),
    api_version=(3, 0, 0)
)

def generate_data():
    # Generate both valid and invalid data for testing purposes
    valid_data = {
        "id": random.randint(1, 1000),
        "name": "Valid User",
        "email": "valid_user@example.com",
        "is_valid": True
    }
    invalid_data = {
        "id": random.randint(1, 1000),
        "name": "",  # Invalid because the name is empty
        "email": "invalid_user@invalid",  # Invalid email format
        "is_valid": False
    }
    return random.choice([valid_data, invalid_data])

def add_entry():
    data = generate_data()
    producer.send('user_validations', value=data)
    producer.flush()
    print(f"Sent data: {data}")
    time.sleep(30)  # Adjust the sleep time as necessary
    add_entry()  # Recursively call to continue producing data

if __name__ == "__main__":
    add_entry()
