from rest_framework import serializers
from .models import Women

class WomenSerializer(serializers.ModelSerializer):
    test = serializers.IntegerField()
    class Meta:
        model = Women
        fields = ('title', 'cat_id', 'test')
