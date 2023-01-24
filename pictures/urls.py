from django.urls import path

from pictures import views


app_name = 'pictures'
urlpatterns = [
    path('', views.index, name='index'),
    path('upload/', views.upload, name='upload'),
]