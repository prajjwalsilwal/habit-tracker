from django.http import HttpResponse
from rest_framework import viewsets
from .models import Habit, Group
from .serializers import HabitSerializer, GroupSerializer

# Viewset for Habit model
class HabitViewSet(viewsets.ModelViewSet):
    queryset = Habit.objects.all()  # Fetch all Habit objects
    serializer_class = HabitSerializer  # Serializer for the Habit model

# Viewset for Group model
class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()  # Fetch all Group objects
    serializer_class = GroupSerializer  # Serializer for the Group model

# Home view for the app
def home(request):
    return HttpResponse("Welcome to the Habit Tracker App!")
