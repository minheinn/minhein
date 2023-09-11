from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.dashboard, name="dashboard"),

    ##About
    path('about/', views.about, name="about"),
    path('about/<str:pk>/delete/', views.aboutDelete, name="about_delete"),

    ## type_writer
    path('type_writer/', views.type_writer, name="type-writer"),
    path('type_writer/<str:pk>/edit/', views.type_writer_edit, name="type-writer-edit"),
    path('type_writer/<str:pk>/delete/', views.type_writer_delete, name="type-writer-delete"),
]
