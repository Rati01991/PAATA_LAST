from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('car/<int:car_id>/', views.car_details, name='car_details'),
    path('add_car/', views.add_car, name='add_car'),
    path('search/', views.search_cars, name='search_cars'),
    path('', views.home, name='home'),
    path('submit-car/', views.submit_car, name='submit_car'),
    path('submit-car/', views.submit_car, name='submit_car'),
    path('update-car/<int:car_id>/', views.update_car, name='update_car'),
    path('delete-car/<int:car_id>/', views.delete_car, name='delete_car'),
    # Other URL patterns if any
]