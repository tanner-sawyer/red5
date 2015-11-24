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

  manufacturer = hmod.Manufacturers.objects.all()

  params['manufacturer'] = manufacturer
  
  return templater.render_to_response(request, 'manufacturer.html', params)

@view_function
def edit(request):
  params = {}

  try:
    manufacturer = hmod.Manufacturers.objects.get(id=request.urlparams[0])
  except hmod.Manufacturers.DoesNotExist:
    return HttpResponseRedirect('/catalog/')

  form = ManForm(initial={
    'name': manufacturer.name,
  })
  if request.method == 'POST':
    form = ManForm(request.POST)
    if form.is_valid():
      manufacturer.name = form.cleaned_data['name']
      manufacturer.save()
      return HttpResponseRedirect('/catalog/')

  params['manufacturer'] = manufacturer
  params['form'] = form
  
  return templater.render_to_response(request, 'manufacturer.edit.html', params)


@view_function
def create(request):
  params = {}

  a = hmod.Manufacturers.objects.all().order_by("-id")
  if len(a) > 0:
  	if a[0].name == '':
  		return HttpResponseRedirect('/manufacturer.edit/{}'.format(a[0].id))

  manufacturer = hmod.Manufacturers()
  manufacturer.name = ''
  manufacturer.save()

  params['manufacturer'] = manufacturer
  
  return HttpResponseRedirect('/manufacturer.edit/{}'.format(manufacturer.id))


@view_function
def delete(request):
  params = {}

  try:
    manufacturer = hmod.Manufacturers.objects.get(id=request.urlparams[0])
  except hmod.Manufacturers.DoesNotExist:
    return HttpResponseRedirect('/manufacturer/')

  manufacturer.delete()
 
  return HttpResponseRedirect('/manufacturer/')


class ManForm(forms.Form):
  name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}),max_length=255)