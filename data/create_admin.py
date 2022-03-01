import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings.common")
from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth import get_user_model
User=get_user_model()
user=User.objects.create_user(os.getenv('ADMIN_USER', 'admin'), email=os.getenv('ADMIN_EMAIL', 'admin@bibbox.org'), password=os.getenv('ADMIN_PASSWORD', 'psw'))
user.is_superuser=True
user.is_staff=True
user.save()

