from django.http import HttpRequest
from django.contrib.auth import authenticate, login
from django_mako_plus.controller import view_function
import homepage.models as hmod
from django_mako_plus.controller.router import get_renderer
from django.views.decorators.csrf import csrf_exempt

templater = get_renderer('homepage')


@view_function
def process_request(request):
  params = {}

  asset = hmod.Asset.objects.all()

  params['asset'] = asset
  
  return templater.render_to_response(request, 'catalog.html', params)

