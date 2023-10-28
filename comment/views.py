from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import generics, status
from rest_framework.views import APIView

from post.models import Post
from .models import Comment
from .serializers import CommentSerailizer, CommentCreateSerailizer

# Create your views here.


class CommentsView(generics.ListAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerailizer


class CommentCreateView(generics.CreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentCreateSerailizer


class CommentView(APIView):
    http_method_names = ['get']

    def get(self, request, post_id: int):
        post = Post.objects.filter(id=post_id)
        if post.exists():
            comments = Comment.objects.filter(post=post.first())
            serailizer = CommentSerailizer(comments, many=True)
            return Response(serailizer.data, status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)
        

