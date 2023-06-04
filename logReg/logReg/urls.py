"""logReg URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from sre_constants import SUCCESS
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('Registration/', views.userreg,name="regis"),
    path('home/',views.home_page,name="Home"),
    path('reg/', views.show,name="Reg"),
    path('Logout/', views.logout,name="Logout"),
    path('sample/', views.sample,name="sample"),
    path('success/', views.thankyou),
    path('success1/', views.sub),
    path('sample/test/', views.test,name="test"),   
    path('sample/recent/', views.recent,name="recent"),   
]
