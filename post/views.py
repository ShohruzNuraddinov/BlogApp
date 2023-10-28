from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response


from .models import Post, Tags, Category
from .serializers import PostSerailizer, PostCreateSeralizer, CategorySeralizer, TagsSerailizer

# Create your views here.


class PostsView(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerailizer


class PostCreateView(generics.CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostCreateSeralizer
    permission_classes = [IsAuthenticated]


class PostGetView(APIView):
    http_method_names = ['get', 'put', 'delete']

    def get(self, request, post_id: int):
        post = Post.objects.get(id=post_id)
        serializer = PostSerailizer(post, many=False)
        return Response(serializer.data)

    def put(self, request, post_id: int):
        if request.user.is_authenticated:

            post = Post.objects.filter(id=post_id)
            if post.exists():
                serailizer = PostSerailizer(post.first(), data=request.data)
                if serailizer.is_valid():
                    serailizer.save()
                    return Response(serailizer.data)
        else:
            return Response(data={'detail': 'Authentication credentials were not provided.'}, status=status.HTTP_401_UNAUTHORIZED)

    def delete(self, request, post_id: int):
        if request.user.is_authenticated:
            post = Post.objects.filter(id=post_id)
            if post.exists():
                post.first().delete()
                return Response(status=status.HTTP_200_OK)
        else:
            return Response(data={'detail': 'Authentication credentials were not provided.'}, status=status.HTTP_401_UNAUTHORIZED)


class CategoryView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySeralizer


class CategoryCreateView(generics.CreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySeralizer


class TagsView(generics.ListAPIView):
    queryset = Tags.objects.all()
    serializer_class = TagsSerailizer


class TagCreateView(generics.CreateAPIView):
    queryset = Tags.objects.all()
    serializer_class = TagsSerailizer
