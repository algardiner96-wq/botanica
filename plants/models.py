from django.db import models

# Create your models here.
class Plant(models.Model):
    name = models.CharField(max_length=100)
    scientific_name = models.CharField(max_length=100, blank=True, null=True)
    plant_type = models.CharField(max_length=50)
    watering = models.CharField(max_length=50)
    sunlight = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    icon = models.ImageField(upload_to='plant_icons/', blank=True, null=True)
    image = models.ImageField(upload_to='plant_images/', blank=True, null=True)
    symbolism = models.ManyToManyField('Symbolism', blank=True)

    def __str__(self):
        return self.name
    
    