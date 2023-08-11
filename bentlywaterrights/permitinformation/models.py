from django.db import models

# Create your models here.
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

	def __str__(self):
		return f"{self.permit_num}, {self.cert_status} , {self.basin}, {self.owner_of_record}"

	class Meta:
		verbose_name_plural = "Properties"


"""
basin
owner_of_record
permit_num
cert_status
priority_date

pod_1
pod_2
pod_3
pod_4
pod_5

unit_acres
unit_sheep
unit_lamb
unit_cattle
unit_horses
unit_other

cfs (Float)
duty_af (Float)
poc_due (varchar(20))
pbu_due (varchar(20))
use (varchar(5))
source (varchar(5))
source_description (varchar(50))
remarks (varchar(50))
sale_value (varchar(100))
potential_values (varchar(150))

"""
