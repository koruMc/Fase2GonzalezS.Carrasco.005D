from django.test import TestCase
from destino.forms import CiudadForm, DestinoForm
from destino.models import Ciudad, Destino
from django.core.files.uploadedfile import SimpleUploadedFile

class CiudadFormsTest(TestCase):
    def test_valid_form(self):
        c = Ciudad.objects.create(name='Prueba1')
        form = GenreForm(data=data)
        self.assertTrue(form.is_valid())

    def test_invalid_form(self):
        c = Ciudad.objects.create(name='',)
        form = GenreForm(data=data)
        self.assertFalse(form.is_valid())

class DestinoFormsTest(TestCase):
    def test_valid_form(self):
        ciudad = Ciudad.objects.create(name='1')
        ciudad = Ciudad.objects.get(pk=1).pk
        d = Destino.objects.create(name='Prueba1', url='https://www.youtube.com/embed/rslZ-fHiSuI')
        d.save()
        data = {'name': d.name, 'ciudad': ciudad, 'url' : d.url, }
        
        with open('destino/static/img/logo.png', 'rb') as file:
            document = SimpleUploadedFile(file.name, file.read(), content_type='image/png')
        
        form = DestinoForm(data, {'image': document})
        print(form.errors)
        self.assertTrue(form.is_valid())

    def test_invalid_form(self):
        c = Ciudad.objects.create(name='Accion')
        d = Destino.objects.create(name='', ciudad=c, url='https://www.youtube.com/embed/rslZ-fHiSuI')
        data = {'name': d.name 'ciudad': d.ciudad, 'url' : d.url, }
        form = DestinoForm(data=data)
        self.assertFalse(form.is_valid())