from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

# pagina de inicio
def home(request):
    return render(request, 'home.html')

# dashboard 
@login_required
def dashboard(request):
    return render(request, 'dashboard.html')

# registrar
def register(request):
    pass


# crear grupos 

# elimiar grupos 

# agregar a un grupo

# eliminar de un grupo 

# hacer formulario de belbin 
