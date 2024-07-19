#   Request: Hace la peticion
#   Response: Envia la respuesta de la peticion

#   Al hacer la funcion nunca olvidarse del parametro request, si no devuelve un error 404 la web.

from django.http import HttpResponse
import datetime
from django.template import Template, Context

from django.template import loader

from django.shortcuts import render


def bienvenida(request): #Primera vista

    return HttpResponse("Bienvenido chaval")

def despedida(request):

    return HttpResponse("Adios chaval")

#   Otra forma de hacer la funcion es de esta manera
def bienvenida(request):

    #documento="Hola mundo" # Tambien se puede editar el contenido como en HTML (h1, h2, etc.) y quedaria: <html><body><h1>"Hola mundo"</h1></body></html>
    # Con estos parametros adopta las caracteristicas de HTML.

    # Se puede tambien con el otro formato pero utilizando las triples comillas:
    #documento="""
    #               <html>
    #                   <body>
    #                       <h1>
    #                           "Hola mundo"
    #                       </h1>
    #                   </body>
    #               </html>
    #           """
    # ESTO ES UNA MALA PRACTICA



    # El siguiente metodo es a traves de plantillas:

    documento_externo = open("D:/Curso Django/Proyecto1/Proyecto1/plantillas/miplantilla") # Este es un metodo de importacion de plantilla, el cual no se utiliza de esta manera, por lo general se usa con cargadores, pero eso todavia no lo vi.
    
    # Lo que hacemos es por el metodo de abrir archivos es buscar la ubicacion del archivo de la plantilla y guardarla en una variable, la cual la utilizamos despues para devolver en la funcion.
    
    # Recordar importar django.template = context y template.
    plt = Template(documento_externo.read()) # Leemos y almacenamos el archivo de la plantilla en una variable.
    documento_externo.close() # Lo cerramos para que no consuma memoria innecesariamente

    ctx = Context() # Ahora le pasamos el contexto, en este caso es un contexto vacio porque no interactua en tiempo real.

    documento = plt.render(ctx) # Luego en la variable documento lo que hacemos es reenderizar ese documento pasandole como atributo el contexto (en este caso vacio) del archivo template en la variable plt.

    return HttpResponse(documento)


# CONTENIDO DINAMICO: Es aquel que toma informacion del servidor en tiempo real y lo mostrara por pantalla.
# El ejemplo mas comun es el de fecha y hora:
def fecha(request):
    fecha_actual = datetime.datetime.now()
    documento="""
                   <html>
                       <body>
                           <h2>
                               Fecha y hora actuales: %s
                           </h2>
                       </body>
                   </html>
               """ %fecha_actual
    return HttpResponse(documento)

# %s es un marcador de posicion.
# Para luego poner lo que quiero en esa posicion fuera de las comillas se escribe %variable, si tengo mas de 2 variables a representar seria: %(var1, var2) y se asignan automaticamente por posicion.



# Como pasar parametros a traves de la URL.
# El ejemplo que se va a utilizar es que calcule cuantos anios tendremos en un tiempo x.

# El parametro anio lo vamos a pasar por la url, entonces lo que hara es calcular a traves de ese parametro restando el anio actual

def calculaEdad(request, anio):
    edadActual = 18
    periodo = anio-2024
    edadFutura = edadActual + periodo
    documento = "<html><body><h2> En el año %s tendras %s años" %(anio, edadFutura)
    return HttpResponse(documento)

#   Para pasarle dos parametros simplemente lo agregamos como parametro que va a recibir la funcion y luego hacemos los cambios en las variables

def calculaEdad(request, edad, anio):
    #edadActual = 18
    periodo = anio-2024
    edadFutura = edad + periodo
    documento = "<html><body><h2> En el año %s tendras %s años" %(anio, edadFutura)
    return HttpResponse(documento)

# Este fragmento es dee programacion orientada a objetos, lo que hago es pasarle por parametro el nombre y el apellido.
# Luego en la funcion de saludo al crear la variable "p1" y utilizar el objeto "Persona" lo que hago con el punto es llamar a la propiedad de nombre y de apellido para poder dar a conocer estos valores.
class Persona(object):
    def __init__(self, nombre, apellido):
        self.nombre = nombre

        self.apellido = apellido


def saludo(request):

    p1 = Persona("Profe Juan", "Perez")
    
    #nombre = "Juan" # Tambien en vez de colocarle un valor aqui a la variable, se lo podriamos haber puesto dentro del diccionario del contexto, quedando como resultado: {"nombre_persona": "Juan"}

    #apellido = "Perez"

    temas_del_curso = ["Plantillas", "Modelos", "Formularios", "Vistas", "Despliegue"]

    ahora = datetime.datetime.now()

    #documento = doc_externo.render(ctx)

    #doc_externo = open("D:/Curso Django/Proyecto1/Proyecto1/plantillas/miplantilla")

    #plt = Template(doc_externo.read())
    #doc_externo.close()

    #ctx = Context({"nombre_persona": p1.nombre, "apellido_persona": p1.apellido, "momento_actual": ahora, "temas": temas_del_curso}) # De esta forma le estoy poroporcionando al contexto que bajo la clave de "nombre_persona", esta el valor almacenado dentro de la variable nombre.
    
    # Ademas dentro del diccionario podemos pasarle una lista, tomando el nombre y en el valor es donde apareceria la lista. Otra forma posible es crear una variable, ahi dentro hacer referencia a la lista y luego en el diccionario crear una clave para esa variable.

    #documento = plt.render(ctx)


    """
    Para poder utilizar el loader hay que hacer lo siguiente:
    1- Ir a settings y en la parte de templates ubicar la clave "DIRS"
    2- Dentro de "DIRS" hay que especificarle la ruta. En este caso seria D:/Curso Django/Proyecto1/Proyecto1/plantillas
    3- Para cargar la plantilla hay que crear una variable
        ejemplo = loader.get_template('Nombre de plantilla.extension')
    4- Renderizar el documento de la variable

    Quedaria asi:

    from django.template import loader
    doc_externo = loader.get_template('miplantilla.html')
    documento = doc_externo.render({"nombre_persona": p1.nombre, "apellido_persona": p1.apellido, "momento_actual": ahora, "temas": temas_del_curso})
"""
    #doc_externo = loader.get_template('miplantilla')
    #documento = doc_externo.render({"nombre_persona": p1.nombre, "apellido_persona": p1.apellido, "momento_actual": ahora, "temas": temas_del_curso}) # El contexto con el diccionario ahora es pasado directamente al render.


    # En este momento estamos usando el modulo render de la libreria shortcut de Django, esto nos simplifica varias lineas de codigo. El primero y el segundo atributo son obligatorios, es decir, siempre lleva como atributo request y luego la plantilla con el nombre propio, el tercer argumento es opcional, en este caso es el contexto que ya definimos anteriormente, le pasamos directamente el diccionario en vez de la variable del contexto. Con esto nos olvidamos de tener que cargar una plantilla, renderizarla y luego pasarle el contexto, nos ahorra muchas lineas de codigo.
    return render(request, "miplantilla", {"nombre_persona": p1.nombre, "apellido_persona": p1.apellido, "momento_actual": ahora, "temas": temas_del_curso})

def cursoc(request):
    fecha_actual = datetime.datetime.now()
    return render(request, "cursoc.html", {"fecha":fecha_actual}) # Aca lo que hacemos es actualizar la vista para la nueva plantilla, en este caso le pasamos los valores del dia que solicitamos en dicha plantilla.

def cursocss(request):
    fecha_actual = datetime.datetime.now()
    return render(request, "cursocss.html", {"fecha": fecha_actual})