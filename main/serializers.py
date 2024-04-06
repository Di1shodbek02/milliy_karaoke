from rest_framework.serializers import ModelSerializer

from rest_framework import serializers
from main.models import Category, Video, LikeVideo, Basket


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


class VideoLikeSerializer(ModelSerializer):
    class Meta:
        model = LikeVideo
        fields = '__all__'


class BasketListSerializer(ModelSerializer):
    class Meta:
        model = Basket
        fields = '__all__'


class VideoModelSerializer(ModelSerializer):
    class Meta:
        model = Video
        fields = '__all__'
