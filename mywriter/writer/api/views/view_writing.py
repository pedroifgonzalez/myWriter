from rest_framework import viewsets
from writer.models import Writing
from writer.api.serializers import WritingSerializer


class WritingViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows writings to be viewed or edited.
    """
    queryset = Writing.objects.all()
    serializer_class = WritingSerializer