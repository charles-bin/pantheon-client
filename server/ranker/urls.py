from django.conf.urls import url
from ranker import views

urlpatterns = [
    url(r'^mangas/$', views.MangaList.as_view()),
    url(r'^mangas/(?P<pk>[0-9]+)/$', views.MangaDetail.as_view()),
    ]