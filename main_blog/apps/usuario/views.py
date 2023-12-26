from .forms import RegistroUsuarioForm
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import CreateView
from django.contrib import messages
from django.urls import reverse_lazy  # Usar reverse_lazy en vez de reverse
from django.shortcuts import redirect
from django.contrib.auth import logout
from django.contrib.auth.views import PasswordResetView
from django.contrib.auth.views import PasswordChangeDoneView
from django.contrib.auth.models import Group

class RegistrarUsuario(CreateView):
    template_name = 'registration/registrar.html'
    form_class = RegistroUsuarioForm
    
    def form_valid(self, form):
        #response= super().form_valid(form)
        messages.success(self.request, 'Registro exitoso. Por favor inicia sesión.')
        #group= Group.objects.get(name='Registrado')
        #self.objects.groups.add(group)
        #return redirect('apps.usuario:registrar')
        form.save()
        return redirect('apps.usuario:login')


class LoginUsuario(LoginView):
    template_name = 'registration/login.html'
    
    def get_success_url(self):
        #messages.success(self.request, 'Login exitoso')
        return reverse_lazy('index')  # Cambiar a reverse_lazy
    

    #def sign_out(request):
    #    logout(request)
    #    return redirect ('login')

def sign_out(request):
    logout(request)
    #return redirect('apps.usuario:login')
    return redirect('index')

'''
class LogoutUsuario(LogoutView):
    template_name = 'registration/logout.html'
    
    def get_next_page(self):
        return reverse_lazy('apps.usuario:logout')  # Cambiar a reverse_lazy

'''

'''
#from django.forms.models import BaseModelForm
#from django.http import HttpResponse
from .forms import RegistroUsuarioForm
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import CreateView
from django.contrib import messages
from django.contrib.auth import logout
from django.shortcuts import redirect
from django.urls import reverse



# Create your views here.

class RegistrarUsuario(CreateView):
    template_name = 'registration/registrar.html'
    form_class = RegistroUsuarioForm
    
    def form_valid(self, form):
        messages.success(self.request, 'Registro exitoso. Por favor inicia sesion.')
        form.save()
        
        return redirect('apps.usuario:registrar')
    
class LoginUsuario(LoginView):
    template_name = 'registration/login.html'
    
    def get_success_url(self):
        messages.success(self.request, 'Login exitoso')
        
        return reverse('apps.usuario:login')
    
class LogoutUsuario(LogoutView):
    template_name = 'registration/logout.html'
    
    def get_success_url(self):
        messages.success(self.request, 'Logout exitoso')
        return reverse('apps.usuario:logout')
'''

