from rest_framework import generics, permissions
from rest.permissions import IsOwnerOrReadOnly
from likes.models import Like
from likes.serializer import LikeSerializer


class LikeList(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = LikeSerializer
