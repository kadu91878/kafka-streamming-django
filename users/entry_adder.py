import json
import random
import time
import uuid
from kafka import KafkaProducer
from django.conf import settings

producer = KafkaProducer(
    bootstrap_servers=[settings.KAFKA_BOOTSTRAP_SERVERS],
    value_serializer=lambda v: json.dumps(v).encode('utf-8'),
    api_version=(3, 0, 0)
)

def generate_data():
    # Generate random valid or invalid data
    valid_data = {
        "id": str(uuid.uuid4()),  # Generate a new UUID for each entry
        "name": "Valid User",
        "email": f"valid_user_{uuid.uuid4()}@example.com",  # Unique email
        "is_valid": True
    }
    invalid_data = {
        "id": str(uuid.uuid4()),  # Generate a new UUID for each entry
        "name": "",  # Invalid because the name is empty
        "email": "invalid_user@invalid",  # Invalid email format
        "is_valid": False
    }
    return random.choice([valid_data, invalid_data])

def add_entry():
    try:
        start_time = time.time()
        messages_sent = 0
        while True:
            data = generate_data()
            producer.send('user_validations', value=data)
            messages_sent += 1
            current_time = time.time()
            elapsed_time = current_time - start_time
            if elapsed_time < 1:
                if messages_sent >= 1000:
                    time.sleep(1 - elapsed_time)
                    start_time = current_time
                    messages_sent = 0
            else:
                start_time = current_time
                messages_sent = 0
            print(f"Sent data: {data}")
    except KeyboardInterrupt:
        print("Stopping producer...")
    finally:
        producer.close()

if __name__ == "__main__":
    add_entry()
