from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator
# Create your models here.

class item(models.Model):
    user = models.ForeignKey(User, on_delete= models.CASCADE,)
    name = models.CharField(max_length=50)
    description = models.TextField()
    img = models.ImageField(upload_to='pictures')
    price = models.IntegerField()

class address(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,)
    name = models.CharField(max_length=50)
    street = models.CharField(max_length=50)
    city = models.CharField(max_length=20)
    state = models.CharField(max_length=20)
    pin = models.CharField(validators=[RegexValidator(regex='^.{6}$')],max_length=6)
    phone = models.CharField(validators=[RegexValidator(regex='^.{10}$')],max_length=10)
