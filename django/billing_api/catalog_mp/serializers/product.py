from rest_framework import serializers
from catalog.models import Product, Category

class ProductSerializer(serializers.ModelSerializer):
    nombre_categoria = serializers.ReadOnlyField(source="category.nombre")
    categoria_id = serializers.PrimaryKeyRelatedField(
        source="category", queryset=Category.objects.all(), write_only=True
    )

    class Meta:
        model = Product
        fields = ("id", "nombre", "slug", "precio", "stock", "activo",
                  "categoria_id", "nombre_categoria", "creado_en", "actualizado_en")
        read_only_fields = ("id", "creado_en", "actualizado_en", "nombre_categoria")
