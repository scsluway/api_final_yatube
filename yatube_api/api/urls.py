from django.urls import include, path
from rest_framework.routers import SimpleRouter

from . import views

v1_router = SimpleRouter()
v1_router.register('posts', views.PostViewSet, basename='post')
v1_router.register(
    r'posts/(?P<post_id>\d+)/comments',
    views.CommentViewSet,
    basename='comment'
)
v1_router.register('groups', views.GroupViewSet, basename='group')
v1_router.register('follow', views.FollowViewSet, basename='follow')

v1_urls = [
    path('', include(v1_router.urls)),
    path('', include('djoser.urls.jwt')),
]

urlpatterns = [
    path('v1/', include(v1_urls)),
]
