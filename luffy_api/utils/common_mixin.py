from rest_framework.mixins import (
    CreateModelMixin,
    ListModelMixin,
    UpdateModelMixin,
    DestroyModelMixin,
    RetrieveModelMixin,
)
from utils.common_response import APIResponse


class APIListModelMixin(ListModelMixin):
    def list(self, request, *args, **kwargs):
        res = super().list(request, *args, **kwargs)
        return APIResponse(results=res.data)
