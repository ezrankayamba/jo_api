from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth.models import User

import random
import string


class Command(BaseCommand):
    help = 'Add or update credentials of a user$ python manage.py <username>'

    def add_arguments(self, parser):
        parser.add_argument('username', nargs='+', type=str)

    def new_password(self, length=8):
        letters = string.ascii_lowercase
        return ''.join(random.choice(letters) for i in range(length))

    def handle(self, *args, **options):
        if 'username' in options:
            username = options['username'][0]

            password = self.new_password()
            exist = User.objects.filter(username=username).first()
            if exist:
                print("Updating credentials for user: ", username)
                exist.delete()
                user = User.objects.create_user(username, None, password)
            else:
                print("Creating credentials for user: ", username)
                user = User.objects.create_user(username, None, password)
            print("New password: ", password)
        else:
            print('No username provided')
