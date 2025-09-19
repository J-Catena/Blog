from django.urls import path
from . import views

app_name = "posts"

urlpatterns = [
    path("", views.home, name="home"),
    path("categoria/<slug:slug>/", views.category_list, name="category"),
    path("post/<slug:slug>/", views.post_detail, name="detail"),
    path("buscar/", views.search, name="search"),
    path("sobre-mi/", views.about, name="about"),
    path("contacto/", views.contact, name="contact"),
]


