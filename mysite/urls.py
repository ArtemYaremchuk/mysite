"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('mainpage.urls')),# django начинает сначала здесь(1)
    path('Volkswagen_Touareg/', include('mainpage.urls')),
    path('Volkswagen_Golf_R_2017/', include('mainpage.urls')),
    path('Mitsubishi_Lancer_2015/', include('mainpage.urls')),
    path('Mitsubishi_Outlander/', include('mainpage.urls')),
    path('Toyota_Corolla_2016/', include('mainpage.urls')),
    path('Chevrolet_Cruze/', include('mainpage.urls')),
    path('rewives/', include('rewives.urls')),
    path('grappelli/', include('grappelli.urls')),  # grappelli admin_style URLS
    path('admin/', admin.site.urls),
]
