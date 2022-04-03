from django.shortcuts import get_object_or_404

from rest_framework import viewsets, permissions

from .models import Post, Comment, Group
from .serializers import PostSerializer, GroupSerializer, CommentSerializer
from .permissions import IsAuthorOrReadOnly


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated, IsAuthorOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def perform_update(self, serializer):
        super().perform_update(serializer)

    def perform_destroy(self, instance):
        super().perform_destroy(instance)


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticated, IsAuthorOrReadOnly]

    def get_queryset(self):
        post_id = self.kwargs.get("post_id")
        post = get_object_or_404(Post, id=post_id)
        comments = Comment.objects.filter(post=post)
        return comments

    def perform_create(self, serializer):
        post_id = self.kwargs.get("post_id")
        post = get_object_or_404(Post, id=post_id)
        serializer.save(author=self.request.user, post=post)

    def perform_update(self, serializer):
        super().perform_update(serializer)

    def perform_destroy(self, instance):
        super().perform_destroy(instance)


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
