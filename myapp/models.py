from django.db import models

# The `Timestamp` class is an abstract model in Python with `created_at` and `updated_at` fields that
# automatically track creation and update times.
class Timetstamp(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        abstract = True
        

# This Python class defines a Category model with fields for category name and description.
class Category(Timetstamp):
    category_name = models.CharField(max_length=100)
    discription = models.TextField()
    
    def __str__(self):
        return self.category_name
    

class Product(Timetstamp):
    product_name = models.CharField(max_length=100)
    descipton = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='products/')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.product_name

class Order(Timetstamp):
    customer_name = models.CharField(max_length=50)
    email = models.EmailField()
    Product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    
    def __str__(self):
        return f"Order #{self.id}"