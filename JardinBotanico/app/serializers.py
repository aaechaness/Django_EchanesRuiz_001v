from .models import Producto, Marca
from rest_framework import serializers


class MarcaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Marca
        fields = '__all__'


class ProductoSerializer(serializers.ModelSerializer):
    nombre_marca = serializers.CharField(read_only=True, source="marca.nombre")
    marca = MarcaSerializer(read_only=True)
    marca_id = serializers.PrimaryKeyRelatedField(queryset=Marca.objects.all(), source="marca")
    nombre = serializers.CharField(required=True, min_length=3)
    
    def validate_nombre(self, values):
        existe = Producto.objects.filter(nombre_iexact=values).exists()

        if existe:
            raise serializers.ValidationError("Este producto ya existe")

        return values
    
    
    class Meta:
        model = Producto
        fields = '__all__'



