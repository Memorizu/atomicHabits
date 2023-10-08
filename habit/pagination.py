from rest_framework.pagination import PageNumberPagination


class HabitPaginator(PageNumberPagination):
    """
    Custom pagination class for paginating Habit objects.

    Attributes:
    - page_size: The number of items to include on each page.
    - page_size_query_param: The query parameter key to specify the page size dynamically in the request.
    - max_page_size: The maximum page size allowed.

    Methods:
    - get_page_size(self, request): Returns the actual page size based on the request.
    """
    page_size = 5
    page_size_query_param = 'page_size'
    max_page_size = 100
