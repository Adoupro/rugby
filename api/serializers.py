from rest_framework import serializers
from app.models import ODS_Licence
from app.models import D_Date, D_Federation, D_Geography, D_Age_Group, D_Club_Type, D_Sexe
from app.models import F_Licence, F_Club

class ODS_Licence_Serializer(serializers.ModelSerializer):
    class Meta:
        model = ODS_Licence
        fields = '__all__'
        
class D_Date_Serializer(serializers.ModelSerializer):
    class Meta:
        model = D_Date
        fields = '__all__'
        
class D_Federation_Serializer(serializers.ModelSerializer):
    class Meta:
        model = D_Federation
        fields = '__all__'
        
class D_Geography_Serializer(serializers.ModelSerializer):
    class Meta:
        model = D_Geography
        fields = '__all__'
        
class F_Licence_Serializer(serializers.ModelSerializer):
    class Meta:
        model = F_Licence
        fields = '__all__'
        
class F_Club_Serializer(serializers.ModelSerializer):
    class Meta:
        model = F_Club
        fields = '__all__'