from django import forms

from . models import Destino, Ciudad

class CiudadForm(forms.ModelForm):
    name = forms.CharField(label='Nombre',max_length=200, widget=forms.TextInput(
        attrs={
            'class':'form-control'
        }
    ))
    summary = forms.CharField(label='Descripción', max_length=1000, widget=forms.Textarea(
        attrs={
            'class':'form-control'
        }
    ))
    class Meta:
        model = Ciudad
        fields = ('name', 'summary',)

class DestinoForm(forms.ModelForm):
    title = forms.CharField(label='Nombre',max_length=200, widget=forms.TextInput(
        attrs={
            'class':'form-control'
        }
    ))
    summary = forms.CharField(label='Descripción', max_length=1000, widget=forms.Textarea(
        attrs={
            'class':'form-control'
        }
    ))
    url = forms.URLField(label='URL', max_length=100,widget=forms.URLInput(
        attrs={
            'class':'form-control'
        }
    ))
    ciudad = forms.ModelChoiceField(queryset=Genre.objects.all(), label='Género',
            widget=forms.Select(
            attrs={
                'class':'form-control' 
            }
            ))
    image = forms.ImageField(label='Imagen',
            widget=forms.ClearableFileInput(
            attrs={
                'class':'form-control' 
            }
            ))

             
    class Meta:
        model = Destino
        fields = ('title','ciudad','summary', 'url', 'image',)