from api.base.routers import BaseRouter
from api.sample.viewsets import SampleViewSet

sample_router = BaseRouter()

sample_router.register("sample", SampleViewSet, basename="sample-route")
