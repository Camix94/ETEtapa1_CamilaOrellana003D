from django import forms
from django.forms import ModelForm
from django.forms import widgets
from django.forms.models import ModelChoiceField
from django.forms.widgets import Widget
from . models import MonedaPago, ProveedorNuevo

class ProveedorForm(forms.ModelForm):

    class Meta: 
        model= ProveedorNuevo
        fields = ['nroIdentificacion','fotoLogo', 'nombre', 'fono', 'direccion', 'email', 'pais', 'contraseña', 'monedaPago']
        labels ={
            'nroIdentificacion' : 'Número Identificación',
            'fotoLogo' : 'Imagen *obligatorio' ,
            'nombre' : 'Nombre Completo', 
            'fono' : 'Teléfono', 
            'direccion' : 'Dirección',
            'email' : 'Email', 
            'pais' : 'País', 
            'contraseña' : 'Contraseña',
            'monedaPago' : 'Moneda de Pago'
        }
        widgets={
            'nroIdentificacion': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese número de identificación', 
                    'name': 'nroIdentificacion',
                    'id' : 'nroIdentificacion'
                }
            ),
            'fotoLogo': forms.ClearableFileInput(
                attrs={
                    'class': 'form-control', 
                    'name': 'fotoLogo',
                    'id' : 'fotoLogo'
                }
            ), 
            'nombre': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese nombre completo', 
                    'name': 'nombre',
                    'id' : 'nombre'
                }
            ), 
            'fono': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese teléfono', 
                    'name': 'fono',
                    'id' : 'fono'
                }
            ),
            'direccion': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese dirección', 
                    'name': 'direccion',
                    'id' : 'direccion'
                }
            ),
            'email': forms.EmailInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese email', 
                    'name': 'email',
                    'id' : 'email'
                }
            ),
            'pais': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese país', 
                    'name': 'pais',
                    'id' : 'pais'
                }
            ), 
            'contraseña': forms.PasswordInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese contraseña',
                    'name': 'contraseña',
                    'id' : 'contraseña'
                }
            ),
           
            'monedaPago': forms.Select(
                attrs={
                    'class': 'form-control',
                    'name': 'monedaPago',
                    'id' : 'monedaPago'
                }
            )

        }