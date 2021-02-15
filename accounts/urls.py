from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('',views.index,name="homePage"),
    path('accounts/sign_up/',views.sign_up,name="sign-up")
]