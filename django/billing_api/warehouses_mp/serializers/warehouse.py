from rest_framework import serializers
from ..models import Almacen

class AlmacenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Almacen
        fields = ['codigo', 'nombre', 'direccion', 'ciudad', 'creado_en', 'actualizado_en']
    
    def validate_codigo(self, value):
        if ' ' in value:
            raise serializers.ValidationError('El código no debe contener espacios')
        return value
