from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('', views.home),
    path('about', views.about),
    path('add_appointment', views.add_appointment),
    path('book_test', views.book_test),
    path('all_appointments', views.all_appointments),
    path('delete/<int:id>', views.delete),
    path('health_checkup', views.health_checkup),
    path('view_spcilaists/<int:id>', views.view_specialists),
    
]
