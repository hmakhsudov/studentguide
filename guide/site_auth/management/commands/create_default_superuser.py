from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = 'Create a default superuser using the default Django user model'

    def handle(self, *args, **options):
        UserModel = get_user_model()
        username = input('Username: ')
        email = input('Email: ')
        password = input('Password: ')

        UserModel.objects.create_superuser(username=username, email=email, password=password)
        self.stdout.write(self.style.SUCCESS('Default superuser created successfully'))
