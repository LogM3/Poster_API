from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views

v1_router = DefaultRouter()
v1_router.register('posts', views.PostViewSet)
v1_router.register('groups', views.GroupViewSet)
v1_router.register('follow', views.FollowViewSet, 'follow')
v1_router.register(
    'posts/(?P<post_id>[^/.]+)/comments', views.CommentViewSet,
    'comments')

urlpatterns = [
    # Если добавление новых пользователей не требуется,
    # значит и стандартные пути от djoser не нужны?

    # path('v1/auth/', include('djoser.urls')),
    path('v1/', include('djoser.urls.jwt')),
    path('v1/', include(v1_router.urls)),
]
