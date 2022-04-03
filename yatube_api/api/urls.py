from django.urls import path, include

from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views

from posts.views import PostViewSet, CommentViewSet, GroupViewSet

v1_router = DefaultRouter()

app_name = 'api'

v1_router.register(r'posts', PostViewSet)
v1_router.register(r'posts/(?P<post_id>\d+)/comments', CommentViewSet)
v1_router.register(r'groups', GroupViewSet)

urlpatterns = [
    path('v1/', include(v1_router.urls)),
    path('v1/api-token-auth/', views.obtain_auth_token),
]
