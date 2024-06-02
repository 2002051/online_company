from django.urls import path
from . import views

app_name = 'newsApp'

urlpatterns = [
    path('news/<str:newName>/', views.news, name='news'), # 新闻列表
    path('newDetail/<int:id>/', views.newDetail, name='newDetail'),
]