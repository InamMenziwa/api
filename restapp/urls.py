from django.urls import path
from . import views

urlpatterns = [
    path('data/', views.Blogcreation.as_view(), name="blogcreation"),
    path('', views.Homepage, name="index")
]