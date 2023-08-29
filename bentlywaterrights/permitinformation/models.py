from django.db import models
from django.db.models.signals import post_save, post_delete, pre_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from django.contrib import admin


class Property(models.Model):
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

	unit_acres = models.CharField('Acres', max_length=10, blank=True, null=True) #FloatField?
	unit_sheep = models.IntegerField('Sheep', blank=True, null=True)
	unit_lamb = models.IntegerField('Lamb', blank=True, null=True)
	unit_cattle = models.IntegerField('Cattle', blank=True, null=True)
	unit_horses = models.IntegerField('Horses', blank=True, null=True)
	unit_other = models.CharField('Other', max_length=100, blank=True)

	cfs = models.CharField('C.F.S.', max_length=10, blank=True, null=True) #FloatField?
	duty_af = models.CharField('Duty (AF)', max_length=10, blank=True, null=True) #FloatField?
	poc_due = models.DateField('POC Due', blank=True, null=True)
	pbu_due = models.DateField('PBU Due', blank=True, null=True)
	use = models.CharField('Use', max_length=10, blank=True)
	source = models.CharField('Source', max_length=10, blank=True)
	source_description = models.CharField('Source Description', max_length=50, blank=True)
	remarks = models.CharField('Remarks', max_length=150, blank=True)
	sale_value = models.CharField('Sale Value', max_length=150, blank=True)
	potential_values = models.CharField('Potential Value', max_length=150, blank=True)
	user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

	created_by = models.CharField('', max_length=50, blank=True)
	modified_by = models.CharField('', max_length=50, blank=True)
	create_date = models.DateTimeField('', auto_now_add=True)
	modify_date = models.DateTimeField('', auto_now=True)

	def __str__(self):
		return f"{self.permit_num}, {self.cert_status} , {self.basin}, {self.owner_of_record}"

	class Meta:
		verbose_name_plural = "Properties"


class AuditLog(models.Model):
	property = models.ForeignKey(Property, on_delete=models.CASCADE, related_name='audit_logs')
	user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True) # User who made the change
	field_name = models.CharField(max_length=255) # Name of the field that was changed
	old_value = models.TextField(null=True, blank=True) # Previous value of the field
	new_value = models.TextField(null=True, blank=True) # New value of the field
	changed_at = models.DateTimeField(auto_now_add=True) # Timestamp of when the change occurred


@receiver(post_save, sender=Property)
def create_update_audit_log(sender, instance, created, **kwargs):
	EXCLUDED_FIELDS = ['user']
	print("Signal Triggered!")
	user = getattr(instance, 'user', None)
	if created:
		print("Instance Created!")
		AuditLog.objects.create(
        	property=instance,
        	user=user,
        	field_name="Created",
        	new_value=str(instance)
        )
	else:
		#print("Checking for field updates...")
		old_instance = getattr(instance, "_old_instance", None)
		if old_instance:
			for field in instance._meta.fields:
				if field.name not in EXCLUDED_FIELDS and field.verbose_name:
					old_value = getattr(old_instance, field.name)
					new_value = getattr(instance, field.name)
					print(f"Field: {field.name}, Old Value: {old_value}, New Value: {new_value}")
					if old_value != new_value:
						print(f"Field {field.name} has changed.")
						AuditLog.objects.create(
							property=instance,
							user=user,
							field_name=field.verbose_name,
							old_value=str(old_value),
							new_value=str(new_value)
							)

@receiver(pre_save, sender=Property)
def capture_old_instance(sender, instance, **kwargs):
	if instance.pk:
		try:
			instance._old_instance = Property.objects.get(pk=instance.pk)
		except Property.DoesNotExist:
			instance._old_instance = None










