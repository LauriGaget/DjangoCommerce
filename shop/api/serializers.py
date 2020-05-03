from rest_framework import serializers
from shop.models import Product


class ProductSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    category = serializers.CharField()
    name = serializers.CharField()
    description = serializers.CharField()
    brand = serializers.CharField()
    price = serializers.FloatField()
    image = serializers.ImageField

    def create(self, validated_data):
        print(validated_data)
        return Product.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.category = validated_data.get('author', instance.author)
        instance.name = validated_data.get('name', instance.author)
        instance.description = validated_data.get('description', instance.author)
        instance.brand = validated_data.get('brand', instance.author)
        instance.price = validated_data.get('price', instance.author)
        instance.image = validated_data.get('image', instance.author)
        instance.save()
        return

