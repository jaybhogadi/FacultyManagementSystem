from django.db import models

# Create your models here.
class members(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField(max_length = 254)
    password=models.CharField(max_length=50)
    phno=models.BigIntegerField(default=9347804746)
    dept=models.CharField(max_length=50)

class admin_table(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField(max_length = 254)
    password=models.CharField(max_length=50)

class student(models.Model):
    name=models.CharField(max_length=100)
    rollid1=models.CharField(max_length=100,default=00)
    email=models.EmailField(max_length = 254)
    year=models.CharField(max_length=50)
    dept=models.CharField(max_length=50)    

class faculty(models.Model):
    name=models.CharField(max_length=100)
    rollid=models.CharField(max_length=100,default=00)
    email=models.EmailField(max_length = 254)
    year=models.CharField(max_length=50)
    dept=models.CharField(max_length=50)       
    qualify=models.CharField(max_length=50) 
    date=models.DateField()

   
   
