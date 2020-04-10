from django.db import models
from datetime import datetime
from realtors.models import Realtor

class State(models.Model):
    code = models.CharField(max_length=3)
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class Listing(models.Model):

    realtor = models.ForeignKey(Realtor, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=100)
    state = models.ForeignKey(State, on_delete=models.CASCADE)
    zipcode= models.CharField(max_length=20)
    description = models.TextField(blank=True)
    price = models.IntegerField(blank=True)
    bedrooms = models.IntegerField()
    bathrooms = models.DecimalField(max_digits=2, decimal_places=1)
    garage = models.IntegerField(default=0)
    sqft = models.IntegerField()
    lot_size = models.DecimalField(max_digits=5, decimal_places=1)
    photo_main = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    
    is_published = models.BooleanField(default=True)
    list_date = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.title

class ListingPhoto(models.Model):
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE)
    description = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    main_photo = models.BooleanField(default=False)
    def __str__(self):
        return self.description


 

    


