from django.db import models

# Create your models here.

class About(models.Model):
    name=models.CharField(max_length=50,verbose_name="Enter your name")
    age=models.IntegerField(max_length=2,verbose_name="Enter your age")
    dob=models.DateField(verbose_name="Enter your DOB")
    mobile=models.CharField(max_length=12,verbose_name="Enter your number")
    email=models.EmailField(max_length=40,verbose_name="Enter your email")
    city=models.CharField(max_length=30,verbose_name="Enter your city")
    website=models.CharField(max_length=50,verbose_name="Enter your website")
    degree=models.CharField(max_length=50,verbose_name="Enter your degree")
    shor_desc=models.TextField(verbose_name="Enter your description")
    desc=models.TextField(verbose_name="Enter your description")
    pimg=models.ImageField(verbose_name="Enter your img")
    freelance=models.CharField(max_length=100, default="Available")
    mapurl=models.URLField(max_length=400,default="see url")
    sumdes=models.TextField(default="Not Provided")
    condes=models.TextField(default="Not Provided")
    

    class Meta:
        db_table="about"

class Skills(models.Model):
    tech=models.CharField(max_length=40,verbose_name="enter your skills;")
    rate=models.IntegerField(max_length=5,verbose_name="enter your rate of skills in persantage")
    desc=models.TextField(max_length=300,verbose_name="enter you descripseion")

    class Meta:
        db_table='skills'

class Eduction(models.Model):
    degree=models.CharField(max_length=30, verbose_name='enter your degree ')
    year=models.CharField(verbose_name="enter years")
    clgname=models.CharField(max_length=50,verbose_name='enter your clg name')
    desc=models.TextField(max_length=300,verbose_name='enter your decs')

    class Meta:
        db_table='eduction'

class Experince(models.Model):
     year=models.CharField(max_length=25,verbose_name="enter years")
     company=models.CharField(max_length=30,verbose_name='enter your company name')
     desc=models.TextField(max_length=300,verbose_name='enter your decs')
     desc1 = models.TextField(default="Not Provided")
     work = models.CharField(max_length=200, default="Developer")

     class Meta:
         db_table='experince'

class Contact(models.Model):
    name=models.CharField(max_length=30,verbose_name="enter name")
    email=models.CharField(max_length=50,verbose_name="enter email")
    subject=models.CharField(max_length=30,verbose_name="enter subject")  
    message=models.TextField(verbose_name="enter message")

    class  Meta:
        db_table = 'contact'

        
        

