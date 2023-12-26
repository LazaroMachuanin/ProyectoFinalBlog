from .models import Usuario
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth import authenticate, login as auth_login


class RegistroUsuarioForm(UserCreationForm):
    
    class Meta:
        model = Usuario
        fields = ['username', 'first_name', 'last_name', 'password1', 'password2', 'email', 'imagen']
        
        
class LoginForm(forms.Form):
    username = forms.CharField(label='Nombre de usuario')
    password = forms.CharField(label= 'Contraseña', widget=forms.PasswordInput)
    '''
    def login(self, request):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
        '''
    def login_user(self, request):  # Cambié el nombre de la función
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        user = authenticate(request, username=username, password=password)
        if user:
            auth_login(request, user)  # Usé el nombre importado para la función de login
            return user  # Retorna el usuario autenticado
        return None  # Retorna None si la autenticación falla
