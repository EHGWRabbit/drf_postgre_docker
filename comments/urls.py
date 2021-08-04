from django.urls import path
from . import views
from .views import CommentList, PostList

urlpatterns = [
    path('', views.post_detail),
    path('list/', PostList.as_view()),
    path('comment/', CommentList.as_view()),
]