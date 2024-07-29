from django.contrib import admin

from gestionPedidos.models import Clientes
from gestionPedidos.models import Articulos
from gestionPedidos.models import Pedidos

# Register your models here.

# list_display -> Sirve para ver mas de un campo en el registro del panel de administracion, por parametro recibe las variables escritas en "models" que queremos ver.
# search_fields -> Sirve para agregar una barra de busqueda en el panel de administracion, por parametro recibe el filtro que queremos buscar.

class ClientesAdmin(admin.ModelAdmin):
    list_display = ["nombre", "email"]
    search_fields = ["nombre"]

admin.site.register(Clientes, ClientesAdmin)
admin.site.register(Articulos)
admin.site.register(Pedidos)