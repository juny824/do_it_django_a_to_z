from django.urls import path
from . import views

urlpatterns = [
    path('', views.PostList.as.view()),
    #path('<int:pk>/', views.single_post_page),
    path('', views.index),
]