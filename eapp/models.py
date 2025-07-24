from django.db import models
from django.contrib.auth.models import User

class category(models.Model):
    name=models.CharField(max_length=10)
    def __str__(self):
        return self.name
    
class Profile(models.Model):
    image = models.ImageField(default='ProfileImg/3d_default.jpg',upload_to='product')
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return str(self.us)

    
class Product(models.Model):
    name=models.CharField(max_length=40)
    price = models.FloatField()
    details=models.TextField()
    image=models.ImageField(upload_to="product",null=True,blank=True)
    catry=models.ForeignKey(category,on_delete=models.CASCADE,null=True,blank=True)
    us = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)


    def __str__(self):
        return self.name

class Order(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    order_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Order #{self.id} - {self.user.username}"
    
class OrderItem(models.Model):
    order=models.ForeignKey(Order,on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    qty = models.IntegerField()
    
    def __str__(self):
      return f"{self.qty} x {self.product.name} (Order #{self.order.id})"
    





