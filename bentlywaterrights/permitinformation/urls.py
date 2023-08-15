from django.urls import path
from . import views

urlpatterns = [
	path('', views.home, name="home"),
	path('logbook.html', views.logbook, name="logbook"),
	path('about.html', views.about, name="about"),
	path('delete/<property_id>', views.deleteProperty, name="deleteProperty"),
	path('details/<int:property_id>/', views.getPropertyDetails, name='getPropertyDetails'),
]
