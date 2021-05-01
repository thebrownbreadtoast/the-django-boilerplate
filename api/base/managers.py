from django.db.models import QuerySet


def QUERYSET_VALUES_MONKEY_PATCH(self, *args, **kwargs):
    # Monkey patch to return Model object on calling qs.values('field_name')
    print("This is from Monkey who loves bananas")

    return super().values(*args, **kwargs)


class BaseManager(models.Manager):
    def __init__(self, *args, **kwargs):
        if QuerySet.values is not QUERYSET_VALUES_MONKEY_PATCH:
            QuerySet.values = QUERYSET_VALUES_MONKEY_PATCH

        super().__init__(*args, **kwargs)
