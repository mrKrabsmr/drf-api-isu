from apps.permissions_core import IsAuthorOrReadOnly
from rest_framework.permissions import SAFE_METHODS

class ResumePermissions(IsAuthorOrReadOnly):
    def has_permission(self, request, view):
        return bool(
            request.method in SAFE_METHODS or
            request.user and
            request.user.is_authenticated and
            not request.user.is_company
        )