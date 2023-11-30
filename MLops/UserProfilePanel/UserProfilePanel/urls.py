"""UserProfilePanel URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# UserProfilePanel/urls.py
# UserProfilePanel/urls.py

from django.contrib import admin
from django.urls import path, include
from user_profiles.views import UserListView  # Import the new UserListView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('user_profiles.urls')),  # Use 'api/' prefix for the API URLs
    path('users/', UserListView.as_view(), name='user-list-view'),  # Add a view for the user list
]

