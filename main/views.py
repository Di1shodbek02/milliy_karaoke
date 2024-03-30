from rest_framework.response import Response
from rest_framework.generics import ListAPIView, GenericAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework import filters, status

from accounts.permission import IsAdminPermission
from main.models import Category, Video, LikeVideo, Basket
from main.serializers import CategorySerializer, VideoSerializer, LikeSerializer, BasketSerializer, LikeVideoSerializer


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


class BasketListAPIView(ListAPIView):
    queryset = Basket.objects.all()
    serializer_class = BasketSerializer
    permission_classes = (IsAuthenticated,)


class Like_Video(GenericAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = LikeVideoSerializer

    def post(self, request):
        video_id = request.data.get('video_id')
        user_id = request.user.id

        if LikeVideo.objects.filter(video_id=video_id, user_id=user_id).exists():
            return Response({"message": "You have already liked this video."}, status=status.HTTP_400_BAD_REQUEST)

        like_data = {
            'video_id': video_id,
            'user_id': user_id,
            'count': 1
        }
        serializer = self.get_serializer(data=like_data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)


class LikeVideoLictAPIView(GenericAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = LikeSerializer

    def get(self, request):
        like_count = LikeVideo.objects.all()
        serializer = LikeSerializer(like_count, many=True)
        return Response(serializer.data)


class VideoMusic(GenericAPIView):
    permission_classes = (IsAuthenticated,)
