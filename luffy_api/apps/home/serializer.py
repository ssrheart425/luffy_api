from rest_framework import serializers
from .models import Banner


class Bannerserializer(serializers.ModelSerializer):
    class Meta:
        model = Banner
        fields = ["title", 'image', "link"]
