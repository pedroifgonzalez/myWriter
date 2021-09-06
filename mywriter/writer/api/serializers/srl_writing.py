from rest_framework import serializers
from writer.models import Writing

class WritingSerializer(serializers.ModelSerializer):

    class Meta:
        model = Writing
        fields = '__all__' 
        read_only_fields = ('creation_date', 'modification_date')