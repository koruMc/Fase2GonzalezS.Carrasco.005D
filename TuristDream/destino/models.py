from django.db import models
from django.urls import reverse
import uuid

# Create your models here.

class Ciudad(models.Model):
	"""Model representing an author."""
	name = models.CharField(max_length=100)

	class Meta:
		ordering = ['name']

	def get_absolute_url(self):
		return reverse('ciudad-detail', args=[str(self.id)])

	def __str__(self):
		"""String for representing the Model object."""
		return self.name


class Destino(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    name = models.CharField(max_length=200)
    ciudad = models.ForeignKey('Ciudad', on_delete=models.SET_NULL, null=True, blank=False)
    image = models.ImageField(upload_to='images/', null=True, blank=True)

    

    class Meta:
        ordering=['name']
        
    def __str__(self):
        #return f'{self.id} ({self.title})'
        return self.name
    
    def get_absolute_url(self):
        """Returns the url to access a detail record for this book."""
        return reverse('Destino-detail', args=[str(self.id)])
