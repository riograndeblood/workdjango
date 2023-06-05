"""
URL configuration for prodjango project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from .views import first,second
from books.views import books, get_book, get_genre_books
from PostTag.views import PostTag, get_post, get_posttag_posts


urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', first),
    path('list/', second),
    path('get_books/', books, name="books"),
    path("get_books/<int:id>/", get_book, name="get_book"),
    path("get_genre/<str:title>/", get_genre_books, name="get_genre"),
    path('get_posts/', PostTag, name="PostTag"),
    path("get_posts/<int:id>/", get_post, name="get_post"),
    path("get_tag/<str:title>/", get_posttag_posts, name="get_tag")

]
