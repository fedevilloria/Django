"""
URL configuration for Proyecto1 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

# Siempre hay que importar la parte de la view, sino no se sabe a que se esta haciendo referencia.

# Django utiliza URLS Friendly, esto quiere decir que utiliza urls muy sencillas para que el ceo en los sitios web sea adecuado

#   Tambien se puede escribir asi:
#       from Proyecto1.views import bienvenida, despedida, fecha
from Proyecto1.views import bienvenida
from Proyecto1.views import despedida
from Proyecto1.views import fecha
from Proyecto1.views import calculaEdad
from Proyecto1.views import saludo
from Proyecto1.views import cursoc
from Proyecto1.views import cursocss

urlpatterns = [
    # La url no tiene porque llamarse igual que la funcion, en la primera parte de la coma. Solo que es mas facil comprender a que se esta referenciando. En la segunda coma se especifica la vista que tiene que referenciar esta url. NUNCA OLVIDARSE DE LA COMA AL FINAL.
    path('admin/', admin.site.urls),
    path('bienvenida/', bienvenida),
    path('despedida/', despedida),
    path('fecha/', fecha),
    
    path('edades/<int:anio>', calculaEdad), # Para pasarle el parametro a traves de la URL se escribe entre <> pero a esto lo va a tomar como str(texto) asi que este valor lo tenemos que pasar a int(entero).
    
    path('edades/<int:edad>/<int:anio>', calculaEdad), # Para pasarle dos parametros hay que agregarlo en el path quedaria: 'edades/<int:edad>/<int:anio>'

    path('saludo/', saludo),

    path('cursoc/', cursoc),

    path('cursocss/', cursocss),
]

