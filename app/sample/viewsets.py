from app.base.viewsets import BaseViewSet
from app.sample.models import SampleModel
from app.sample.paginators import SamplePaginator
from app.sample.serializers import SampleReadOnlySerializer


class SampleViewSet(BaseViewSet):
    queryset = SampleModel.objects.all()
    serializer_class = SampleReadOnlySerializer
    pagination_class = SamplePaginator
