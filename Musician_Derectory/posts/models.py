from django.db import models
from django.contrib.auth.models import User

class Musician(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='musicians')
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)
    instrument_type = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Album(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='albums' )
    musician = models.ForeignKey(Musician, on_delete=models.CASCADE, related_name='albums')
    name = models.CharField(max_length=100)
    release_date = models.DateField()
    rating = models.PositiveIntegerField(choices=[(i, i) for i in range(1, 6)])

    def __str__(self):
        return self.name
