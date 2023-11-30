# user_profiles/models.py
from django.db import models
from django.contrib.auth.models import AbstractUser

class UserProfile(AbstractUser):
    about = models.TextField(blank=True)
    areas_of_interest = models.CharField(max_length=255, blank=True)

    # Add related_name to avoid clash with auth.User model
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='user_profiles',
        blank=True,
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
    )

    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='user_profiles',
        blank=True,
        help_text='Specific permissions for this user.',
    )

    def __str__(self):
        return self.username
