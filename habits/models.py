from django.db import models
from django.contrib.auth.models import User  # For user accounts

# Habit model
class Habit(models.Model):
    name = models.CharField(max_length=255)  # Name of the habit
    description = models.TextField(blank=True)  # Optional description of the habit
    created_at = models.DateTimeField(auto_now_add=True)  # Timestamp for habit creation

    def __str__(self):
        return self.name

# Group model
class Group(models.Model):
    name = models.CharField(max_length=255)  # Name of the group
    description = models.TextField(blank=True)  # Optional description of the group
    created_at = models.DateTimeField(auto_now_add=True)  # Timestamp for group creation
    members = models.ManyToManyField(User, related_name='custom_groups')  # Avoid conflict with auth.User.groups

    def __str__(self):
        return self.name
