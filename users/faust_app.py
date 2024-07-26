import os
import django
import faust
from asgiref.sync import sync_to_async

# Set up Django settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'kafka_app.settings')
django.setup()

from django.conf import settings
from django.core.exceptions import ValidationError
from users.models import User

app = faust.App('user_validation_app', broker=f'kafka://{settings.KAFKA_BOOTSTRAP_SERVERS}')

class UserRecord(faust.Record, serializer='json'):
    id: int
    name: str
    email: str

user_topic = app.topic('user_validations', value_type=UserRecord)

@app.agent(user_topic)
async def process_user(users):
    async for user in users:
        try:
            user_validation = User(**user.asdict())
            await sync_to_async(user_validation.full_clean)()  # Validate model data
            await sync_to_async(user_validation.save)()
            print(f"User validation saved: {user_validation}")
        except ValidationError as e:
            print(f"Invalid data: {user.asdict()}, errors: {e}")

if __name__ == '__main__':
    app.main()
