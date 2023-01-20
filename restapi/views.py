from django.shortcuts import render
from rest_framework.generics import (
    ListAPIView,
    CreateAPIView,
    RetrieveAPIView,
    RetrieveUpdateAPIView,
    DestroyAPIView,
)
from.permissions import IsOwnerOrReadOnly
from rest_framework.permissions import(
    IsAuthenticated,
    IsAdminUser,
    AllowAny,
    IsAuthenticatedOrReadOnly
)
from.serializers import (
    PostformSerializer,
    CreateSerializer,

)
from . models import Posts
from rest_framework.pagination import(
    LimitOffsetPagination,
    PageNumberPagination
)


class PostList(ListAPIView):
    queryset = Posts.objects.all()
    serializer_class = PostformSerializer

class CreatePost(CreateAPIView):
    queryset = Posts.objects.all()
    serializer_class = CreateSerializer
    post_permission= [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save (user=self.request.user)

class Retrieve(RetrieveAPIView):
    queryset = Posts.objects.all()
    serializer_class= PostformSerializer

class Update(RetrieveUpdateAPIView):
    queryset = Posts.objects.all()
    serializer_class= PostformSerializer
    post_permission = [ IsOwnerOrReadOnly]

    def perform_update(self, serializer):
        serializer.save(user=self.request.user)

class Delete(DestroyAPIView):
    queryset = Posts.objects.all()
    serializer_class= PostformSerializer

