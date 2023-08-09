from django.shortcuts import render, redirect
from .models import Property
from .forms import PropertyForm
from django.contrib import messages

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


def logbook(request):
	return render(request, 'logbook.html', {})

def about(request):
	return render(request, 'about.html', {})