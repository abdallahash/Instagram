from django.urls import path, include
from .views import (
    PostDetailView,
    PostListView,
    post_create_view,
    PostCreateView,
)
# from django.contrib.auth import views as auth_views
app_name = 'insta' 
urlpatterns = [
    path('', PostListView.as_view(), name='post_list'),
    path('<int:id>',PostDetailView.as_view(), name='post_detail'),
    path('create/', post_create_view, name='post_create'),
    path('new/', PostCreateView.as_view(), name='post_new'),
]