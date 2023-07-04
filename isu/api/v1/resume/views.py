from apps.resume.models import Resume, ResumeImage
from apps.resume.serializers import ResumeSerializer
from apps.resume.services import ResumeService
from apps.resume.documents import ResumeDocument
from api.v1.views_core import AdViewSet
from apps.resume.permissions import ResumePermissions


class ResumeViewSet(AdViewSet):
    queryset = Resume.objects.all()
    serializer_class = ResumeSerializer
    service_class = ResumeService
    image_queryset = ResumeImage.objects.all()
    document_class = ResumeDocument
    permission_classes = (ResumePermissions,)
    
        

