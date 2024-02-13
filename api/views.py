from django.shortcuts import render
from app.models import Player
from app.models import ODS_Player
from api.serializers import ODS_Player_Serializer
import json

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

# Create your views here.
class API_Datawarehouse(APIView):
    """ Voici l\'API de ma base de donnée

        Méthode GET :
        Méthode POST :
        Méthode PUT :
        Méthode PATCH :
        Méthode DELETE :
    """
    def get(self, request, pk=None):
        
        if 'code_commune' in request.GET:
            code_commune = request.GET['code_commune']
            data = ODS_Player.objects.filter(code_commune=code_commune)
            count = data.count()
        else:
            data = ODS_Player.objects.all()
            count = data.count()
            data = data[:30]
        
        serializer = ODS_Player_Serializer(data=data, many=True)
        serializer.is_valid()
        
        data = serializer.data
        
        result = {
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
        
        players = Player.objects.all()
        count = players.count()
        players.delete()
        
        result = {
            'message': f"{count} lignes ont été supprimées",
            'data': []
        }
        
        return Response(result, status=status.HTTP_200_OK)
