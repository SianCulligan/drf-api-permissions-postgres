from rest_framework import serializers
from .models import Outfits

class PostSerializer(serializers.ModelSerializer):
    class Meta: 
        fields = ('id', 'outfit_wearer', 'outfit_name', 'top', 'bottom', 'shoes', 'created_at')
        model = Outfits