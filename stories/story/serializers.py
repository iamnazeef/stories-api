from rest_framework import serializers
from .models import Story


class StorySerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()

    class Meta:
        model = Story
        fields = ['id', 'image', 'caption', 'created_at',
                  'expires_at', 'user', 'is_active']

        read_only_fields = ['created_at', 'expires_at']

    def create(self, validated_data):
        request = self.context.get('request')
        if request and hasattr(request, 'user'):
            validated_data["user"] = request.user
        return super().create(validated_data)
