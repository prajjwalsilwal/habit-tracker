# habits/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views  # Import views from the current app
from .views import HabitViewSet, GroupViewSet

# Set up the default router
router = DefaultRouter()
router.register(r'habits', HabitViewSet)
router.register(r'groups', GroupViewSet)

# Include router URLs into the app's URL configuration
urlpatterns = [
    path('', views.home, name='home'),  # Maps the root URL to the 'home' view
    path('api/', include(router.urls)),  # Include the API endpoints defined by the router
]
