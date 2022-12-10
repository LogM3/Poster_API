import base64

from django.core.files.base import ContentFile
from rest_framework import serializers
from rest_framework.relations import SlugRelatedField

from posts import models


class Base64ImageField(serializers.ImageField):
    def to_internal_value(self, data):
        if isinstance(data, str) and data.startswith('data:image'):
            extension, img_str = data.split(';base64,')
            extension = extension.split('/')[-1]
            data = ContentFile(
                base64.b64decode(img_str), name='upload.' + extension)
        return super().to_internal_value(data)


class PostSerializer(serializers.ModelSerializer):
    author = SlugRelatedField(slug_field='username', read_only=True)
    image = Base64ImageField(required=False, allow_null=True)

    class Meta:
        fields = '__all__'
        model = models.Post


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        read_only=True, slug_field='username'
    )

    class Meta:
        fields = '__all__'
        read_only_fields = ('post',)
        model = models.Comment


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = models.Group


class FollowSerializer(serializers.ModelSerializer):
    user = SlugRelatedField('username', read_only=True)
    following = SlugRelatedField(
        'username', queryset=models.User.objects.all())

    def validate_following(self, data):
        user = self.context.get('request').user
        if user == data:
            raise serializers.ValidationError(
                'Невозможно подписаться на самого себя'
            )
        if user.follower.filter(following=data).exists():
            raise serializers.ValidationError(
                'Вы уже подписаны на данного пользователя'
            )
        return data

    class Meta:
        fields = ('user', 'following')
        model = models.Follow
