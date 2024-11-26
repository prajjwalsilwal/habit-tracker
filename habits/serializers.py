from rest_framework import serializers
from .models import Habit, Group

# Serializer for Habit model
class HabitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Habit
        fields = '__all__'  # This will serialize all fields in the Habit model

# Serializer for Group model
class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = '__all__'  # This will serialize all fields in the Group model
