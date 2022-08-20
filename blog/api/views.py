from rest_framework import generics

from blog.api.serializers import PostSerializer
from blog.api.permissions import AuthorModifyOrReadOnly,IsAdminUserForObject
from blog.models import Post
from rest_framework.authentication import SessionAuthentication


class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    authentication_classes = [SessionAuthentication]


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [AuthorModifyOrReadOnly | IsAdminUserForObject]
    queryset = Post.objects.all()
    serializer_class = PostSerializer