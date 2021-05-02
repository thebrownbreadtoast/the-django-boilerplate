from rest_framework.pagination import PageNumberPagination
from rest_framework.settings import DEFAULTS, api_settings

DEFAULTS["MAX_PAGE_SIZE"] = None

api_settings.reload()  # noqa


class BasePaginator(PageNumberPagination):
    """Base Paginator class to be inherited by other Paginator classes."""

    page_size_query_param = "page_size"

    max_page_size = api_settings.MAX_PAGE_SIZE
