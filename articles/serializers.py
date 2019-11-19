from rest_framework import serializers
from .models import Article


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ['title', 'text', 'article_id', 'version', 'created']

    def create(self, validated_data):
        identifier = self.validated_data['article_id']
        Article.objects.filter(article_id=identifier).update(flag_default=False)
        article = Article.objects.create(**validated_data)
        return article


class ArticleUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ['title', 'text', 'version', 'created']

    def create(self, validated_data):
        validated_data.pop('version', None)
        validated_data.pop('created', None)
        validated_data['article_id'] = self.context['article_id']
        article = Article.objects.create(**validated_data)
        return article


class ArticleCurrentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ['flag_default']
