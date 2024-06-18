from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import UrineStripImage
from .serializers import UrineStripImageSerializer
from .utils import process_image
from django.shortcuts import render
from django.conf import settings

class UrineStripImageView(APIView):
    def get(self, request, *args, **kwargs):
        images = UrineStripImage.objects.all()
        serializer = UrineStripImageSerializer(images, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        serializer = UrineStripImageSerializer(data=request.data)
        if serializer.is_valid():
            urine_strip_image = serializer.save()
            image_path = urine_strip_image.image.path  # Get the correct path to the saved image
            colors = process_image(image_path)
            return Response(colors, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def index(request):
    return render(request, 'api/index.html')
