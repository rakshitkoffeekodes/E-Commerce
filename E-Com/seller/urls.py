from django.urls import path
from seller import views

urlpatterns = [
    path('', views.register),
    path('login/', views.login),
    path('logout/', views.logout),
    path('profile/', views.profile),
    path('update_profile/', views.update_profile),
]
