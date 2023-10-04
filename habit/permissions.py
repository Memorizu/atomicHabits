from rest_framework.permissions import BasePermission

from habit.models import Habit


class IsOwner(BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.user == request.user


class IsPublic(BasePermission):
    def has_permission(self, request, view):
        return Habit.objects.filter(is_public=True).exists()
