from django.test import TestCase
from peliculas.models import Ciudad, Destino

class CiudadModelTest(TestCase):

    @classmethod

    def setUpTestData(cls):
        Ciudad.objects.create(name='Accion')
    
    def test_name_label(self):
        ciudad=Ciudad.objects.get(id=1)
        field_label = ciudad._meta.get_field('name').verbose_name
        self.assertEquals(field_label,'name')
    
    def test_name_max_length(self):
        ciudad=Ciudad.objects.get(id=1)
        max_length = ciudad._meta.get_field('name').max_length
        self.assertEquals(max_length,100)
    
    
    def test_get_absolute_url(self):
        ciudad=Ciudad.objects.get(id=1)
        self.assertEquals(ciudad.get_absolute_url(), '/destino/ciudad/1')

class DestinoModelTest(TestCase):

    @classmethod

    def setUpTestData(cls):
        c = Ciudad.objects.create(name='Accion')
        test_destino = Destino.objects.create(id= '44fc2b9d-2b04-45cb-af8a-c4601527b156', name='Reloj Viña', ciudad=c, url='https://www.youtube.com/embed/rslZ-fHiSuI')
    
    def test_name_label(self):
        destino= Destino.objects.get(id= '44fc2b9d-2b04-45cb-af8a-c4601527b156')
        field_label = destino._meta.get_field('name').verbose_name
        self.assertEquals(field_label,'name')

    
    def test_ciudad_label(self):
        destino=Destino.objects.get(id='44fc2b9d-2b04-45cb-af8a-c4601527b156')
        field_label = Destino._meta.get_field('ciudad').verbose_name
        self.assertEquals(field_label,'ciudad')
    
    def test_name_max_length(self):
        destino=Destino.objects.get(id='44fc2b9d-2b04-45cb-af8a-c4601527b156')
        max_length = destino._meta.get_field('name').max_length
        self.assertEquals(max_length,200)
    
    
    def test_get_absolute_url(self):
        destino=Destino.objects.get(id='44fc2b9d-2b04-45cb-af8a-c4601527b156')
        self.assertEquals(destino.get_absolute_url(), '/destino/destino/44fc2b9d-2b04-45cb-af8a-c4601527b156')
