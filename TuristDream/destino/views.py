from django.shortcuts import render
from . models import Destino, Ciudad
from django.views import generic

# Create your views here.

def index(request):
    num_destino=Destino.objects.all()
    
    return render(
        request,
        'index.html',
        context={'num_destino':num_destino},
    )
# Create your views here. 

def about(request):
    
    
    return render(
        request,
        'about.html',
        
    )

def contact(request):
    
    return render(
        request,
        'contact.html',
    )



