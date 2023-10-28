from rest_framework import serializers

from .models import Post, Tags, Category

from users.models import UserModel as User


class TagsSerailizer(serializers.ModelSerializer):
    class Meta:
        model = Tags
        fields = ['name']


class CategorySeralizer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['name']


class PostSerailizer(serializers.ModelSerializer):
    tags = serializers.SlugRelatedField(
        slug_field='name',
        many=True,
        read_only=True
    )
    category = serializers.SlugRelatedField(
        queryset=Category.objects.all(),
        slug_field='name'
    )

    user = serializers.SlugRelatedField(
        queryset=User.objects.all(),
        slug_field='username'
    )

    class Meta:
        model = Post
        fields = ['id', 'image', 'user', 'tags', 'category', 'title',
                  'content', 'created_at', 'published_at', 'read_time']


class PostCreateSeralizer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'
