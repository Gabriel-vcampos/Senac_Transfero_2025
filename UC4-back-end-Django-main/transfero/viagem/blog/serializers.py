from blog.models import Topico
from rest_framework import serializers

class TopicoSerializer(serializers.ModelSerializer):


    class Meta:
        model = Topico
        fields = '__all__'