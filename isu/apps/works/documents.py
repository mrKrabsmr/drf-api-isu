from django_elasticsearch_dsl import Index, Document, fields
from apps.elastic_core import settings, search_analyzer
from apps.works.models import Work

WorkIndex = Index("works")
WorkIndex.settings(
    **settings
)

@WorkIndex.doc_type
class WorkDocument(Document):
    body = fields.TextField(
        analyzer=search_analyzer
    )

    class Django:
        model = Work
        fields = ("id",)