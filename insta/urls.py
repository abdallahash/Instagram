from django.urls import path, include
from .views import (
    PostListView
)
# from django.contrib.auth import views as auth_views
app_name = 'insta' 
urlpatterns = [
    path('', PostListView.as_view(), name='post_list'),
]