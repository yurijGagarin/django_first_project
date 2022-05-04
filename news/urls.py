from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path("", views.index, name = 'index'),
    path('news/<int:post_id>/', views.news_post),
    path("news/", views.main_page),
    path("news/create/", views.create),
]
urlpatterns += static(settings.STATIC_URL)