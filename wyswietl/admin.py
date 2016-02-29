from django.contrib import admin
from .models import Odbiorca
from .models import Parametry

class OdbiorcaAdmin(admin.ModelAdmin):
    list_display=('imie','nazwisko')
#    prepopulated_fields={'slug': ('nazwisko',)}


admin.site.register(Odbiorca,OdbiorcaAdmin)
admin.site.register(Parametry)
# Register your models here.
