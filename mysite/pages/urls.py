from django.urls import path
from . import views
# from news import views as news_views


urlpatterns = [
    # path("news/", news_views.news_list, name="news_list"),
    path("", views.home, name="home"),
    path("<slug:slug>/", views.page_detail, name="page_detail"),
]
