from django.db import models
from listings.models import Listing
from datetime import datetime

class Contact(models.Model):
    listing = models.name = models.ForeignKey(Listing, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    message = models.TextField()
    contact_date = models.DateTimeField(default=datetime.now, blank=True)
    user_id = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.name
