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
			if request.user.is_authenticated:
				property_instance.user = request.user
			else:
				property_instance.user = None
			property_instance.save()

			messages.success(request, ("Property has been added"))
			return redirect('home')
		else:
			ticker = Property.objects.all()
			return render(request, 'home.html', {'ticker': ticker, 'form': form})
	else:
		ticker = Property.objects.all()
		form = PropertyForm()  # Initialize an empty form
		return render(request, 'home.html', {'ticker': ticker, 'form': form})





def getPropertyDetails(request, property_id):
    #try:
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
    		return redirect(reverse('getPropertyDetails', args=[item.id]))  # Change 'some_url_name' to the desired redirect URL
    else:
    	form = PropertyForm(instance=item)
    return render(request, 'rights_detail.html', {'item': item, 'form': form})

    #except Property.DoesNotExist:
    #    return JsonResponse({"error": "Property not found"}, status=404)

    #except Exception as e:
        # You might want to log the exception for debugging
        #return JsonResponse({"error": "An error occurred"}, status=500)

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
'''
	basin = models.CharField('Basin', max_length=50)
	owner_of_record = models.CharField('Owner of Record', max_length=50)
	permit_num = models.CharField('Permit Number', max_length=20)
	cert_status = models.CharField('Cert./Status', max_length=20, blank=True)
	priority_date = models.DateField('Priority Date', blank=True, null=True)

	pod_1 = models.CharField('PoE 1/4', max_length=10, blank=True)
	pod_2 = models.CharField('PoE 1/4', max_length=10, blank=True)
	pod_3 = models.CharField('PoE S', max_length=10, blank=True)
	pod_4 = models.CharField('PoE T(N)', max_length=10, blank=True)
	pod_5 = models.CharField('PoE R', max_length=10, blank=True)

	unit_acres = models.IntegerField('Acres', blank=True, null=True)
	unit_sheep = models.IntegerField('Sheep', blank=True, null=True)
	unit_lamb = models.IntegerField('Lamb', blank=True, null=True)
	unit_cattle = models.IntegerField('Cattle', blank=True, null=True)
	unit_horses = models.IntegerField('Horses', blank=True, null=True)
	unit_other = models.CharField('Other', max_length=30, blank=True)

	cfs = models.FloatField('C.F.S.', blank=True, null=True)
	duty_af = models.FloatField('Duty (AF)', blank=True, null=True)
	poc_due = models.DateField('POC Due', blank=True, null=True)
	pbu_due = models.DateField('PBU Due', blank=True, null=True)
	use = models.CharField('Use', max_length=5, blank=True)
	source = models.CharField('Source', max_length=5, blank=True)
	source_description = models.CharField('Source Description', max_length=50, blank=True)
	remarks = models.CharField('Remarks', max_length=50, blank=True)
	sale_value = models.CharField('Sale Value', max_length=100, blank=True)
	potential_values = models.CharField('Potential Value', max_length=150, blank=True)

	created_by = models.CharField('', max_length=50, blank=True)
	modified_by = models.CharField('', max_length=50, blank=True)
	create_date = models.DateTimeField('', auto_now_add=True)
	modify_date = models.DateTimeField('', auto_now=True)
'''