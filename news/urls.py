from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name = 'index'),
    path('news/<int:post_id>/', views.news_post),
    path("news/", views.main_page),
    path("news/create/", views.create),
]