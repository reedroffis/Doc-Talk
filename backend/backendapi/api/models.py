from django.db import models


class Doctor(models.Model):
    name = models.TextField(max_length=32, blank=False, null=False)
    address = models.TextField(max_length=50, blank=False)
    phone_number = models.TextField(max_length=50, blank=False) 
