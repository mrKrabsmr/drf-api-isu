from rest_framework import routers

from api.v1.works.views import WorkViewSet

router = routers.SimpleRouter()
router.register(r"", WorkViewSet.as_view())

urlpatterns = []

urlpatterns += router.urls