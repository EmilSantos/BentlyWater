from django import forms
from .models import Property

class PropertyForm(forms.ModelForm):
	BASIN_CHOICES = [
		("", "Choose..."),
		("Lake Tahoe Basin (90)", "Lake Tahoe Basin (90)"),
		("Dayton Valley (103)", "Dayton Valley (103)"),
		("Carson Valley (105)", "Carson Valley (105)"),
		("Antelope Valley (106)", "Antelope Valley (106)"),
		]

	basin = forms.ChoiceField(choices=BASIN_CHOICES, required=True, label="Basin", widget=forms.Select(attrs={'class': 'form-control'}))
	owner_of_record = forms.CharField(max_length=50, required=True, label="Owner of Record", widget=forms.TextInput(attrs={'class': 'form-control'}))
	permit_num = forms.CharField(max_length=20, required=True, label="Permit Number", widget=forms.TextInput(attrs={'class': 'form-control'}))
	cert_status = forms.CharField(max_length=20, required=True, label="Certification/Status", widget=forms.TextInput(attrs={'class': 'form-control'}))

	priority_date = forms.DateField(required=True, label="Priority Date", widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}))
	cfs = forms.CharField(max_length=20, required=False, label="C.F.S.", widget=forms.TextInput(attrs={'class': 'form-control'}))
	duty_af = forms.CharField(max_length=20, required=False, label="Duty (AF)", widget=forms.TextInput(attrs={'class': 'form-control'}))
	use = forms.CharField(max_length=10, required=False, label="Use", widget=forms.TextInput(attrs={'class': 'form-control'}))
	remarks = forms.CharField(max_length=150, required=False, label="Remarks",widget=forms.TextInput(attrs={'class': 'form-control'}))

	poc_due = forms.DateField(required=False, label="POC Due", widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}))
	pbu_due = forms.DateField(required=False, label="PBU Due", widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}))
	source = forms.CharField(max_length=10, required=False, label="Source",widget=forms.TextInput(attrs={'class': 'form-control'}))
	source_description = forms.CharField(max_length=50, required=False, label="Source Description",widget=forms.TextInput(attrs={'class': 'form-control'}))

	sale_value = forms.CharField(max_length=150, required=False, label="Sale Value", widget=forms.TextInput(attrs={'class': 'form-control'}))
	potential_values = forms.CharField(max_length=150, required=False, label="Potential Values", widget=forms.TextInput(attrs={'class': 'form-control'}))
	pod_1 = forms.CharField(max_length=10, required=False, label="1/4", widget=forms.TextInput(attrs={'class': 'form-control'}))
	pod_2 = forms.CharField(max_length=10, required=False, label="1/4", widget=forms.TextInput(attrs={'class': 'form-control'}))
	pod_3 = forms.CharField(max_length=10, required=False, label="S", widget=forms.TextInput(attrs={'class': 'form-control'}))
	pod_4 = forms.CharField(max_length=10, required=False, label="T(N)", widget=forms.TextInput(attrs={'class': 'form-control'}))
	pod_5 = forms.CharField(max_length=10, required=False, label="R", widget=forms.TextInput(attrs={'class': 'form-control'}))

	unit_acres = forms.CharField(required=False, label="Acres", widget=forms.TextInput(attrs={'class': 'form-control'}))
	unit_sheep = forms.IntegerField(required=False, label="Sheep", widget=forms.NumberInput(attrs={'class': 'form-control'}))
	unit_lamb = forms.IntegerField(required=False, label="Lamb", widget=forms.NumberInput(attrs={'class': 'form-control'}))
	unit_cattle = forms.IntegerField(required=False, label="Cattle", widget=forms.NumberInput(attrs={'class': 'form-control'}))
	unit_horses = forms.IntegerField(required=False, label="Horses", widget=forms.NumberInput(attrs={'class': 'form-control'}))
	unit_other = forms.CharField(max_length=150, required=False, label="Other", widget=forms.TextInput(attrs={'class': 'form-control'}))
	
	class Meta:
		model = Property
		fields = ["basin", "owner_of_record", "permit_num", "cert_status", "priority_date", "pod_1", "pod_2", "pod_3", "pod_4", "pod_5", 
		"unit_acres", "unit_sheep", "unit_lamb", "unit_cattle", "unit_horses", "unit_other", "cfs", "duty_af", "poc_due", "pbu_due", 
		"use", "source", "source_description", "remarks", "sale_value", "potential_values", "created_by", "modified_by"]


