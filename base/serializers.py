from rest_framework import serializers
from .models import *

class ProductSerializer(serializers.ModelSerializer):
    genre = serializers.StringRelatedField(read_only=True, many=False)
    class Meta:
        model = Product
        fields = '__all__'

class ThemeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Theme
        fields = '__all__'

class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = '__all__'
