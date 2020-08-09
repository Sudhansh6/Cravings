from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class item(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    img = models.ImageField(upload_to='pictures')
    price = models.IntegerField()
