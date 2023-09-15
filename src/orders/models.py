from django.db import models

from core.models import BaseModel
from users.models import User
from product.models import Product

class Discount(BaseModel):
    discount = models.DecimalField(decimal_places=1, max_digits=3, default=0.0)

    def __str__(self):
        return self.discount
