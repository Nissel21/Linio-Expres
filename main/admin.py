from django.contrib import admin

from .models import *
#tambien se puede importar todas las clases con *

#....
...
class ClienteInline(admin.TabularInline):
    model=Cliente


class ColaboradorInline(admin.TabularInline):
    model=Colaborador


class ProfileAdmin(admin.ModelAdmin):
    inlines = [
        ClienteInline,
        ColaboradorInline
    ]

# Register your models here.
...
admin.site.register(Cliente)
admin.site.register(Colaborador)
admin.site.register(Profile, ProfileAdmin)
admin.site.register(Localizacion)
admin.site.register(Producto)
admin.site.register(Categoria)
admin.site.register(Proveedor)

#username: admin
#email adress: linio_exp@yopmail.com
#se puede entrar despues ahi y ver la bandeja de entrada
#contra es: ru