from django.conf import settings
from django import forms
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.http import HttpRequest
from django.contrib.auth import authenticate, login
from django_mako_plus.controller import view_function
import homepage.models as hmod
from django_mako_plus.controller.router import get_renderer
from django.views.decorators.csrf import csrf_exempt
from ldap3 import Server, Connection, AUTH_SIMPLE, STRATEGY_SYNC,GET_ALL_INFO

templater = get_renderer('homepage')


@view_function
def process_request(request):
  params = {}
  
  return templater.render_to_response(request, 'index.html', params)

@view_function
def loginform(request):
  params = {}

  form = LoginForm()
  params['form'] = form
  if request.method == 'POST':
    form = LoginForm(request.POST)
    if form.is_valid():
      username = form.cleaned_data['username']
      password = form.cleaned_data['password']
      try:
        s = Server('www.thecolonialheritage.com', port=8889, get_info=GET_ALL_INFO)
        c = Connection(s, auto_bind=True, client_strategy=STRATEGY_SYNC, user=username, password=password, authentication=AUTH_SIMPLE)

        if c:
          hmod.User.objects.get_or_create(username="Jordan")
          u = hmod.User.objects.get(username="Jordan")
          u.first_name = "Jordan"
          u.last_name = "Rader"
          u.set_password(password)
          u.save()
          u2 = authenticate(username="Jordan",password=password)
          login(request, u2)
          return HttpResponse('''<script>window.location.href = "/homepage/account/";</script>''')
      except:
        user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
        login(request, user)
        return HttpResponse('''<script>window.location.href = "/homepage/account/";</script>''')

  return templater.render_to_response(request, 'index.loginform.html', params)

class LoginForm(forms.Form):
  username = forms.CharField()
  password = forms.CharField(label='Password', widget=forms.PasswordInput)

  def clean(self):
    return self.cleaned_data