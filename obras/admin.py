from django.contrib import admin
from .models import CategoriaObra, Obra


class ObraAdmin(admin.ModelAdmin):
    readonly_fields= ('created', 'updated')

class CategoriaObraAdmin(admin.ModelAdmin):
    readonly_fields= ('created', 'updated')


admin.site.register(CategoriaObra, CategoriaObraAdmin)
admin.site.register(Obra, ObraAdmin)

# Register your models here.
