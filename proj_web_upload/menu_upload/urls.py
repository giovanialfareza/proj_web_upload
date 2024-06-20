from django.urls import path # type: ignore
from . import views

urlpatterns = [
    path('', views.upload_photo, name='upload_photo'),
    path('success/', views.upload_success, name='upload_success'),
    path('photos/', views.photo_list, name='photo_list'),
]