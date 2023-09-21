"""
Artist views.
"""

from rest_framework.generics import GenericAPIView
from rest_framework.mixins import (
    ListModelMixin,
    CreateModelMixin,
    RetrieveModelMixin,
    UpdateModelMixin,
    DestroyModelMixin,
)

from .serializers import ArtistSerializer
from .models import Artist


class Artists(ListModelMixin, CreateModelMixin, GenericAPIView):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer

    def get_queryset(self):
        name_filter = self.request.query_params.get("name", None)
        if name_filter is not None:
            return Artist.objects.filter(first_name=name_filter)
        return Artist.objects.all()

    def get(self, request):
        return self.list(request)

    def post(self, request):
        return self.create(request)


class ArtistDetail(
    RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin, GenericAPIView
):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
