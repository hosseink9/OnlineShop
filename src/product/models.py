from django.db import models

from core.models import BaseModel


class Category(BaseModel):
    title = models.CharField(max_length=50)
    description = models.TextField()
    image = models.ImageField(null=True,blank=True)

    def __str__(self):
        return self.name