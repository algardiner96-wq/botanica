from django.db import models

# Create your models here.
class Plant(models.Model):
    LIFESPAN_CHOICES = [
        ('Annual', 'Annual'),
        ('Perennial', 'Perennial'),
        ('Biennial', 'Biennial'),
    ]
    
    name = models.CharField(max_length=100)
    scientific_name = models.CharField(max_length=100, blank=True, null=True)
    plant_type = models.CharField(max_length=50)
    lifespan = models.CharField(max_length=20, choices=LIFESPAN_CHOICES, blank=True)
    watering = models.CharField(max_length=50)
    sunlight = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    icon = models.ImageField(upload_to='plant_icons/', blank=True, null=True)
    image = models.ImageField(upload_to='plant_images/', blank=True, null=True)
    symbolism = models.ManyToManyField('Symbolism', blank=True)

    def __str__(self):
        return self.name
    
class Symbolism(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name
    

class Variant(models.Model):
    plant = models.ForeignKey(Plant, on_delete=models.CASCADE, related_name='variants')
    name = models.CharField(max_length=100)
    colour = models.CharField(max_length=50, blank=True)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='variant_images/', blank=True, null=True)

    def __str__(self):
        return f"{self.plant.name} - {self.name}"
    
