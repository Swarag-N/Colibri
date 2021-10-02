from rest_framework.serializers import ModelSerializer
from colibri.models import Colibri

class ColibriSerializer(ModelSerializer):
    class Meta:
        model = Colibri
        fields = "__all__"

class ColibriAdvancedSerializer(ModelSerializer):
    class Meta:
        model = Colibri
        fields = "__all__"
    
    