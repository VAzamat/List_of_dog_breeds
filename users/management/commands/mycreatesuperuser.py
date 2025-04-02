from django.core.management import BaseCommand
from users.models import User

import os
SUPERUSER_PASSWORD = os.environ.get('DJANGO_PROJECT_SUPERUSER_PASSWORD')
SUPERUSER_EMAIL = os.environ.get('DJANGO_PROJECT_SUPERUSER_EMAIL')

class Command(BaseCommand):

    def handle(self, *args, **options):
        user = User.objects.create(
            email=SUPERUSER_EMAIL,
            first_name='Admin',
            last_name='DatabaseAdmin',
            is_staff=True,
            is_superuser=True
        )

        user.set_password(SUPERUSER_PASSWORD)
        user.save()
