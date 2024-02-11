from django.shortcuts import render
from app.models import Player

# Create your views here.
def index(request):
    
    players = Player.objects.all()
    #Player.objects.get_or_create()
    
    context = {'ball': 'blablabla', 'players':players}

    
    return render(request, 'index.html', context)
