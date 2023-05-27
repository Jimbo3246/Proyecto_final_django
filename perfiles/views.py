from django.shortcuts import *
from django.urls import reverse
from perfiles.forms import UserRegisterForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LogoutView
from django.contrib.auth import login, authenticate

# Create your views here.
def registro(request):
    if request.method == "POST":
        formulario = UserRegisterForm(request.POST)

        if formulario.is_valid():
            formulario.save() #Esto lo puedo usar porque es un model form
            url_exitosa = reverse('inicio')
            return redirect(url_exitosa)
    else:
        formulario = UserRegisterForm()
    return render(
        request= request,
        template_name='perfiles/registro.html',
        context={'form':formulario}
    )
def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid(): 
            data = form.cleaned_data
            usuario = data.get('username')
            password = data.get('password')
            user = authenticate(username=usuario, password=password)

            if user:
                login(request=request, user=user)
                url_exitosa = reverse('inicio')
                return redirect(url_exitosa)
    else:
        form = AuthenticationForm()
    return render(
        request=request,
        template_name='perfiles/login.html',
        context={'form':form},
    )
class CustomLogoutView(LogoutView):
    template_name = 'perfiles/logout.html'    