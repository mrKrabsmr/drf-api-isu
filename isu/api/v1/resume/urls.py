from api.v1.resume.views import ResumeViewSet
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r"", ResumeViewSet)

urlpatterns = []

urlpatterns += router.urls