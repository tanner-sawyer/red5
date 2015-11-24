from django.db import models


class Location(models.Model):
	place = models.TextField(max_length=30, null=True, blank=True)


class Manufacturers(models.Model):
	name = models.TextField(max_length=30, null=True, blank=True)


class Asset(models.Model):
	asset_code = models.TextField(max_length=10, unique=True, null=True, blank=True)
	description = models.TextField(max_length=255, null=True, blank=True)
	date_acquired = models.DateField(null=True, blank=True)
	location = models.ForeignKey(Location)
	organization_type = models.TextField(max_length=30, null=True, blank=True)
	date_assigned = models.DateField(null=True, blank=True)
	maintenance_note = models.TextField(max_length=255, null=True, blank=True)
	part_num = models.TextField(max_length=30, null=True, blank=True)
	manufacturer = models.ForeignKey(Manufacturers)
	pass





