from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class post(models.Model):
    id = models.IntegerField(primary_key = True, auto_created = True)
    titulo = models.CharField(max_length = 200)
    texto = models.TextField()
    fecha = models.DateTimeField(default = timezone.now)
    
    def __str__(self):
        return self.titulo
        
class Category(models.Model):
    id = models.IntegerField(primary_key = True, auto_created = True)
    nombre = models.CharField(max_length = 200)
    
    def __str__(self):
        return self.nombre
        
class Hashtag(models.Model):
    id = models.IntegerField(primary_key = True, auto_created = True)
    nombre = models.CharField(max_length=200)
    
    def __str__(self):
        return self.nombre
        
class Entry(models.Model):
    id = models.IntegerField(primary_key = True, auto_created = True)
    titulo = models.CharField(max_length = 200)
    texto = models.TextField()
    fecha = models.DateTimeField(default = timezone.now)
    
    #relaciones con los modelos 
    autor = models.ForeignKey(User, on_delete = models.CASCADE)
    categoria = models.ForeignKey(Category, on_delete = models.CASCADE)
    etiquetas = models.ManyToManyField(Hashtag)
    
    def __str__(self):
        return self.titulo