
from django.shortcuts import render, redirect
from .models import MonedaPago, ProveedorNuevo
from .forms import ProveedorForm

# Create your views here.
def home(request):
    return render(request, 'index.html')

def crearProveedorNuevo(request):
    if request.method=='POST':  
        data=request.POST
        # Remember the old way
        _mutable = data._mutable
        # Set _mutable to True
        data._mutable = True
        
        ide = request.POST['nroIdentificacion']
        nom = request.POST['nombre']
        pai = request.POST['pais']
        fon = request.POST['fono']
        nueva = str(ide)[:2] + nom[:2].upper() + pai[-2:].lower() + str(fon)[-2:]
        data['contraseña'] = nueva
        
        # Restore the original attributes of _mutable
        data._mutable = _mutable
        
        form_1 = ProveedorForm(request.POST, request.FILES)

        if form_1.is_valid():
            form_1.save()    
            return redirect('home')
    else:
        form_1= ProveedorForm()
    return render(request, 'groundzero/formulario-proveedor.html', {'form_1': form_1})

def Ver(request):
    proveedores = ProveedorNuevo.objects.all()

    return render(request, 'groundzero/mostrar-proveedores.html', context={'proveedores':proveedores})

def form_mod_proveedor(request,id):
    proveedor = ProveedorNuevo.objects.get(nroIdentificacion=id)

    datos ={
        'form': ProveedorForm(instance=proveedor )
    }
    if request.method == 'POST': 
        formulario = ProveedorForm(data=request.POST, instance = proveedor)
        if formulario.is_valid: 
            formulario.save()           
            return redirect('ver')
    return render(request, 'groundzero/formulario-modificar-proveedor.html', datos)

def eliminar_proveedor(request,id):
    proveedor  = ProveedorNuevo.objects.get(nroIdentificacion=id)
    proveedor.delete()
    return redirect('ver')

