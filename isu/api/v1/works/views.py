from api.v1.views_core import AdViewSet
from apps.works.documents import WorkDocument
from apps.works.models import Work, WorkImage
from apps.works.serializers import WorkSerializer
from apps.works.services import WorkService
from apps.works.permissions import WorkPermissions


class WorkViewSet(AdViewSet):
    queryset = Work.objects.all()
    serializer_class = WorkSerializer
    service_class = WorkService
    image_queryset = WorkImage.objects.all()
    document_class = WorkDocument
    permission_classes = (WorkPermissions,)
