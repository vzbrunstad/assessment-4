from django.db import models
from django.db.models.deletion import CASCADE

# Create your models here.

class Category (models.Model):
    name = models.CharField(max_length=200)
    
    def __str__(self):
        return f"{self.name}"

class Post(models.Model):
    item = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    category = models.ForeignKey(Category, on_delete=CASCADE, related_name='post_category')
  
    def __str__(self):
        return f"{self.item}"