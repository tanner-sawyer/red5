from django.http import HttpRequest, HttpResponseRedirect
from django.contrib.auth import authenticate, login
from django_mako_plus.controller import view_function
import homepage.models as hmod
from django_mako_plus.controller.router import get_renderer
from django.views.decorators.csrf import csrf_exempt
from django import forms

templater = get_renderer('homepage')


@view_function
def process_request(request):
  params = {}

  asset = hmod.Asset.objects.all()

  params['asset'] = asset
  
  return templater.render_to_response(request, 'catalog.html', params)


@view_function
def edit(request):
  params = {}

  try:
    asset = hmod.Asset.objects.get(id=request.urlparams[0])
  except hmod.Asset.DoesNotExist:
    return HttpResponseRedirect('/catalog/')

  location = hmod.Location.objects.get(id=asset.location_id)

  form = AssetForm(initial={
    'asset_code': asset.asset_code,
    'description': asset.description,
    'date_acquired': asset.date_acquired,
    'location': asset.location,
    'organization_type': asset.organization_type,
    'date_assigned': asset.date_assigned,
    'manufacturer': asset.manufacturer,
    'part_num': asset.part_num,
    'maintenance_note': asset.maintenance_note,
  })
  if request.method == 'POST':
    form = AssetForm(request.POST)
    if form.is_valid():
      asset.asset_code = form.cleaned_data['asset_code']
      asset.description = form.cleaned_data['description']
      asset.date_acquired = form.cleaned_data['date_acquired']
      asset.organization_type = form.cleaned_data['organization_type']
      asset.date_assigned = form.cleaned_data['date_assigned']
      asset.part_num = form.cleaned_data['part_num']
      asset.maintenance_note = form.cleaned_data['maintenance_note']
      place = hmod.Location.objects.get(place=form.cleaned_data['location'])
      name = hmod.Manufacturers.objects.get(name=form.cleaned_data['manufacturer'])
      asset.location = place
      asset.manufacturer = name

      asset.save()
      return HttpResponseRedirect('/catalog/')

  params['asset'] = asset
  params['form'] = form
  
  return templater.render_to_response(request, 'catalog.edit.html', params)


@view_function
def create(request):
  params = {}

  a = hmod.Asset.objects.all().order_by("-id")
  if len(a) > 0:
  	if a[0].asset_code == '':
  		return HttpResponseRedirect('/catalog.edit/{}'.format(a[0].id))

  location = hmod.Location.objects.get(id=1)
  manufacturers = hmod.Manufacturers.objects.get(id=1)

  asset = hmod.Asset()
  asset.asset_code = ''
  asset.description = ''
  asset.date_acquired = None
  asset.location = location
  asset.organization_type = ''
  asset.date_assigned = None
  asset.part_num = ''
  asset.manufacturer = manufacturers
  asset.maintenance_note = ''
  asset.save()

  params['asset'] = asset
  
  return HttpResponseRedirect('/catalog.edit/{}'.format(asset.id))


@view_function
def delete(request):
  params = {}

  try:
    asset = hmod.Asset.objects.get(id=request.urlparams[0])
  except hmod.Asset.DoesNotExist:
    return HttpResponseRedirect('/catalog/')

  asset.delete()
 
  return HttpResponseRedirect('/catalog/')


class AssetForm(forms.Form):
  places = hmod.Location.objects.all().values_list('place', flat=True)
  place_choices = [('', 'None')] + [(id, id) for id in places]
  names = hmod.Manufacturers.objects.all().values_list('name',flat=True)
  name_choices = [('', 'None')] + [(id, id) for id in names]

  asset_code = forms.CharField(max_length=10)
  description = forms.CharField(max_length=255)
  date_acquired = forms.DateField()
  location = forms.ChoiceField(place_choices, required=False)
  # location = forms.ModelChoiceField(label='Location', queryset=hmod.Location.objects.all().values_list('place', flat=True), empty_label=None, required=False)
  organization_type = forms.CharField(max_length=30)
  date_assigned = forms.DateField()
  manufacturer = forms.ChoiceField(name_choices, required=False)
  # manufacturer = forms.ModelChoiceField(label='Manufacturer', queryset=hmod.Manufacturers.objects.all().values_list('name', flat=True), empty_label=None, required=False)
  part_num = forms.CharField(max_length=30)
  maintenance_note = forms.CharField(max_length=255)