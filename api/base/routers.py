from rest_framework import routers


class BaseRouter(routers.SimpleRouter):
    """Base Router class to be inherited by all Router classes."""

    def extend(self, extended_router=None):
        if extended_router:
            self.registry.extend(extended_router.registry)  # noqa
