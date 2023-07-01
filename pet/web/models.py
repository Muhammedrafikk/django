from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    image = models.ImageField(upload_to='media/product_image')


class Order(models.Model):

    user=models.ForeignKey(User,on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    company=models.CharField(max_length=100)
    country=models.CharField(max_length=100)
    address= models.TextField()
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    pincode = models.IntegerField()
    phone = models.IntegerField()
    email = models.EmailField(max_length=100)
    account = models.CharField(max_length=100)

    def __str__(self):
        return self.first_name



class OrderItem(models.Model):
    order = models.ForeignKey(Order,on_delete=models.CASCADE)
    Product = models.CharField(max_length=100)
    image=models.ImageField(upload_to='media/product_image')
    qunatity= models.IntegerField()
    price = models.IntegerField()
    total = models.IntegerField()
    price = models.IntegerField(default=False)



class fristemail(models.Model):

    Email= models.EmailField(max_length=100)

class contact_data(models.Model):

    Name= models.CharField(max_length=100)
    Email= models.EmailField(max_length=100)
    Subject= models.CharField(max_length=100)
    Message= models.CharField(max_length=100)

class leave_cont(models.Model):

    Name= models.CharField(max_length=100)
    Email= models.EmailField(max_length=100)
    Webiste= models.CharField(max_length=100)
    Comment= models.CharField(max_length=100)



   


