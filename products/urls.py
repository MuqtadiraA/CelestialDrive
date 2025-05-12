from django.urls import path, include
from products import views
from products.views import signup_view


urlpatterns = [
    path('', views.index, name="index"),
    path("about/", views.about, name="about"),
    path("signin/", views.signin, name="log"),
    path('contact/', views.contact_view, name='contact'),
    path("signup/", views.signup_view, name="signup"),
    path("signin/", views.signin, name="signin"),




  # Car pages
    path('cars/car1/', views.car1, name='car1'),
    path('cars/car2/', views.car2, name='car2'),
    path('cars/car3/', views.car3, name='car3'),
    path('cars/car4/', views.car4, name='car4'),
    path('cars/car5/', views.car5, name='car5'),
    path('cars/car6/', views.car6, name='car6'),
    path('cars/car7/', views.car7, name='car7'),
    path('cars/car8/', views.car8, name='car8'),
    path('cars/car9/', views.car9, name='car9'),
    path('cars/car10/', views.car10, name='car10'),

]