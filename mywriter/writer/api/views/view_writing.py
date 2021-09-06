from rest_framework import viewsets
from writer.models import Writing
from writer.api.serializers.srl_writing import WritingSerializer


class WritingViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows writings to be viewed or edited.
    """
    queryset = Writing.objects.all()
    serializer_class = WritingSerializer