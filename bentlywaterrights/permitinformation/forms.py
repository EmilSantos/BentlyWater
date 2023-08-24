from django import forms
from .models import Property

class PropertyForm(forms.ModelForm):
	use = forms.CharField(max_length=5, widget=forms.TextInput(attrs={'maxlength': '5'}))

	class Meta:
		model = Property
		fields = ["basin", "owner_of_record", "permit_num", "cert_status", "priority_date", "pod_1", "pod_2", "pod_3", "pod_4", "pod_5", 
		"unit_acres", "unit_sheep", "unit_lamb", "unit_cattle", "unit_horses", "unit_other", "cfs", "duty_af", "poc_due", "pbu_due", 
		"use", "source", "source_description", "remarks", "sale_value", "potential_values", "created_by", "modified_by"]


