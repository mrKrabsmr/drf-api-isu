from apps.jobs.models import Job, JobImage
from apps.jobs.serializers import JobSerializer
from apps.jobs.services import JobService
from apps.jobs.documents import JobDocument
from api.v1.views_core import AdViewSet
from apps.jobs.permissions import JobPermissions


class JobViewSet(AdViewSet):
    queryset = Job.object.all()
    serializer_class = JobSerializer
    service_class = JobService
    image_queryset = JobImage.objects.all()
    document_class = JobDocument
    permission_classes = (JobPermissions,)