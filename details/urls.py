from django.urls import path
from .import views

urlpatterns= [
    path('', views.show_categories, name='show_categories'),
    path('home', views.home, name='home'),
    path('appetizer/', views.appetizer, name='appetizer'),
    path('management/', views.management, name='management'),
    path('orders/', views.orders, name='orders'),
    path('bookings/', views.bookings, name='bookings'),
    path('staff/', views.staff, name='staff'),
    path('timetable/',views.timetable, name='timetable'),
    path('reservation_form/', views.reservation_form, name='reservation_form'),
    path('reservation_success/', views.reservation_success,  name='reservation_success'),
    path('policies/', views.policies,name='policies'),
    path('feedback/', views.feedback, name='feedback'),
    path('main/', views.main, name='main'),
    path('dessert/', views.dessert, name='dessert'),


    # testing dynamic rendering of models
    # path('categories/', views.show_categories, name='show_categories'),
    path('items/', views.show_items, name='show_items'),
    path('items/<int:category_id>/', views.show_items_by_category, name='show_items_by_category'),
]