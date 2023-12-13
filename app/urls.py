from django.urls import path
from app import views

urlpatterns = [
    path('', views.index, name='home'),
    path('create/', views.create),
    path('edit/<int:id>/', views.edit),
    path('delete/<int:id>/', views.delete),
]
