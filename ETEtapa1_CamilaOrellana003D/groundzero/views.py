
from django.shortcuts import render, redirect
from .models import MonedaPago, ProveedorNuevo
from .forms import ProveedorForm

# Create your views here.
def home(request):
    return render(request, 'index.html')

#def crearContraseña (identificacion, nombre, pais, telefono):
#    cadena1 = str(identificacion[0:2])
#    cadena2 = (nombre[0:2])
#    cadena3 = (pais[-2:]).lower
#    cadena4 =  str(telefono[-2:])
#    contraseña = cadena1 + cadena2 + cadena3 + cadena4
#    return contraseña

#def funcionPruebas(request):
 #   a = request.POST['nroIdentificacion']
#    b = request.POST['nombre']
 #   c= request.POST['pais']
 #   d = request.POST['fono']
 #   e = a[0:2] + (b[0:2]).upper() + (c[-2:]).lower + d[-2:]
 #   return JsonResponse({'contraseña': e})

#def crearContraseña () :
#                contraseña = request.POST['nroIdentificacion'][0:2] + (request.POST['nombre']#[0:2]).upper() + (request.POST['pais'][-2:]).lower +  request.POST['fono'][-2:]
#                return 'contraseña' = contraseña

#def contraseña(para1,para2,para3,para4):
#    ide = para1
#    nom = para2
#    pais = para3
#    fono = para4
#    nueva = str(ide[:2]) + nom[:2].upper() + pais[-2:].lower() + str(fono[-2:])
#    return nueva
    



def crearProveedorNuevo(request):
    if request.method=='POST':  
        #ide = request.POST['nroIdentificacion']
        #nom = request.POST['nombre']
        #pai = request.POST['pais']
        #fon = request.POST['fono']
        #nueva = str(ide[:2]) + nom[:2].upper() + pai[-2:].lower() + str(fon[-2:])
        form_1 = ProveedorForm(request.POST, request.FILES)
        #form_1.contraseña = nueva
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

