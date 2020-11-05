from django.test import TestCase
from django.urls import reverse
from django.core.files.uploadedfile import SimpleUploadedFile

from destino.models import Ciudad, Destino

class CiudadListViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Create 13 authors for pagination tests
        number_of_ciudad = 13

        for ciudad_id in range(number_of_ciudad):
            Ciudad.objects.create(
                name=f'Accion {ciudad_id}',
            )
           
    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/destino/ciudad/')
        self.assertEqual(response.status_code, 200)
           
    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('ciudads'))
        self.assertEqual(response.status_code, 200)
        
    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('ciudads'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'destino/ciudad_list.html')
        
    def test_pagination_is_ten(self):
        response = self.client.get(reverse('ciudads'))
        self.assertEqual(response.status_code, 200)
        self.assertTrue('is_paginated' in response.context)
        self.assertTrue(response.context['is_paginated'] == True)
        self.assertTrue(len(response.context['ciudad_list']) == 10)

    def test_lists_all_ciudads(self):
        # Get second page and confirm it has (exactly) remaining 3 items
        response = self.client.get(reverse('ciudads')+'?page=2')
        self.assertEqual(response.status_code, 200)
        self.assertTrue('is_paginated' in response.context)
        self.assertTrue(response.context['is_paginated'] == True)
        self.assertTrue(len(response.context['ciudad_list']) == 3)

class DestinoListViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Create 13 authors for pagination tests
        number_of_destino = 13
        c =Ciudad.objects.create(name='Accion')
        with open('destino/static/img/logo.png', 'rb') as file:
            document = SimpleUploadedFile(file.name, file.read(), content_type='image/png')

        for destino_id in range(number_of_destino):
            test_destino = Destino.objects.create(
                title=f'Rey Leon {destino_id}',
                ciudad= c,
                url=f'Prueba.com {destino_id}',
                image= document
            )
            
            test_destino.save()

           
    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/destino/destinos/')
        self.assertEqual(response.status_code, 200)
           
    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('destinos'))
        self.assertEqual(response.status_code, 200)
        
    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('destinos'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'base_generic.html', 'index.html')
        
    """def test_pagination_is_ten(self):
        response = self.client.get(reverse('movies'))
        self.assertEqual(response.status_code, 200)
        self.assertTrue('is_paginated' in response.context)
        self.assertTrue(response.context['is_paginated'] == True)
        self.assertTrue(len(response.context['movie_list']) == 10)

    def test_lists_all_movies(self):
        # Get second page and confirm it has (exactly) remaining 3 items
        response = self.client.get(reverse('movies')+'?page=2')
        self.assertEqual(response.status_code, 200)
        self.assertTrue('is_paginated' in response.context)
        self.assertTrue(response.context['is_paginated'] == True)
        self.assertTrue(len(response.context['movie_list']) == 3)

        """