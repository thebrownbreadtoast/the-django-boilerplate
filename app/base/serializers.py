from rest_framework import serializers


class BaseModelSerializer(serializers.ModelSerializer):
    """Base Serializer class to be inherited by other Serializer classes."""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)  # noqa


class BaseReadOnlySerializer(serializers.Serializer):
    """Base Read-Only Serializer class to be inherited by other Read-Only Serializer classes."""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)  # noqa
