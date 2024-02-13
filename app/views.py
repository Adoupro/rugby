from django.shortcuts import render

# Create your views here.
def index(request):

    context = {'data': 'OK'}
    
    return render(request, 'index.html', context)
