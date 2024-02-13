from rest_framework import serializers
from app.models import ODS_Licence

class ODS_Licence_Serializer(serializers.ModelSerializer):
    class Meta:
        model = ODS_Licence
        fields = '__all__'