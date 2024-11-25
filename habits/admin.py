from django.contrib import admin
from .models import Habit, Group

# Register Habit model
@admin.register(Habit)
class HabitAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at')  # Fields displayed in the admin panel
    search_fields = ('name',)  # Add a search bar for habits

# Register Group model
@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at')  # Fields displayed in the admin panel
    search_fields = ('name',)  # Add a search bar for groups
