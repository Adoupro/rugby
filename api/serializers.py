from rest_framework import serializers
from app.models import ODS_Player

class ODS_Player_Serializer(serializers.ModelSerializer):
    class Meta:
        model = ODS_Player
        fields = '__all__'