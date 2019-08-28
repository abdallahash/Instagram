from django.urls import path, include
from .views import (
    PostDetailView,
    PostDeleteView,
    PostListView,
    PostCreateView,
    PostUpdateView,
)
# from django.contrib.auth import views as auth_views
app_name = 'insta' 
urlpatterns = [
    path('', PostListView.as_view(), name='post_list'),
    path('<int:id>',PostDetailView.as_view(), name='post_detail'),
    path('new/', PostCreateView.as_view(), name='post_new'),
    path('<int:id>/update/', PostUpdateView.as_view(), name='post_update'),
    path('<int:id>/delete/', PostDeleteView.as_view(), name='post_delete'),
    # path('api_upload/', FileView.as_view(), name='file-upload')
]


