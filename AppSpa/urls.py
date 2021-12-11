from django.urls import path
from .Views.v_home import Home,error
from .Views.v_post import PostPage
from .Views.v_tag_list import TagList
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('home',Home,name='homepage'),
    path('tag/<slug:slug>',TagList,name='tagpage'),
    path('post/<slug:slug>',PostPage,name='postpage'),
]

