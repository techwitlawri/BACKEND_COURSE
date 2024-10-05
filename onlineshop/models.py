from django.db import models

# Create your models here.

# The `TimestampModel` class is an abstract model in Python that includes fields for creation and
# update timestamps.

class TimestampModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at= models.DateTimeField(auto_now=True)


    class Meta:
        abstract = True

class Category(TimestampModel):
    category_name= models.CharField(max_length=180)
    description = models.TextField(max_length= 250)

    def __str__(self):
        return self.category_name

class Product(TimestampModel):
    product_name = models.CharField(max_length=180)
    description = models.TextField(max_length=250)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image= models.FileField(upload_to='product/')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.product_name

class Order(TimestampModel):
    customer_name = models.CharField(max_length=180)
    customer_email=models.EmailField()
    product= models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
   

    def __str__(self):
        """
        The `__str__` method in the Python code snippet returns a string representation of an object,
        specifically "Order #1".
        :return: The `__str__` method is returning a string "Order #1".
        """
        return f"Order #1"
   