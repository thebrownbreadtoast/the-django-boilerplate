from django.db import models


class BaseManager(models.Manager):
    """Base Manager class to be used with BaseModel class."""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)  # noqa
