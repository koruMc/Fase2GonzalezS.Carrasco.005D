from django.test import TestCase
from django.urls import reverse
from django.core.files.uploadedfile import SimpleUploadedFile

from destino.models import Ciudad, Destino

class GenreListViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Create 13 authors for pagination tests
        number_of_genre = 13

        for genre_id in range(number_of_genre):
            Genre.objects.create(
                name=f'Accion {genre_id}',
                
            )
           
    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/peliculas/genres/')
        self.assertEqual(response.status_code, 200)
           
    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('genres'))
        self.assertEqual(response.status_code, 200)
        
    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('genres'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'peliculas/genre_list.html')
        
    def test_pagination_is_ten(self):
        response = self.client.get(reverse('genres'))
        self.assertEqual(response.status_code, 200)
        self.assertTrue('is_paginated' in response.context)
        self.assertTrue(response.context['is_paginated'] == True)
        self.assertTrue(len(response.context['genre_list']) == 10)

    def test_lists_all_genres(self):
        # Get second page and confirm it has (exactly) remaining 3 items
        response = self.client.get(reverse('genres')+'?page=2')
        self.assertEqual(response.status_code, 200)
        self.assertTrue('is_paginated' in response.context)
        self.assertTrue(response.context['is_paginated'] == True)
        self.assertTrue(len(response.context['genre_list']) == 3)

class MovieListViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Create 13 authors for pagination tests
        number_of_movie = 13
        g =Genre.objects.create(name='Accion', summary='Prueba')
        with open('peliculas/static/img/logo.png', 'rb') as file:
            document = SimpleUploadedFile(file.name, file.read(), content_type='image/png')

        for movie_id in range(number_of_movie):
            test_movie = Movie.objects.create(
                title=f'Rey Leon {movie_id}',
                summary=f'Prueba {movie_id}',
                genre= g,
                url=f'Prueba.com {movie_id}',
                image= document
            )
            
            test_movie.save()

           
    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/peliculas/movies/')
        self.assertEqual(response.status_code, 200)
           
    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('movies'))
        self.assertEqual(response.status_code, 200)
        
    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('movies'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'base_generic.html', 'movies.html')
        
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