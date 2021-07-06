from django.db import models

# Create your models here.
class MonedaPago(models.Model):
    idMonedaPago = models.IntegerField(primary_key=True, verbose_name='Id de Moneda de Pago')
    nombreCategoria = models.CharField(max_length=50, verbose_name='Tipo Moneda')

    def __str__(self):
        return self.nombreCategoria

class ProveedorNuevo(models.Model):
    nroIdentificacion = models.IntegerField(primary_key=True, verbose_name="Número Identificación")
    fotoLogo = models.ImageField(upload_to='images/', null=True, blank=True)
    nombre = models.CharField(max_length=500, verbose_name='Nombre Completo')
    fono = models.IntegerField(verbose_name='Teléfono')
    direccion = models.CharField(max_length=200, verbose_name='Dirección')
    email = models.EmailField(max_length=100, verbose_name='Email')
    pais = models.CharField(max_length=100, verbose_name='País')
    contraseña = models.CharField(max_length=10, verbose_name='Contraseña')
    monedaPago = models.ForeignKey(MonedaPago, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre




