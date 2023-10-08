import os

from django.core.management import BaseCommand

from users.models import User


class Command(BaseCommand):
    """
    Command for creating a new superuser
    """
    help = 'Create super_user'

    def handle(self, *args, **kwargs):
        admin = User.objects.create(
           username='admin',
           email='kaidohmary@gmail.com',
           is_staff=True,
           is_active=True,
           is_superuser=True
        )

        admin.set_password(os.getenv('ADMIN_PASSWORD'))
        admin.save()
