from django.core.management.base import BaseCommand
from users import entry_adder  # Importe o módulo entry_adder

class Command(BaseCommand):
    help = 'Run the Kafka producer'

    def handle(self, *args, **kwargs):
        entry_adder.add_entry()
