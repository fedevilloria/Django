from django.db import models

# Create your models here.

# Aca adentro hay que crear una clase model por cada tabla que necesitemos que tenga la base de datos


# Nuestra primera tabla va a ser la de Clientes, se crea con el class y nombre de tabla, dentro de ella van a ir los campos que queremos en nuestra tabla. Como primer campo hacemos el de nombres el cual le ponemos el tipo de datos que va a almacenar.

"""
1er campo:
Nombre = campo
models.CharField(max_length=30) = tipo de dato en este caso caracter con una longitud de 30 caracteres como maximo.

2do campo
direccion = campo
models.CharField(max_length=50) = tipo de dato en este caso caracter con una longitud de 50 caracteres como maximo.

3er campo
email = campo
models.EmailField() = tipo de dato en este caso es el de email el cual verificara que exista el arroba y un punto como minimo.
"""

class Clientes(models.Model):
    nombre = models.CharField(max_length=30)
    direccion = models.CharField(max_length=50)
    email = models.EmailField(blank=True, null=True)
    telefono = models.CharField(max_length=7)

    def __str__(self):
        return self.nombre

class Articulos(models.Model):
    nombre = models.CharField(max_length=30)
    seccion = models.CharField(max_length=20)
    precio = models.IntegerField()

    def __str__(self):
        return "El nombre es %s la seccion es %s y el precio es %s" %(self.nombre, self.seccion, self.precio)

class Pedidos(models.Model):
    numero = models.IntegerField()
    fecha = models.DateField()
    entregado = models.BooleanField()