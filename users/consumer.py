# users/consumer.py

from confluent_kafka import Consumer, KafkaError
import os
import django
import sys

# Adicione o diretório do projeto ao sys.path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Defina o módulo de configurações do Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'kafka.settings')

# Configure o Django
django.setup()

from users.models import User
import json

kafka_bootstrap_servers = os.getenv('KAFKA_BOOTSTRAP_SERVERS', 'localhost:9092')

c = Consumer({
    'bootstrap.servers': kafka_bootstrap_servers,
    'group.id': 'mygroup',
    'auto.offset.reset': 'earliest'
})

c.subscribe(['user_validations'])

def validate_user(user_data):
    # Implement your validation logic here
    if "@" in user_data['email']:
        return "PROCESSAMENTO_VALIDO"
    return "PROCESSAMENTO_NAO_VALIDO"

while True:
    msg = c.poll(1.0)
    if msg is None:
        continue
    if msg.error():
        if msg.error().code() == KafkaError._PARTITION_EOF:
            continue
        else:
            print(msg.error())
            break

    user_data = json.loads(msg.value().decode('utf-8'))
    validation_status = validate_user(user_data)
    
    user = User.objects.get(email=user_data['email'])
    user.validation = validation_status
    user.save()

c.close()
