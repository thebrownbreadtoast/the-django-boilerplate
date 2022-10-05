from app.base.routers import BaseRouter
from app.sample.viewsets import SampleViewSet

sample_router = BaseRouter()

sample_router.register("sample", SampleViewSet, basename="sample-route")
