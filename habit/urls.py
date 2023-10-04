from django.urls import path
from rest_framework.routers import DefaultRouter

from habit.apps import HabitConfig
from habit.views import HabitViewSet, PublicHabitListAPIView

app_name = HabitConfig.name
router = DefaultRouter()
router.register(r'', HabitViewSet, basename='habit')


urlpatterns = [
    path('public', PublicHabitListAPIView.as_view(), name='public')
] + router.urls
