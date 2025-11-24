from django.contrib.auth.models import User
from rest_framework import serializers

class UsuarioAdminListadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'id', 'username', 'email', 'first_name', 'last_name',
            'is_active', 'is_staff', 'date_joined', 'last_login'
        )
        read_only_fields = ('id', 'date_joined', 'last_login')

class UsuarioAdminEscrituraSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=False, allow_blank=True)

    class Meta:
        model = User
        fields = (
            'username', 'email', 'first_name', 'last_name',
            'is_active', 'is_staff', 'password'
        )

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        usuario = User(**validated_data)
        usuario.set_password(password or User.objects.make_random_password())
        usuario.save()
        return usuario

    def update(self, instance, validated_data):
        password = validated_data.pop('password', None)
        for k, v in validated_data.items():
            setattr(instance, k, v)
        if password:
            instance.set_password(password)
        instance.save()
        return instance
