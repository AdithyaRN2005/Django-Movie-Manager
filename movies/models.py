from django.db import models
from django.contrib.auth.models import User

class Genre(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50, unique=True)
    
    def __str__(self):
        return self.title
    
class Movie(models.Model):
    title = models.CharField(max_length=50)
    director = models.CharField(max_length=50) 
    release_date = models.DateField()
    genre = models.ManyToManyField(Genre, related_name='movies')
    description = models.TextField()
    poster = models.ImageField(upload_to='movie_posters/', null=True, blank=True)
    slug = models.SlugField(max_length=50,unique=True)
    
    
    class Meta:
        ordering = ('-release_date',)

    def __str__(self):
        return self.title    