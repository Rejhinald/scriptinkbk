from rest_framework import serializers
from .models import *

class ProductSerializer(serializers.ModelSerializer):
    author = serializers.SerializerMethodField()
    genre_name = serializers.ReadOnlyField(source='genre.name')

    def get_author(self, obj):
        if obj.author:
            return f"{obj.author.first_name} {obj.author.last_name}"
        else:
            return None

    class Meta:
        model = Product
        fields = '__all__'
        

class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = '__all__'

class TierSerializer(serializers.ModelSerializer):
    genre_name = serializers.ReadOnlyField(source='genre.name')
    class Meta:
        model = Tier
        fields = '__all__'

class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SerializerMethodField()
    author_email = serializers.EmailField(source='author.email')

    def get_author(self, obj):
        if obj.author:
            return f"{obj.author.first_name} {obj.author.last_name}"
        else:
            return None
    
    class Meta:
        model = Comment
        fields = '__all__'

