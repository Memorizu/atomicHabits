from rest_framework import viewsets, generics
from rest_framework.permissions import IsAuthenticated


from habit.models import Habit
from habit.pagination import HabitPaginator
from habit.permissions import IsOwner
from habit.serializer import HabitSerializer


# Create your views here.
class HabitViewSet(viewsets.ModelViewSet):
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
    pagination_class = HabitPaginator

    def get_permissions(self):
        match self.action:
            case 'update', 'partial_update', 'destroy':
                return [IsAuthenticated(), IsOwner()]
            case _:
                return [IsAuthenticated()]


class PublicHabitListAPIView(generics.ListAPIView):
    queryset = Habit.objects.filter(is_public=True)
    permission_classes = [IsAuthenticated]
    serializer_class = HabitSerializer
