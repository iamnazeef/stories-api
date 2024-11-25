from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.utils import timezone
from django.shortcuts import get_object_or_404

from .models import Story
from .serializers import StorySerializer


class StoryView(APIView):
    def get(self, request, id=None):
        current_time = timezone.now()
        if id is not None:
            story = get_object_or_404(Story, id=id)
            return Response(StorySerializer(story).data)

        stories = Story.objects.filter(
            expires_at__gt=current_time).order_by('-created_at')
        serializer = StorySerializer(stories, many=True)
        return Response(serializer.data)

    def post(self, request):
        if request.user.is_authenticated:
            # Check if the image is in request.FILES
            if 'image' not in request.FILES:
                return Response({"error": "No image file provided"}, status=status.HTTP_400_BAD_REQUEST)

            serializer = StorySerializer(data=request.data)
            if serializer.is_valid():
                serializer.save(user=self.request.user)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        return Response({"detail": "Authentication credentials were not provided."}, status=status.HTTP_401_UNAUTHORIZED)
