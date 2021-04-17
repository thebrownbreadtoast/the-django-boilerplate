from django.contrib import admin


class BaseAdmin(admin.Admin):
	"""Base admin classes to be inherited by other admin classes."""

	def __init__(self, *args, **kwargs):
		super(BaseAdmin, self).__init__(*args, **kwargs)  # noqa
