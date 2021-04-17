from django.db import models


class BaseModel(models.Model):
	"""Abstract base model class to be inherited by other model classes."""

    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    modified_at = models.DateTimeField(auto_now=True, editable=False)

	def __init__(self, *args, **kwargs):
		super(BaseModel, self).__init__(*args, **kwargs)  # noqa

	def save(self, *args, **kwargs):
		explicit_update_fields = kwargs.get('update_fields', [])

		if explicit_update_fields and 'modified_at' not in explicit_update_fields:
			explicit_update_fields.append('modified_at')  # noqa

		super(BaseModel, self).save(*args, **kwargs)  # noqa
