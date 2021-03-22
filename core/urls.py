from django.urls import path
from . import views as views

app_name = "core"

urlpatterns = [
    path("", views.home, name="home"),
    path("policy/", views.policy, name="policy"),
    path("purpose/", views.purpose, name="purpose"),
    path("donation_status/", views.donation_status, name="donation_status"),
]
