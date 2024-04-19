from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from main.models import Category, Video, LikeVideo, Basket, Notification


class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class VideoSerializer(ModelSerializer):
    class Meta:
        model = Video
        fields = '__all__'


class LikeSerializer(serializers.Serializer):
    like = serializers.BooleanField()
    video_id = serializers.IntegerField()


class BasketSerializer(serializers.Serializer):
    basket = serializers.BooleanField()
    video_id = serializers.IntegerField()


class VideoLikeSerializer(serializers.ModelSerializer):
    video = serializers.SerializerMethodField()

    class Meta:
        model = LikeVideo
        fields = ('user_id', 'video')

    def get_video(self, obj):
        video = obj.video_id
        return {
            'title': video.title,
            'image': video.image.url,
            'music': video.music.url,
            'text': video.text,
            'category_id': video.category_id_id,
            'uploaded_at': video.uploaded_at,
        }


class BasketListSerializer(ModelSerializer):
    video = serializers.SerializerMethodField()

    class Meta:
        model = Basket
        fields = ('user_id', 'video')

    def get_video(self, obj):
        video = obj.video_id
        return {
            'title': video.title,
            'image': video.image.url,
            'music': video.music.url,
            'text': video.text,
            'category_id': video.category_id_id,
            'uploaded_at': video.uploaded_at,
        }


class VideoModelSerializer(ModelSerializer):
    class Meta:
        model = Video
        fields = '__all__'


class NotificationSerializer(ModelSerializer):
    class Meta:
        model = Notification
        fields = '__all__'
