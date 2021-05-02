from rest_framework import serializers

from api.base.serializers import BaseReadOnlySerializer
from api.sample.models import SampleModel


class SampleReadOnlySerializer(BaseReadOnlySerializer):
    sample_attr1 = serializers.CharField(read_only=True)
    sample_attr2 = serializers.IntegerField(read_only=True)

    class Meta:
        model = SampleModel

        fields = ("sample_attr1", "sample_attr2")
