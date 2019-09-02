from django.db import models

# Create your models here.



class Product(models.Model):
    product_name = models.CharField(max_length=50)
    price = models.BigIntegerField()
    info = models.CharField(max_length=500)
    compony = models.CharField(max_length=50)
    def __str__(self):
            return self.product_name
