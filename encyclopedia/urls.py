from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("edit/", views.edit, name="edit"),
    path("wiki/<str:title>", views.entry, name="entry"),
    path("search/", views.search, name="query"),
    path("random-page/", views.random_page, name="random_page"),
    path("new-page/", views.new_page, name="new_page")
]
