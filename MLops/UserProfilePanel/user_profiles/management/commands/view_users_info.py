# user_profiles/management/commands/view_users_info.py
from django.core.management.base import BaseCommand
from user_profiles.utils import display_user_info, generate_fake_user_profiles

class Command(BaseCommand):
    help = 'View user information'

    def handle(self, *args, **kwargs):
        # Generate fake user profiles before displaying information
        generate_fake_user_profiles()

        # Display user information
        display_user_info()
