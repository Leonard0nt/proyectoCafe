from django.shortcuts import render
from django.contrib import messages

# Create your views here.
from django.shortcuts import render, redirect
from .forms import RegistroForm

def registro_view(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, '¡Registro exitoso!')
            return redirect('/')
    else:
        form = RegistroForm()
    return render(request, '../templates/registro.html', {'form': form})

