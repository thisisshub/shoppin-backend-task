from uuid import uuid4
from django.db import models

class BaseDbModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
        
class AmazonProduct(BaseDbModel):
    image_url = models.URLField()
    name = models.CharField(max_length=255)
    price = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
    product_link = models.CharField(max_length=255)
    
    def __str__(self):
        return self.name
    
    def __repr__(self):
        return self.name


class BewakoofProduct(BaseDbModel):
    image_url = models.URLField()
    name = models.CharField(max_length=255)
    price = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
    product_link = models.CharField(max_length=255)
