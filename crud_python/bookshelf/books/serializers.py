from rest_framework import serializers
from .models import Book

class BookSerializer(serializers.ModelSerializer):
    category = serializers.SerializerMethodField()

    class Meta:
        model = Book
        fields = ['id', 'title', 'author', 'isbn', 'publish_date', 'category']

    def get_category(self, obj):
        return [category.category_name for category in obj.category.all()]

    def create(self, validated_data):
        data_category = validated_data.pop('category', [])
        book = Book.objects.create(**validated_data)
        book.category.set(data_category)
        return book

    def update(self, instance, validated_data):
        data_category = validated_data.pop('category', [])
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        instance.category.set(data_category)
        return instance