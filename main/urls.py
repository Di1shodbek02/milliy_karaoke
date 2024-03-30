from django.urls import path

from .views import CategoryGenericAPIView, CategoryVideo, VideoListAPIView, CategorySearch, VideoSearch, \
    LikeVideoLictAPIView, Like_Video, BasketListAPIView

urlpatterns = [
    path('category-list/', CategoryGenericAPIView.as_view(), name='category_list'),
    path('category-video/<int:category_id>', CategoryVideo.as_view(), name='category_video'),
    path('video-list/', VideoListAPIView.as_view(), name='video_list'),
    path('search-category/', CategorySearch.as_view(), name='search_category'),
    path('search-video/', VideoSearch.as_view(), name='video_search'),
    path('like-video-count/', LikeVideoLictAPIView.as_view(), name='like_video_count'),
    path('like-video/', Like_Video.as_view(), name='like_video'),
    path('backet-videos/', BasketListAPIView.as_view(), name='backet_videos'),
]
