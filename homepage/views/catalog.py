from django.http import HttpRequest, HttpResponseRedirect
from django.contrib.auth import authenticate, login
from django_mako_plus.controller import view_function
import homepage.models as hmod
from django_mako_plus.controller.router import get_renderer
from django.views.decorators.csrf import csrf_exempt
from django.core.exceptions import ValidationError
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
      place = hmod.Location.objects.get(id=form.cleaned_data['location'])
      name = hmod.Manufacturers.objects.get(id=form.cleaned_data['manufacturer'])
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


def getChoices():
  choice_list = list(hmod.Location.objects.values_list('id','place'))
  return choice_list

def getMan():
  choice_list = list(hmod.Manufacturers.objects.values_list('id','name'))
  return choice_list

class AssetForm(forms.Form):

  def __init__(self, *args, **kwargs):
    super(AssetForm, self).__init__(*args, **kwargs)
    self.fields['location'].choices = getChoices()
    self.fields['manufacturer'].choices = getMan()

  asset_code = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}),min_length=10,max_length=10)
  description = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}),max_length=255)
  date_acquired = forms.DateField(widget=forms.TextInput(attrs={'class': 'form-control'}))
  location = forms.ChoiceField(required=False)
  organization_type = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}),max_length=30)
  date_assigned = forms.DateField(widget=forms.TextInput(attrs={'class': 'form-control'}))
  manufacturer = forms.ChoiceField(label='Manufacturer', required=False)
  part_num = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}),max_length=30)
  maintenance_note = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}),max_length=255)
  def clean_asset_code(self):
    asset_code = self.cleaned_data['asset_code']
    if hmod.Asset.objects.filter(asset_code=asset_code).count() > 0:
        raise ValidationError('This display name is already in use.')
    return asset_code

