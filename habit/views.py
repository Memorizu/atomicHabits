from rest_framework import viewsets, generics
from rest_framework.permissions import IsAuthenticated

from habit.models import Habit
from habit.pagination import HabitPaginator
from habit.permissions import IsOwner

from habit.serializer import HabitSerializer


class HabitViewSet(viewsets.ModelViewSet):
    """
    API view for performing CRUD operations for the Habit model.

    Allows creating, viewing, updating, and deleting habits belonging to the current user.

    Parameters:
    - serializer_class: The serializer class for converting Habit model data to and from JSON.
    - pagination_class: The class for configuring pagination of query results.
    - permission_classes: A list of permission classes required to access this view.

    Methods:
    - get_queryset(): Returns a query set containing only the habits belonging to the current user.
    """
    serializer_class = HabitSerializer
    pagination_class = HabitPaginator
    permission_classes = [IsAuthenticated, IsOwner]

    def get_queryset(self):
        return Habit.objects.filter(owner=self.request.user)


class PublicHabitListAPIView(generics.ListAPIView):
    queryset = Habit.objects.filter(is_public=True)
    permission_classes = [IsAuthenticated]
    serializer_class = HabitSerializer
    pagination_class = HabitPaginator
