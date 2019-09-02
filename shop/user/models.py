from django.db import models
from django.contrib.auth.models import User
from products.models import Product
# Create your models here.


class Customer(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    sexuality = (
        ('M','male'),
        ('F','female'),
        ('O','other'),
    )
    sex = models.CharField(max_length = 1 , choices = sexuality)
    phone_number = models.CharField(max_length = 11)
    birth_date = models.DateTimeField()
    age = models.IntegerField()
    address = models.CharField(max_length = 255)
    national_code = models.CharField(max_length = 11)
    def __str__(self):
            return self.user


            
class Purchase(models.Model):
    user = models.ForeignKey(User,on_delete = models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    def __str__(self):
            return str(self.user)+" , "+str(self.product)
