from django.db import models

# Create your models here.
class RegisterModel(models.Model):
    class Meta:
        abstract = True

    telephone = models.CharField(unique=True, max_length=20, null=True)
    nickname = models.CharField(max_length=20,null=True,blank=False,default="")
    password = models.CharField(max_length=128,blank=False,default="")
    country = models.CharField(max_length=30, default="", blank=False)