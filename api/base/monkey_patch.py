from django.db.models.query import QuerySet, ValuesIterable


def patched_values(self, *fields, **expressions):
    # Monkey patched .values method on QuerySet to toggle usage of
    # ValuesIterable depending upon `is_dict` expressions.
    # Reference:
    # 	- https://github.com/django/django/blob/stable/3.2.x/django/db/models/query.py#L838
    is_dict = expressions.get("is_dict", True)

    fields += tuple(expressions)

    clone = self._values(*fields, **expressions)

    if is_dict:
        clone._iterable_class = ValuesIterable

    return clone


# Disabling this monkey patch, as same can be achieved with .only
# QuerySet.values = patched_values
