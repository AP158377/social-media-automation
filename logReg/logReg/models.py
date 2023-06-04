from django.db import models

class user(models.Model):
    fname=models.CharField(max_length=150)
    gender=models.CharField(max_length=1)
    age=models.IntegerField()
    mobile=models.CharField(max_length=150)
    email=models.CharField(max_length=150)
    username=models.CharField(max_length=150)
    password=models.CharField(max_length=150)
class encr_data(models.Model):
    data=models.CharField(max_length=450)
class post_data(models.Model):
    data=models.CharField(max_length=450)
