from django import forms

from . models import Ciudad, Destino

class CiudadForm(forms.ModelForm):
    name = forms.CharField(label='Nombre',max_length=200, widget=forms.TextInput(
        attrs={
            'class':'form-control'
        }
    ))
    """summary = forms.CharField(label='Descripción', max_length=1000, widget=forms.Textarea(
        attrs={
            'class':'form-control'
        }
    ))"""
    class Meta:
        model = Ciudad
        fields = ('name',)

class DestinoForm(forms.ModelForm):
    name = forms.CharField(label='Nombre',max_length=200, widget=forms.TextInput(
        attrs={
            'class':'form-control'
        }
    ))
    """summary = forms.CharField(label='Descripción', max_length=1000, widget=forms.Textarea(
        attrs={
            'class':'form-control'
        }
    ))"""
    url = forms.URLField(label='URL', max_length=100,widget=forms.URLInput(
        attrs={
            'class':'form-control'
        }
    ))
    ciudad = forms.ModelChoiceField(queryset=Ciudad.objects.all(), label='Ciudad',
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
        fields = ('name','url','ciudad', 'image',)