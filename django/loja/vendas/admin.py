from django.contrib import admin
from .models import Venda, Cobranca, Entrega

admin.site.register(Venda)
admin.site.register(Cobranca)
admin.site.register(Entrega)