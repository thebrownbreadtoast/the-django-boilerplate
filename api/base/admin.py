from django.contrib import admin


class BaseAdmin(admin.Admin):
    """Base Admin class to be inherited by other admin classes."""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)  # noqa
