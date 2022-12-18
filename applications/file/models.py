from django.db import models
from core.models import BaseModel
from applications.product.models import Product

class File(BaseModel):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images')
    file = models.FileField(upload_to='files')
    
    def __str__(self):
        return self.product