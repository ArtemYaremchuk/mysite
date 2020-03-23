from django.urls import path

from . import views


app_name = 'mainpage'
urlpatterns = [
   #    path(r'', views.index, name='index'),  # (2) далее django переходит сюда, видит index и
    path(r'FAQ/', views.index, name='index'),
    path(r'', views.CarListView.as_view(), )
]
