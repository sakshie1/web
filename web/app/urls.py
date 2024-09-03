from django.urls import path,include
from . import views


urlpatterns = [
    path('',views.index,name='index'),
    path('read',views.read,name='read'),
    path('display_json',views.display_json,name='display_json'),
]
