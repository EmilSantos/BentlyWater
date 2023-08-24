from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
	path('', views.home, name="home"),
	path('logbook.html', views.logbook, name="logbook"),
	path('about.html', views.about, name="about"),
	path('delete/<property_id>', views.deleteProperty, name="deleteProperty"),
	path('rights_detail.html/<property_id>/', views.getPropertyDetails, name='getPropertyDetails'),
	path('edit_rights.html/<property_id>/', views.edit_rights, name='edit_rights'),
]
