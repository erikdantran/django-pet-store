from django.db import models
# from django.forms import CharField

# Create your models here.

class Pet(models.Model):
    name = models.CharField(max_length=30)
    breed = models.CharField(max_length=30)
    age = models.IntegerField()
    color = models.CharField(max_length=20)
    category = models.CharField(max_length=10)
    description = models.CharField(max_length=200)
    sold = models.BooleanField(default=False)
    buyer = models.CharField(max_length=30, default="No buyer yet")
    imageUrl = models.CharField(
        max_length=1000, default="https://i.guim.co.uk/img/media/03734ee186eba543fb3d0e35db2a90a14a5d79e3/0_173_5200_3120/master/5200.jpg?width=1200&height=900&quality=85&auto=format&fit=crop&s=9c30ed97ea8731f3e2a155467201afe3")

    def __str__(self):
        return self.name


class Customer(models.Model):
    name = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    phone = models.CharField(max_length=15)
    card = models.IntegerField()

    def __str__(self):
        return self.name
