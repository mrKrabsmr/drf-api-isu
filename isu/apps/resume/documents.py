from django_elasticsearch_dsl import Index, Document, fields
from apps.elastic_core import search_analyzer, settings
from apps.resume.models import Resume


ResumeIndex = Index("resume")
ResumeIndex.settings(
    **settings
)

@ResumeIndex.doc_type
class ResumeDocument(Document):
    body = fields.TextField(
        analyzer=search_analyzer
    )

    class Django:
        model = Resume
        fields = ("id",)