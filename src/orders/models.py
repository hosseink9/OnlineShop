from django.db import models

from core.models import BaseModel
from users.models import User
from product.models import Product

class Discount(BaseModel):
    discount_amount = models.DecimalField(decimal_places=1, max_digits=3, default=0.0)

    def __str__(self):
        return self.discount_amount


class Payment(BaseModel):
    is_paid = models.BooleanField()

    def __str__(self):
        return self.is_paid


class Order(BaseModel):
    customer = models.ForeignKey(User,on_delete=models.CASCADE)
    discount_amount = models.ForeignKey(Discount,on_delete=models.CASCADE)
    payment_amount = models.ForeignKey(Payment,on_delete=models.CASCADE)

    def __str__(self):
        return self.customer


class OrderItem(BaseModel):
    quantity = models.IntegerField()
    unit_price = models.DecimalField(decimal_places=2, max_digits=5)
    discount_amount = models.DecimalField(decimal_places=1, max_digits=3, default=0.0)

    orders = models.ForeignKey(Order,on_delete=models.CASCADE)
    products = models.ForeignKey(Product,on_delete=models.CASCADE)

    def __str__(self):
        return self.quantity


