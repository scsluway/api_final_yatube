# TODO:  Напишите свой вариант
from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.filters import SearchFilter
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.permissions import IsAuthenticated

from api import permissions, serializers
from posts import models


class PostViewSet(viewsets.ModelViewSet):
    queryset = models.Post.objects.all()
    permission_classes = (permissions.OnlyAuthorDestroyUpdate,)
    serializer_class = serializers.PostSerializer
    pagination_class = LimitOffsetPagination

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.Group.objects.all()
    serializer_class = serializers.GroupSerializer


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.CommentSerializer
    permission_classes = (permissions.OnlyAuthorDestroyUpdate,)

    def get_post(self):
        return get_object_or_404(models.Post, pk=self.kwargs.get('post_id'))

    def get_queryset(self):
        return self.get_post().comments

    def perform_create(self, serializer):
        serializer.save(author=self.request.user, post=self.get_post())


class FollowViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.FollowSerializer
    filter_backends = (SearchFilter,)
    permission_classes = (IsAuthenticated,)
    search_fields = ('following__username', )

    def get_queryset(self):
        return self.request.user.follows

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
