from django.shortcuts import render

# Create your views here.
def index(request):
    
    context = {'ball': 'blablabla'}
    
    
    return render(request, 'index.html', context)
