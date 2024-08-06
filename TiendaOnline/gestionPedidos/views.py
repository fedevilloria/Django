from django.shortcuts import render
from django.http import HttpResponse
from gestionPedidos.models import Articulos
from django.core.mail import send_mail
from django.conf import settings
from gestionPedidos.forms import FormularioContacto

# Create your views here.
def busqueda_productos(request):

    return render(request, "busqueda_productos.html")

def buscar(request):
    
    if request.GET["producto"]:

        prd = request.GET["producto"]

        # Esto es para que los caracteres de busqueda no excedan de 20
        if len(prd) > 20:
            mensaje = "Texto de busqueda demasiado largo"
        
        else:
            articulo = Articulos.objects.filter(nombre__icontains=prd)

            return render(request, "resultados_busquedas.html", {"articulo":articulo, "query":prd})

    else:
        mensaje = "No has introducido nada"
    
    return HttpResponse(mensaje)

# Recordar que post y get tienen que estar en mayusculas, si no, no funciona


#def contacto(request):
    
#    if request.method == "POST":
#        asunto = request.POST["asunto"]
#        mensaje = request.POST["mensaje"] + " " + request.POST["email"]
#        mail_desde = settings.EMAIL_HOST_USER
#        mail_llegada = ["xdeepyt00@gmail.com"]
#        send_mail(asunto, mensaje, mail_desde, mail_llegada)
#        return render(request, "gracias.html",)
    
#    return render(request, "contacto.html",)


def contacto(request):
    
    if request.method == "POST":
        miformulario = FormularioContacto(request.POST)

        if miformulario.is_valid():
            info = miformulario.cleaned_data
            send_mail(info["asunto"], info["mensaje"], info.get("email", ""), ["fede.bruno_03@hotmail.com"],)

            return render(request, "gracias.html",)
    else:
        miformulario = FormularioContacto()
    
    return render(request, "formulario_contacto.html", {"form": miformulario})

"""
Si el usuario ha pulsado el boton de enviar (if request.method == "POST":) lo primero es que cree una variable que pueda guardar la informacion del formulario.

Si el formulario paso la validacion (if miformulario.is_valid()) se crea una variable en la que podamos almacenar solo la informacion enviada por el usuario, luego utilizamos el metodo "send_mail" para que la envie al correo electronico.

**** ACLARACION ****
Lo que esta dentro de "send_mail" es la informacion que rescato del diccionario creado por el metodo "cleaned_data" de la variable 'info'.
     ********

El metodo get lo que hace es enviar la informacion desde el email ingresado por el usuario hacia el mail aclarado despues. Si no se agrega nada se supone que se envia al mail configurado del HOST. Despues tambien volvemos a agregar el mail del destinatario.

En el caso que no se haya ingresado nada o no se haya enviado lo que va a hacer es que construye el formulario vacio hasta que se rellenen los campos y se logre enviar, una vez se envia entra en el primer if.

return render(request, "formulario_contacto.html", {"form": miformulario}): Aca basicamente lo que hacemos es decirle que me renderice un documento llamado "formulario_contacto.html", a ese documento lo vas a construir con lo que hay aca: {"form": miformulario} y lo que hay ahi es un formulario vacio que nos construye la clase 'FormularioContacto' dentro del archivo "forms.py".
"""