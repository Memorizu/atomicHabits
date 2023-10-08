from rest_framework.permissions import BasePermission


class IsOwner(BasePermission):
    """
    Custom permission class to allow access only to the owner of an object.

    Attributes:
    - message: A descriptive message to be displayed when permission is denied.

    Methods:
    - has_object_permission(self, request, view, obj): Determines whether the user has permission to access the object.
    """
    def has_object_permission(self, request, view, obj):
        """
        Checks if the requesting user is the owner of the object.

        Args:
        - request: The HTTP request object.
        - view: The view that defines the object permission check.
        - obj: The object being accessed.

        Returns:
        True if the requesting user is the owner of the object, False otherwise.
        """
        return request.user == obj.owner
