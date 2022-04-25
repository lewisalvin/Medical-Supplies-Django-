from django.db import models

class Person(models.Model):
    firstName = models.CharField(max_length=100)
    lastName = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    insurance = models.CharField(max_length=100)
    

