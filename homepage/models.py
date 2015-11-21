from django.db import models

class Asset(models.Model):
	asset_code = models.TextField(max_length=10, null=True, blank=True)
	description = models.TextField(max_length=255, null=True, blank=True)
	date_acquired = models.DateField(null=True, blank=True)
	pass

class Assignment(Asset):
	location = models.TextField(max_length=30, null=True, blank=True)
	organization_type = models.TextField(max_length=30, null=True, blank=True)
	date_assigned = models.DateField(null=True, blank=True)
	pass

class Manufacturer(Asset):
	manufacturer = models.TextField(max_length=30, null=True, blank=True)
	part_num = models.TextField(max_length=30, null=True, blank=True)
	pass

class Maintenance(Asset):
	maintenance_note = models.TextField(max_length=255, null=True, blank=True)
	pass
