from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.dashboard, name="dashboard"),

    ##About
    path('about/', views.about, name="about"),
    path('about/<slug:slug>/delete/', views.aboutDelete, name="about_delete"),

    ## type_writer
    path('type_writer/', views.type_writer, name="type-writer"),
    path('type_writer/<slug:slug>/edit/', views.type_writer_edit, name="type-writer-edit"),
    path('type_writer/<slug:slug>/delete/', views.type_writer_delete, name="type-writer-delete"),
]
