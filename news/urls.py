from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('news', views.allnews, name="news"),
    path('news/<int:id>/', views.article, name="article"),
    path('news/categories', views.allcategories, name="categories"),
]
