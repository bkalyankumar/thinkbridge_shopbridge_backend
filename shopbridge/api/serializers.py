from rest_framework import serializers
from .models import Products
from django.contrib.auth.models import User

class TokenSerializer(serializers.Serializer):
    """
    This serializer serializes the token data
    """
    token = serializers.CharField(max_length=255)

class UserSerializer(serializers.ModelSerializer):
    """
    This serializer serializes the User data
    """
    class Meta:
        model = User
        fields = ("username", "password", "email")

class ProductsSerializer(serializers.ModelSerializer):
    """
    This serializer serializes the product data
    """
    class Meta:
        model = Products
        fields = ('name', 'description', 'price', 'category')
    
    """
    Function to update product
    """
    def update(self, instance, validated_data):
        instance.name = validated_data.get("name", instance.name)
        instance.description = validated_data.get("description", instance.description)
        instance.price = validated_data.get("price", instance.price)
        instance.category = validated_data.get("category", instance.category)
        instance.save()
        return instance