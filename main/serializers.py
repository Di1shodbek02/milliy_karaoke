from rest_framework.serializers import ModelSerializer

from rest_framework import serializers
from main.models import Category, Video, LikeVideo, Basket


class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = ('name', 'photo')


class VideoSerializer(ModelSerializer):
    class Meta:
        model = Video
        fields = '__all__'


class LikeSerializer(ModelSerializer):
    class Meta:
        model = LikeVideo
        fields = '__all__'


class LikeVideoSerializer(ModelSerializer):
    class Meta:
        model = LikeVideo
        fields = ('video_id',)


class BasketSerializer(ModelSerializer):
    class Meta:
        model = Basket
        fields = '__all__'
