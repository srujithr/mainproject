"""
URL configuration for carrental project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path
from rentalapps import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('user_register',views.user_register),
    path('user_login',views.user_login),
    path('company_register',views.company_register),
    path('add_car',views.add_car, name='add_car'),
    path('',views.indexs,name="indexs"),
    path('service',views.services),
    path('user_page',views.user_page),
    path('cars',views.cars),
    path('details',views.details),
    path('contacts',views.contacts),
    path('bookings',views.bookings),
    path('abouts',views.abouts),
    path('update_company',views.update_company),
    path('view_user',views.view_user),
    path('logout',views.logout),
    # path('profile',views.profile),
    path('view_car',views.view_car),
]
