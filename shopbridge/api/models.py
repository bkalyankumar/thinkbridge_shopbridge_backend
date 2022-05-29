from django.db import models

# Create your models here.
class Products(models.Model):
    """Products class defining a model, derived from the Model class."""
    
    #Fields
    name = models.CharField(max_length=200, null=False)
    description = models.TextField(null=False)
    price = models.FloatField(null=False)
    category = models.CharField(max_length=200, null=False)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)
    
    # Metadata
    def __str__(self):
        return "{} - {} - {} - {}".format(self.name, self.description, self.price, self.category)