from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='rewives'),  # (2) далее django переходит сюда, видит index и
    path('leave_rewive/', views.leave_rewive),

]