from django.urls import path
from .import views

urlpatterns= [
    path('', views.home, name='home'),
    path('appetizer/', views.appetizer, name='appetizer'),
    path('management/', views.management, name='management'),
    path('orders/', views.orders, name='orders'),
    path('bookings/', views.bookings, name='bookings'),
    path('staff/', views.staff, name='staff'),
    path('timetable/',views.timetable, name='timetable'),
    path('reservation_form/', views.reservation_form, name='reservation_form'),
    path('reservation_success/', views.reservation_success,  name='reservation_success'),
]