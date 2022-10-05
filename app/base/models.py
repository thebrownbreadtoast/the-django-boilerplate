import uuid

from django.db import models

from app.base.managers import BaseManager as CustomBaseManager


class BaseModel(models.Model):
    """Abstract base model class to be inherited by other model classes."""

    uuid = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False
    )
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    modified_at = models.DateTimeField(auto_now=True, editable=False)

    objects = CustomBaseManager()

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        explicit_update_fields = kwargs.get("update_fields", [])

        if (
            explicit_update_fields
            and "modified_at" not in explicit_update_fields
        ):
            explicit_update_fields.append("modified_at")  # noqa

        super().save(*args, **kwargs)  # noqa
