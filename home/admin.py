from django.contrib import admin
from .models import Medico


@admin.register(Medico)
class detMedico(admin.ModelAdmin):
    list_display = ('id', 'nome', 'crm', 'especialidade', 'foto')