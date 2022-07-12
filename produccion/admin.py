from django.contrib import admin

from produccion.models import Produccion

# Register your models here.

class ProduccionAdmin(admin.ModelAdmin):
    readonly_fields= ('created', 'updated')


admin.site.register(Produccion, ProduccionAdmin)