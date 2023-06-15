from django.db import models

# Create your models here.
class signupDB(models.Model):
    Username = models.CharField(max_length=50, blank=True, null=True)
    Email = models.CharField(max_length=50, blank=True, null=True)
    Phone = models.IntegerField(blank=True, null=True)
    password = models.CharField(max_length=50, blank=True, null=True)
    Confrim_pswd = models.CharField(max_length=50, blank=True, null=True)
    Profile_img = models.ImageField(upload_to="Profile", null=True, blank=True)

class cartDB(models.Model):
    Username = models.CharField(max_length=50, blank=True, null=True)
    Brand = models.CharField(max_length=100, null=True, blank=True)
    Price = models.IntegerField(null=True, blank=True)
    Quality = models.IntegerField(null=True, blank=True)
    Total = models.IntegerField(null=True, blank=True)
