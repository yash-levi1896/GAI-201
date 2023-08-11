from django.urls import path
from . import views

urlpatterns = [
    path('greet', views.hello, name='hello'),
    path('greet/<str:username>', views.hello1, name='hello1'),
    path('farewell/<str:username>', views.hello2, name='hello2'),
    path('create', views.create, name='create'),
    path('read', views.readdata, name='read'),
    path('update', views.UpdateData, name='update'),
    path('delete', views.DeleteData, name='delete'),
    path('', views.Home, name='home'),
]
