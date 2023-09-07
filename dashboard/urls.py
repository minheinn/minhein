from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.dashboard, name="dashboard"),

    ##About
    path('about/', views.about, name="about"),
    path('about/<str:pk>/delete/', views.aboutDelete, name="about_delete"),
]
