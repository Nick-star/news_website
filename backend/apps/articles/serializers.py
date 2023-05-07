from rest_framework import serializers
from .models import Article, Category

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name')

class ArticleSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    author = serializers.StringRelatedField()

    class Meta:
        model = Article
        fields = ('id', 'title', 'content', 'category', 'author', 'published_at')
