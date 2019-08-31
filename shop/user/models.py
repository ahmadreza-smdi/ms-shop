from django.db import models
from django.contrib.auth.models import User
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


