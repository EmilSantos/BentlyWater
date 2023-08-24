from django.contrib import admin
from .models import Property, AuditLog
# Register your models here.

admin.site.register(Property)

@admin.register(AuditLog)
class AuditLogAdmin(admin.ModelAdmin):
	list_display = ('property', 'user', 'field_name', 'old_value', 'new_value', 'changed_at')
	search_fields = ('property__id', 'user__username', 'field_name')
	list_filter = ('changed_at',)