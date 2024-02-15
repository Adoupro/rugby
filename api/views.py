from django.shortcuts import render
import json
import sqlite3

from app.models import ODS_Licence, ODS_Club
from app.models import D_Geography, D_Age_Group, D_Federation, D_Club_Type, D_Sexe, D_Date
from app.models import F_Licence, F_Club
from api.serializers import ODS_Licence_Serializer
from api.serializers import D_Date_Serializer, D_Federation_Serializer, D_Geography_Serializer
from api.serializers import F_Licence_Serializer, F_Club_Serializer

from rugby.settings import DATABASES

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

# Create your views here.

class API_Operational_Data_Store(APIView):
    """ Voici l\'API de ma base de donnée

        Méthode GET :
        Méthode POST :
        Méthode PUT :
        Méthode PATCH :
        Méthode DELETE :
    """
    def get(self, request, pk=None):
        
        if 'table_name' in request.GET:
            table_name = request.GET['table_name']
            data = eval(table_name).objects.all()
            count = data.count()
        else:
            data = ODS_Licence.objects.all()
            count = data.count()
            data = data[:30]
        
        serializer = ODS_Licence_Serializer(data=data, many=True)
        serializer.is_valid()
        
        data = serializer.data
        
        result = {
            'count': count,
            'data': data,
        }

        
        return Response(data=result, status=status.HTTP_200_OK)


    
class API_Datawarehouse(APIView):
    """ Voici l\'API de ma base de donnée

        Méthode GET :
        Méthode POST :
        Méthode PUT :
        Méthode PATCH :
        Méthode DELETE :
    """
    def get(self, request, pk=None):
        
        if 'table_name' in request.GET:
            table_name = request.GET['table_name']
            data = eval(table_name).objects.all()
            count = data.count()
            #data = data[:1000]
        else:
            data = F_Club.objects.all()
            count = data.count()
            data = F_Club[:1000]
        
        serializer = eval(f"{table_name}_Serializer")(data=data, many=True)
        serializer.is_valid()
        
        data = serializer.data
        
        result = {
            'table_name': table_name,
            'count': count,
            'data': data,
        }
        
        return Response(data=result, status=status.HTTP_200_OK)
    
    def post(self, request):
        result = {
            'message':'Voici les résultats trouvés',
            'data':[]
        }
        
        return Response(result, status=status.HTTP_200_OK)

    def put(self, request, pk=None):
        result = {
            'message':'Voici les résultats trouvés',
            'data':[]
        }
        
        return Response(result, status=status.HTTP_200_OK)
    
    def patch(self, request, pk=None):
        result = {
            'message':'Voici les résultats trouvés',
            'data':[]
        }
        
        return Response(result, status=status.HTTP_200_OK)
    
    def delete(self, request, pk=None):
        
        rows = ODS_Licence.objects.all()
        count = rows.count()
        rows.delete()
        
        rows = D_Geography.objects.all()
        count = rows.count()
        rows.delete()
        
        rows = D_Age_Group.objects.all()
        count = rows.count()
        rows.delete()
        
        rows = D_Federation.objects.all()
        count = rows.count()
        rows.delete()
        
        rows = D_Club_Type.objects.all()
        count = rows.count()
        rows.delete()
        
        rows = D_Sexe.objects.all()
        count = rows.count()
        rows.delete()
        
        rows = D_Date.objects.all()
        count = rows.count()
        rows.delete()
        
        rows = F_Licence.objects.all()
        count = rows.count()
        rows.delete()
        
        conn = sqlite3.connect(DATABASES['default']['NAME'])
        conn.execute("VACUUM")
        conn.close()
        
        result = {
            'message': f"{count} lignes ont été supprimées",
            'data': []
        }
     
        return Response(result, status=status.HTTP_200_OK)
