from django.db import models

from core.models import BaseModel


class Category(BaseModel):
    title = models.CharField(max_length=50)
    description = models.TextField()
    image = models.ImageField(null=True,blank=True)

    def __str__(self):
        return self.title


class Product(BaseModel):
    name = models.CharField(max_length=100)
    price = models.DecimalField(decimal_places=2, max_digits=5)
    quantity = models.IntegerField()
    description = models.TextField()
    images = models.ImageField(null=True,blank=True)
    categories = models.ForeignKey(Category,on_delete=models.CASCADE)

    def __str__(self):
        return self.name