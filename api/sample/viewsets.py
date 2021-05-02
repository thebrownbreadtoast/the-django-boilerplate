from api.base.viewsets import BaseViewSet
from api.sample.models import SampleModel
from api.sample.paginators import SamplePaginator
from api.sample.serializers import SampleReadOnlySerializer


class SampleViewSet(BaseViewSet):
    queryset = SampleModel.objects.all()
    serializer_class = SampleReadOnlySerializer
    pagination_class = SamplePaginator
