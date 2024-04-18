from django.urls import path

from .views import (CategoryGenericAPIView, CategoryVideo, VideoListAPIView, CategorySearch, VideoSearch,
                    LikeVideoAPIView, BasketListAPIView, VideoMusic, VideoLikeAPIView, BasketVideoAPIView,
                    NotificationAPIView, NotificationDetailView)

urlpatterns = [
    path('category-list/', CategoryGenericAPIView.as_view(), name='category_list'),
    path('category-video/<int:category_id>', CategoryVideo.as_view(), name='category_video'),
    path('video-list/', VideoListAPIView.as_view(), name='video_list'),
    path('search-category/', CategorySearch.as_view(), name='search_category'),
    path('search-video/', VideoSearch.as_view(), name='video_search'),
    path('like-video-list/', VideoLikeAPIView.as_view(), name='like_video_list'),
    path('like-video/', LikeVideoAPIView.as_view(), name='like_video'),
    path('basket-video/', BasketVideoAPIView.as_view(), name='basket_video'),
    path('backet-list-video/', BasketListAPIView.as_view(), name='backet_videos'),
    path('video-music/<int:video_id>', VideoMusic.as_view(), name='video_music'),
    path('notification/', NotificationAPIView.as_view(), name='notification'),
    path('notification-detail/<int:pk>', NotificationDetailView.as_view(), name='notification-detail'),
]
