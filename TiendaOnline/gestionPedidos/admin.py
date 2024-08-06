from django.contrib import admin

from gestionPedidos.models import Clientes
from gestionPedidos.models import Articulos
from gestionPedidos.models import Pedidos

# Register your models here.

# list_display -> Sirve para ver mas de un campo en el registro del panel de administracion, por parametro recibe las variables escritas en "models" que queremos ver.
# search_fields -> Sirve para agregar una barra de busqueda en el panel de administracion, por parametro recibe el filtro que queremos buscar.

# list_filter -> Sirve para agregar un filtro en el panel de administracion, le pasamos como parametro lo que queremos mostrar en ese filtro.

# date_hierarchy -> Sirve para mostrar la fecha con otra jerarquia, en este caso nos muestra los anos en la parte superior del panel. No hace falta agregarle los corchetes.

class ClientesAdmin(admin.ModelAdmin):
    list_display = ["nombre", "email",]
    search_fields = ["nombre",]

class ArticulosAdmin(admin.ModelAdmin):
    list_filter = ["seccion",]

class PedidosAdmin(admin.ModelAdmin):
    list_display = ["numero", "fecha",]
    list_filter = ["fecha",]
    date_hierarchy = "fecha"

admin.site.register(Clientes, ClientesAdmin)
admin.site.register(Articulos, ArticulosAdmin)
admin.site.register(Pedidos, PedidosAdmin)