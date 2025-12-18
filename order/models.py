from django.db import models
from home.models import Book

# Create your models here.
class Order(models.Model):
    customer_name = models.CharField(max_length=100)
    product = models.ForeignKey(Book, on_delete=models.CASCADE)
    order_date = models.DateTimeField(auto_now_add=True)
    transaction  = models.OneToOneField('Transaction', on_delete=models.CASCADE, related_name='order')

    def __str__(self):
        return f"Order {self.id} - {self.product} for {self.customer_name}"
    
class Transaction(models.Model):
    transaction_uuid = models.CharField(max_length=100, unique=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    tax_amount = models.DecimalField(max_digits=10, decimal_places=2)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    product_code = models.CharField(max_length=50)
    service_charge = models.DecimalField(max_digits=10, decimal_places=2)
    delivery_charge = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Transaction {self.transaction_uuid}."