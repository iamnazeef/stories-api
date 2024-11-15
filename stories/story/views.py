from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.utils import timezone

from .models import Story
from .serializers import StorySerializer


class StoryView(APIView):
    def get(self, request):
        current_time = timezone.now()
        stories = Story.objects.filter(
            expires_at__gt=current_time).order_by('-created_at')
        serializer = StorySerializer(stories, many=True)
        return Response(serializer.data)

    def post(self, request):
        # Check if the image is in request.FILES
        if 'image' not in request.FILES:
            return Response({"error": "No image file provided"}, status=status.HTTP_400_BAD_REQUEST)

        serializer = StorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
