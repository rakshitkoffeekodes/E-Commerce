from django.urls import path
from seller import views

urlpatterns = [
    path('', views.register),
    path('login/', views.login),
    path('logout/', views.logout),
    path('profile/', views.profile),
    path('update_profile/', views.update_profile),
    path('add_product/', views.add_product),
    path('view_all_product/', views.view_all_product),
    path('update_product/', views.update_product),
    path('delete_product/', views.delete_product),
]
