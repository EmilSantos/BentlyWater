from django.shortcuts import render, redirect
from .models import Property, AuditLog
from .forms import PropertyForm
from django.contrib import messages
from django.http import JsonResponse
from datetime import datetime
from django.urls import reverse

def home(request):
	PropertyDict = {}
	if request.method == "POST":
		form = PropertyForm(request.POST or None)

		if form.is_valid():
			property_instance = form.save(commit=False)
			property_instance.user = request.user if request.user.is_authenticated else None
			property_instance.save()

			messages.success(request, ("Property has been added"))
			return redirect('home')
		else:
			propertyListing = Property.objects.all()
			return render(request, 'home.html', {'propertyListing': propertyListing, 'form': form})
	else:
		propertyListing = Property.objects.all()
		form = PropertyForm()  # Initialize an empty form
		return render(request, 'home.html', {'propertyListing': propertyListing, 'form': form})

def getPropertyDetails(request, property_id):
    item = Property.objects.get(pk=property_id)
    if request.method == "POST":
    	form = PropertyForm(request.POST, instance=item)
    	if form.is_valid():
    		property_instance = form.save(commit=False)
    		if request.user.is_authenticated:
    			print(f"Logged in user: {request.user.username}")
    			property_instance.user = request.user
    		else:
    			print("user not authenticated!")
    			property_instance.user = None
    		property_instance.save()
    		
    		messages.success(request, "Property has been updated!")
    		return redirect(reverse('getPropertyDetails', args=[item.id])) 
    else:
    	form = PropertyForm(instance=item)
    return render(request, 'rights_detail.html', {'item': item, 'form': form})

def edit_rights(request, property_id):
	item = Property.objects.get(pk=property_id)
	return render(request, 'edit_rights.html', {'item': item})

def logbook(request):
	logs = AuditLog.objects.all()
	return render(request, 'logbook.html', {'logs': logs})

def about(request):
	return render(request, 'about.html', {})

def deleteProperty(request, property_id):
	item = Property.objects.get(pk=property_id)
	item.delete()
	messages.success(request, ("Property has been deleted"))
	return redirect('home')
