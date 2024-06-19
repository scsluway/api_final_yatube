# TODO:  Напишите свой вариант
from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.pagination import LimitOffsetPagination

from api import permissions, serializers
from posts import models


class PostViewSet(viewsets.ModelViewSet):
    queryset = models.Post.objects.all()
    permission_classes = (permissions.OnlyOnwerDestroyUpdate,)
    serializer_class = serializers.PostSerializer
    pagination_class = LimitOffsetPagination

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class GroupViewSet(viewsets.ModelViewSet):
    queryset = models.Group.objects.all()
    serializer_class = serializers.GroupSerializer


class CommentViewSet(viewsets.ModelViewSet):
    queryset = models.Comment.objects.all()
    serializer_class = serializers.CommentSerializer


class FollowViewSet(viewsets.ModelViewSet):
    queryset = models.Follow.objects.all()
    serializer_class = serializers.FollowSerializer

    def perform_create(self, serializer):
        following = get_object_or_404(
            models.Follow.objects,
            username=serializer.instance.following
        )
        serializer.save(user=self.request.user, following=following)
