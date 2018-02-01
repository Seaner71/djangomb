from django.db import models

class Post(models.Model):
    text= models.TextField()

    def __str__(self):
        """A string representation of the model"""
        return self.text[:50]
class Dish(models.Model):
    name = models.CharField(max_length=4000, blank=False)
    description = models.CharField(max_length=4000, blank=False)
    price = models.DecimalField(default=0, max_digits=10, decimal_places=2)

    def __str__(self):
        """A string representation of the model"""
        return self.name[:50]
