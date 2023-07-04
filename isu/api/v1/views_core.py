from django.http import QueryDict
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status
from apps.filters_core import StandardSearch

from apps.permissions_core import IsAuthorOrReadOnly
from apps.pagination_core import StandardPagination

class AdViewSet(ModelViewSet):
    queryset = None
    serializer_class = None
    service_class = None
    pagination_class = StandardPagination
    permission_classes = ()
    filter_backends = (StandardSearch,)
    image_queryset = None
    document_class = None
    

    def create(self, request, *args, **kwargs):
        if isinstance(request.data, QueryDict):
            request.data._mutable = True
        request.data["user"] = request.user
        serializer = self.get_serializer(request.data)
        serializer.is_valid(raise_exception=True)
        self.service_class.create(serializer.data, self)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
