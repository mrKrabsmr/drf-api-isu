from django_elasticsearch_dsl import Index, Document, fields
from apps.elastic_core import settings, search_analyzer
from apps.jobs.models import Job


JobIndex = Index("jobs")
JobIndex.settings(
    **settings
)

@JobIndex.doc_type
class JobDocument(Document):
    body = fields.TextField(
        analyzer=search_analyzer
    )

    class Django:
        model = Job
        fields = ("id",)