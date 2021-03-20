from django.db import models
from django.contrib.auth import get_user_model

class Outfits(models.Model):
    outfit_wearer = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    outfit_name = models.CharField(max_length=64)
    top = models.TextField() 
    bottom = models.TextField() 
    shoes = models.TextField() 
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.outfit_name
