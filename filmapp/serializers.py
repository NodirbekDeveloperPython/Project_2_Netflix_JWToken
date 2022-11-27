from rest_framework.exceptions import ValidationError
from rest_framework.serializers import ModelSerializer
from .models import *

class AktyorSerializer(ModelSerializer):
    class Meta:
        model = Aktyor
        fields = '__all__'

    def validate_jins(self,value):
        if value.lower() != 'erkak' and value.lower() != 'ayol':
            raise ValidationError("Aktyorlar jinsi bunday qiymatni qabul qilolmaydi.")
        return value

class KinoSerializer(ModelSerializer):
    aktyorlar = AktyorSerializer(many=True)
    class Meta:
        model = Kino
        fields = '__all__'

class CommentSerializer(ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'