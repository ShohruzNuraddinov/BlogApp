from rest_framework import serializers

from .models import UserModel as User, SocialMedia


class SocialMediaSerailizer(serializers.ModelSerializer):
    class Meta:
        model = SocialMedia
        fields = '__all__'


class UserSerializer(serializers.HyperlinkedModelSerializer):
    # social_media = SocialMediaSerailizer(many=True)

    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'is_staff', 'social_media']
