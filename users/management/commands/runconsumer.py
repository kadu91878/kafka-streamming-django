from django.core.management.base import BaseCommand
from users import consumer  # Importe o módulo consumer

class Command(BaseCommand):
    help = 'Run the Kafka consumer'

    def handle(self, *args, **kwargs):
        consumer.run()
