from django.db import models

class Titles(models.Model):
    type = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    director = models.CharField(max_length=200)
    cast = models.CharField(max_length=200)
    country = models.CharField(max_length=200)
    date_added = models.CharField(max_length=200)
    release_year = models.IntegerField()
    rating = models.CharField(max_length=200)
    duration = models.CharField(max_length=200)
    listed_in = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    
    def __str__(self):
        return self.title           
