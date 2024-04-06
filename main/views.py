from django.db.models import Q
from rest_framework.response import Response
from rest_framework.generics import ListAPIView, GenericAPIView, RetrieveAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework import filters, status
from rest_framework.viewsets import ModelViewSet

from accounts.permission import IsAdminPermission
from main.models import Category, Video, LikeVideo, Basket
from main.serializers import CategorySerializer, VideoSerializer, LikeSerializer, BasketSerializer, \
    VideoModelSerializer, VideoLikeSerializer, BasketListSerializer


class CategoryGenericAPIView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = (IsAuthenticated,)


class CategoryVideo(GenericAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = VideoSerializer

    def get(self, request, category_id):
        video = Video.objects.filter(category_id=category_id)
        serializer = self.get_serializer(video, many=True)
        return Response({'success': True, 'data': serializer.data})


class VideoListAPIView(ListAPIView):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer
    permission_classes = (IsAuthenticated,)


class CategorySearch(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = (IsAuthenticated,)
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']


class VideoSearch(ListAPIView):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer
    permission_classes = (IsAuthenticated,)
    filter_backends = [filters.SearchFilter]
    search_fields = ['title']


class LikeVideoAPIView(GenericAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = LikeSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        like = serializer.validated_data.get('like')
        video_id = serializer.validated_data.get('video_id')
        user_id = request.user.id

        if like:
            self.like_video(video_id, user_id)
            return Response({'message': 'Video Added Successfully'})

        self.unlike_video(video_id, user_id)
        return Response({'message': 'Video Removed Successfully'})

    def like_video(self, video_id, user_id):
        user = self.request.user
        video = Video.objects.get(pk=video_id)
        LikeVideo.objects.create(video_id=video, user_id=user)

    def unlike_video(self, video_id, user_id):
        LikeVideo.objects.filter(video_id=video_id, user_id=user_id).delete()


class VideoLikeAPIView(GenericAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = VideoLikeSerializer

    def get(self, request):
        like = LikeVideo.objects.all()
        serializer = self.get_serializer(like, many=True)
        return Response(serializer.data)


class VideoMusic(GenericAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = VideoModelSerializer

    def get(self, request, video_id):
        video = Video.objects.get(id=video_id)
        serializer = self.get_serializer(video)
        return Response(serializer.data)


class BasketVideoAPIView(GenericAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = BasketSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        basket = serializer.validated_data.get('basket')
        video_id = serializer.validated_data.get('video_id')
        user_id = request.user.id

        if basket:
            self.basket_video(video_id, user_id)
            return Response({'message': 'Video Added Successfully'})

        self.unlike_video(video_id, user_id)
        return Response({'message': 'Video Removed Successfully'})

    def basket_video(self, video_id, user_id):
        user = self.request.user
        video = Video.objects.get(pk=video_id)
        Basket.objects.create(video_id=video, user_id=user)

    def unlike_video(self, video_id, user_id):
        Basket.objects.filter(video_id=video_id, user_id=user_id).delete()


class BasketListAPIView(GenericAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = BasketListSerializer

    def get(self, request):
        basket = Basket.objects.all()
        serializer = self.get_serializer(basket, many=True)
        return Response(serializer.data)
