from django.db import models

class Billing(models.Model):
    # user = models.ForeignKey(, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    amount = models.IntegerField()

class Customer(models.Model):
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    email = models.CharField(max_length=100)

class Product(models.Model):
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    stock = models.IntegerField()
    description = models.CharField(max_length=100)
    image = models.CharField(max_length=100)


