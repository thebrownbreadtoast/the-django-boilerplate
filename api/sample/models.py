from django.db import models

from api.base.models import BaseModel


class SampleModel(BaseModel):
    sample_attr1 = models.CharField(max_length=16, blank=True, null=True)
    sample_attr2 = models.PositiveSmallIntegerField(blank=True, null=True)

    class Meta:
        verbose_name = "Sample Datum"
        verbose_name_plural = "Sample Data"
