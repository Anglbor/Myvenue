from django.db import models
from django.contrib.auth.models import User

class Venue(models.Model):
    name = models.CharField('Venue Name', max_length=120)
    address = models.CharField(max_length=300, blank=True)
    zip_code = models.CharField('Zip Code', max_length=20, blank=True)
    phone = models.CharField('Phone', max_length=50, blank=True)
    web = models.URLField('Website Address', blank=True)
    email = models.EmailField('Email', blank=True)

    def __str__(self):
        return self.name

class MyUsers(models.Model):
    first_name = models.CharField(max_length=120)
    last_name = models.CharField(max_length=120)
    email = models.EmailField('User Email')

    def __str__(self):
        return self.first_name + " " + self.last_name


class Meet(models.Model):
    name = models.CharField('Meet Name', max_length=120)
    meet_date = models.DateTimeField('Meet Date')
    venue = models.ForeignKey(Venue, blank=True, null=True, on_delete=models.CASCADE)
    manager = models.ForeignKey(User, blank=True, null=True, on_delete=models.SET_NULL)
    description = models.TextField(blank=True)
    guests = models.ManyToManyField(MyUsers, blank=True)


    def __str__(self):
        return self.name







