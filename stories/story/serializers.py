from rest_framework import serializers
from .models import Story


class StorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Story
        fields = ['id', 'image', 'caption', 'created_at', 'expires_at']

        read_only_fields = ['created_at']
