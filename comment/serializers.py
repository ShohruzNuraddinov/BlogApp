from rest_framework import serializers

from .models import Comment
from post.serializers import PostSerailizer
# from users.serailizers import UserSerializer

from users.models import UserModel


class CommentSerailizer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(
        queryset=UserModel.objects.all(),
        slug_field='username'
    )
    post = PostSerailizer(many=False)

    class Meta:
        model = Comment
        fields = '__all__'


class CommentCreateSerailizer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'
