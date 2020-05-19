from django.urls import path
from . import views


app_name = 'mainpage'
urlpatterns = [
     path(r'', views.index, name='index'),  # (2) далее django переходит сюда, видит index и
     path(r'FAQ/', views.faq, name='faq'),
     path(r'contacts/', views.contacts, name='contacts'),
     path(r'Volkswagen_Touareg/', views.Volkswagen_Touareg, name='Volkswagen Touareg'),
     path(r'Volkswagen_Golf_R_2017/', views.volkswagen_golf_r_2017, name='Volkswagen Golf R 2017'),
     path(r'Mitsubishi_Lancer_2015/', views.mitsubishi_lancer_2015, name='Mitsubishi Lancer 2015'),
     path(r'Mitsubishi_Outlander/', views.mitsubishi_outlander, name='Mitsubishi Outlander'),
     path(r'Toyota_Corolla_2016/', views.toyota_corolla_2016, name='Toyota Corolla 2016'),
     path(r'Chevrolet_Cruze/', views.chevrolet_cruze, name='Chevrolet Cruze'),
     path('rental_take_car/', views.rental_take_car),

]
