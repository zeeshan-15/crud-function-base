from django.urls import path
from .views import *

urlpatterns = [
    path('', posts_list, name="post_list_url"),
    path('post/create', Post_Create.as_view(), name="post_create_url"),
    path('post/<str:slug>/', Post_Detail.as_view(), name="post_detail_url"),
    path('post/<str:slug>/update/', Post_Update.as_view(), name = 'post_update_url'),
    path('post/<str:slug>/delete/', Post_Delete.as_view(), name='post_delete_url'),
    path('tags/', tags_list, name='tags_list_url'),
    path('tag/create', Tag_Create.as_view(), name="tag_create_url"),
    path('tag/<str:slug>/', Tag_Detail.as_view(), name="tag_detail_url"),
    path('tag/<str:slug>/update/', Tag_Update.as_view(), name="tag_update_url"),
    path('tag/<str:slug>/delete/', Tag_Delete.as_view(), name='tag_delete_url'),
]
