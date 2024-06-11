from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from .forms import RegistroForm

def registro_view(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('registro_exitoso')
    else:
        form = RegistroForm()
    return render(request, '../templates/registro.html', {'form': form})

def registro_exitoso_view(request):
    return render(request, '../templates/registroExitoso.html')
