from rest_framework import routers

from api.v1.jobs.views import JobViewSet

router = routers.SimpleRouter()
router.register(r"", JobViewSet.as_view())

urlpatterns = [] 

urlpatterns += router.urls