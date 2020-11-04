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


from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.views import generic



class DestinoCreate(CreateView):
    model = Destino
    fields = '__all__'

class DestinoUpdate(UpdateView):
    model = Destino
    fields = '__all__'

class DestinoDelete(DeleteView):
    model = Destino
    sucess_url = reverse_lazy('Destino')


class DestinoDetailView(generic.DetailView):
    model=Destino
