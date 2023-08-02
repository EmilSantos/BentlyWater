from django.shortcuts import render

def home(request):

	testResult = "Coming From View"

	return render(request, 'home.html', { 'test':testResult })

def logbook(request):
	return render(request, 'logbook.html', {})

def about(request):
	return render(request, 'about.html', {})