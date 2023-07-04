from apps.permissions_core import IsAuthorOrReadOnly
from rest_framework.permissions import SAFE_METHODS

class WorkPermissions(IsAuthorOrReadOnly):
    pass