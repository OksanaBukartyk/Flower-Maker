from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    phone=models.CharField(max_length=13)
    profile_pic = models.ImageField(null=True, blank=True, upload_to="images", default="user.png")
    bio = models.TextField(null=True, blank=True)


class Category(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to="images", blank=False, null=False)

    def __str__(self):
        return self.name


class Product(models.Model):
    headline = models.CharField(max_length=30, blank=False, null=False)
    thumbnail = models.ImageField(upload_to="images", blank=False, null=False)
    description = models.TextField(max_length=500, null=False, blank=False)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, default=1)
    created = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.headline

class Version(models.Model):
    thumbnail = models.ImageField(upload_to="images", blank=False, null=False)
    count  = models.IntegerField(blank=False, null=False)
    price = models.IntegerField(blank=False, null=False)
    product_id = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True, default=1)
    color= models.CharField(max_length=30, blank=False, null=False)


    def __str__(self):
        return self.color


class Response(models.Model):
    text=models.CharField(max_length=30, blank=False, null=False)
    date=models.DateTimeField(auto_now_add=True)
    count_stars=models.IntegerField( null=False, blank=False)
    name=models.CharField(max_length=30, blank=False, null=False)
    email=models.CharField(max_length=30, blank=False, null=False)
    def __str__(self):
        return self.text

class Order(models.Model):
    product_id=models.ForeignKey(Product, on_delete=models.SET_NULL, null=True, default=1)
    version_id=models.ForeignKey(Version, on_delete=models.SET_NULL, null=True, default=1)
    count=models.IntegerField(blank=False, null=False)
    number=models.CharField(max_length=30, blank=False, null=False)
    first_name= models.CharField(max_length=30, blank=False, null=False)
    last_name=models.CharField(max_length=30, blank=False, null=False)

    def __str__(self):
        return self.count