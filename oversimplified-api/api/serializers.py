from rest_framework import serializers
from base.models import Item, models

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'