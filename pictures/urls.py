from django.urls import path

from pictures import views


app_name = 'pictures'
urlpatterns = [
    path('pictures-function/', views.index, name='function'),
    path('pictures-class/', views.IndexView.as_view(), name='class'),

    path('create-class/', views.CreatePictureView.as_view(), name='create-class'),
    path('create-function/', views.upload, name='create-function'),
]