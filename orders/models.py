from django.db import models

class Order(models.Model):
    STATUS_CHOICES = [
        ('PENDING', 'Pendente'),
        ('SHIPPED', 'Enviado'),
        ('DELIVERED', 'Entregue'),
    ]
    customer_name = models.CharField(max_length=100)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='PENDING')
    created_at = models.DateTimeField(auto_now_add=True)

class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    product_name = models.CharField(max_length=100)
    quantity = models.IntegerField(default=1)
