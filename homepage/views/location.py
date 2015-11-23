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

  location = hmod.Location.objects.all()

  params['location'] = location
  
  return templater.render_to_response(request, 'location.html', params)


@view_function
def edit(request):
  params = {}

  try:
    location = hmod.Location.objects.get(id=request.urlparams[0])
  except hmod.Location.DoesNotExist:
    return HttpResponseRedirect('/location/')

  form = LocForm(initial={
    'place': location.place,
  })
  if request.method == 'POST':
    form = LocForm(request.POST)
    if form.is_valid():
      location.place = form.cleaned_data['place']
      location.save()
      return HttpResponseRedirect('/location/')

  params['location'] = location
  params['form'] = form
  
  return templater.render_to_response(request, 'location.edit.html', params)


@view_function
def create(request):
  params = {}

  a = hmod.Location.objects.all().order_by("-id")
  if len(a) > 0:
  	if a[0].id == '':
  		return HttpResponseRedirect('/location.edit/{}'.format(a[0].id))

  location = hmod.Location()
  location.place = ''
  location.save()

  params['location'] = location
  
  return HttpResponseRedirect('/location.edit/{}'.format(location.id))


@view_function
def delete(request):
  params = {}

  try:
    location = hmod.Location.objects.get(id=request.urlparams[0])
  except hmod.Location.DoesNotExist:
    return HttpResponseRedirect('/location/')

  location.delete()
 
  return HttpResponseRedirect('/location/')


class LocForm(forms.Form):
  place = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}),max_length=255)