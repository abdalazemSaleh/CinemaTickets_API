from django.db import models

# Create your models here.


#Guest -- Reservation -- Movie

# Movie Class
class Movie(models.Model):
    hall    = models.CharField(max_length=10)
    movie   = models.CharField(max_length=10)

# Guest
class Guest(models.Model):
    name    = models.CharField(max_length=30)
    mobile  = models.CharField(max_length=10)

#Reservation
class Reservation(models.Model):
    guest = models.ForeignKey(Guest, related_name='reservation', on_delete=models.CASCADE )
    movie = models.ForeignKey(Movie, related_name='reservation', on_delete=models.CASCADE )

