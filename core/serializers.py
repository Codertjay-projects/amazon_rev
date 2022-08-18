from rest_framework import serializers


class CategorySerializer(serializers.Serializer):
    url = serializers.CharField(max_length=200)


class ProductSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=1000, required=False)
    brand = serializers.CharField(max_length=1000, required=False)
    date = serializers.CharField(max_length=2000, required=False)
    image = serializers.ListField(max_length=2000, required=False)
    tag = serializers.CharField(max_length=2000, required=False)
    rank = serializers.CharField(max_length=2000, required=False)
    description = serializers.JSONField(max_length=20000, required=False)
