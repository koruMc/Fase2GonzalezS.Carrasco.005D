from django.shortcuts import render, redirect, get_object_or_404
from . models import Destino, Ciudad
from . forms import CiudadForm, DestinoForm



def index(request):
    num_destinos=Destino.objects.all()
    
    return render(
        request,
        'index.html',
        context={'num_destinos':num_destinos},
    )
# Create your views here. 


def contacto(request):
    
    return render(
        request,
        'contact.html',
    )

def about(request):
    
    return render(
        request,
        'about.html',
    )




    
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.views import generic


class CiudadDelete(DeleteView):
    model = Ciudad
    success_url = reverse_lazy('index')


class CiudadDetailView(generic.DetailView):
    model = Ciudad
    
class DestinoDelete(DeleteView):
    model = Destino
    success_url = reverse_lazy('index')
    
class DestinoDetailView(generic.DetailView):
    model = Destino

class CiudadListView(generic.ListView):
    model = Ciudad
    template_name = 'templates/destino/ciudad_list.html'
    queryset = Destino.objects.all()

class DestinoListView(generic.ListView):
    model = Destino
    template_name = 'templates/destino/destino_list.html'
    queryset = Destino.objects.all()    

    paginate_by = 10


def ciudad_new(request):
    if request.method == "POST":
        form = CiudadForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('ciudad-detail', pk=post.pk)
    else:
        form = CiudadForm()
        return render(request, 'destino/ciudad_form.html', {'form': form})

def ciudad_edit(request, pk):
    post = get_object_or_404(Ciudad, pk=pk)
    if request.method == "POST":
        form = CiudadForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('ciudad-detail', pk=post.pk)
    else:
        form = GenreForm(instance=post)
    return render(request, 'destino/ciudad_form.html', {'form': form})

def destino_new(request):
    if request.method == "POST":
        form = DestinoForm(request.POST,request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            #form.save_m2m()
            return redirect('destino-detail', pk=post.pk)
    else:
        form = DestinoForm()
        return render(request, 'destino/destino_form.html', {'form': form})

def destino_edit(request, pk):
    post = get_object_or_404(Destino, pk=pk)
    if request.method == "POST":
        form = DestinoForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            post = form.save()
            post.save()
            return redirect('destino-detail', pk=post.pk)
    else:
        form = DestinoForm(instance=post)
    return render(request, 'destino/destino_form.html', {'form': form})
