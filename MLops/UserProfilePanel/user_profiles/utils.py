# user_profiles/utils.py
import random
from faker import Faker
from user_profiles.models import UserProfile
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import Permission

fake = Faker()

def generate_areas_of_interest():
    areas_of_interest = random.sample([
        'Technology and Innovation', 'Business and Management', 'Healthcare and Medicine',
        'Engineering and Manufacturing', 'Finance and Economics', 'Education and Training',
        'Legal and Regulatory Affairs', 'Environmental and Sustainability Issues',
        'Creative Industries', 'Science and Research', 'Human Resources and Organizational Behavior',
        'Information Technology and Data Analysis', 'Public Policy and Governance',
        'Arts and Culture', 'Real Estate and Urban Planning', 'Hospitality and Tourism',
        'Transportation and Logistics', 'Sports and Fitness'
    ], random.randint(2, 4))
    return areas_of_interest

# user_profiles/utils.py
from django.contrib.contenttypes.models import ContentType

# ... (previous code)

def generate_fake_user_profiles(num_profiles=25):
    content_type = ContentType.objects.get_for_model(UserProfile)

    for _ in range(num_profiles):
        areas_of_interest = generate_areas_of_interest()
        about = fake.sentence()
        user = UserProfile.objects.create(
            username=fake.user_name(),
            password=fake.password(),
            about=about,
            areas_of_interest=', '.join(areas_of_interest)
        )

        # Create permissions and add them to the user
        permission_codename = f'can_{fake.word()}'
        permission, created = Permission.objects.get_or_create(
            codename=permission_codename,
            content_type=content_type
        )
        user.user_permissions.add(permission)

# user_profiles/utils.py
def display_user_info():
    users = UserProfile.objects.all()
    for user in users:
        print(f"Username: {user.username}")
        print(f"Password: {user.password}")  # Note: This should not be displayed in a real-world scenario
        print(f"About: {user.about}")
        print(f"Areas of Interest: {user.areas_of_interest}")

        # Access the groups and user_permissions attributes directly
        print(f"Groups: {', '.join(group.name for group in user.groups.all())}")
        print(f"User Permissions: {', '.join(perm.codename for perm in user.user_permissions.all())}")

        print("\n")

