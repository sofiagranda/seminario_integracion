from rest_framework import serializers
from catalog.models import Category

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ("id", "nombre", "slug", "creado_en", "actualizado_en")
        read_only_fields = ("id", "creado_en", "actualizado_en")
