from django.db import models

from core.models import BaseModel


class Category(BaseModel):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name