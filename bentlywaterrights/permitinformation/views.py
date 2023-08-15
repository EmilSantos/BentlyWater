from django.shortcuts import render, redirect
from .models import Property
from .forms import PropertyForm
from django.contrib import messages
from django.http import JsonResponse

def home(request):
	PropertyDict = {}
	if request.method == "POST":
		form = PropertyForm(request.POST or None)

		if form.is_valid():
			form.save()
			messages.success(request, ("Property has been added"))
			return redirect('home')

	else:
		ticker = Property.objects.all()
		return render(request, 'home.html', {'ticker': ticker})

def deleteProperty(request, property_id):
	item = Property.objects.get(pk=property_id)
	item.delete()
	messages.success(request, ("Property has been deleted"))
	return redirect('home')

def getPropertyDetails(request, property_id):
    item = Property.objects.get(pk=property_id)

    details = {
        'permit_num': item.permit_num,
        'basin': item.basin,
        'cert_status': item.cert_status,
        'owner_of_record': item.owner_of_record,
    }
    return JsonResponse(details)

def logbook(request):
	return render(request, 'logbook.html', {})

def about(request):
	return render(request, 'about.html', {})