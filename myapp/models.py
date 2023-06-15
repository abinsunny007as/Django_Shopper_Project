from django.db import models

# Create your models here.
class CategoryDB(models.Model):
    Categoryname = models.CharField(max_length=50, null=True, blank=True)
    CatImage = models.ImageField(upload_to="category", null=True, blank=True)
    Description = models.CharField(max_length=100, null=True, blank=True)

class ProductDB(models.Model):
    Select = models.CharField(max_length=50, null=True, blank=True)
    Pname = models.CharField(max_length=50, null=True, blank=True)
    Brand = models.CharField(max_length=50, null=True, blank=True)
    Price = models.IntegerField(null=True, blank=True)
    Des = models.CharField(max_length=100, null=True, blank=True)
    ProductImage = models.ImageField(upload_to="Product", null=True, blank=True)

class ContactDB(models.Model):
    Fname = models.CharField(max_length=50, null=True, blank=True)
    Lname = models.CharField(max_length=50, null=True, blank=True)
    Email = models.CharField(max_length=50, null=True, blank=True)
    Subject = models.CharField(max_length=50, null=True, blank=True)
    Message = models.CharField(max_length=200, null=True, blank=True)
