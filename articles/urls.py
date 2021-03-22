from django.urls import path
from . import views as views

app_name = "articles"

urlpatterns = [
    path("announce/", views.announce, name="announce"),
    path("news/", views.news, name="news"),    
    path("<int:pk>", views.detail, name="detail")
]