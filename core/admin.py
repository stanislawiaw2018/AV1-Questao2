from django.contrib import admin
from core.models import *
# default: "Administração do Django"
admin.site.site_header = 'Painel de Controle'
# default: "Administração do Site"
admin.site.index_title = 'Aplicações'
# default: ”Site de administração do Django"
admin.site.site_title = 'AProf'


class ProfessorAdmin(admin.ModelAdmin):
    list_display = (
        'nome','carga','valor'
    )
    list_filter = (
        'nome','valor')

class CursoAdmin(admin.ModelAdmin):
    list_display = (
        'nome', 'carga_horaria', 'valor'
    )
class ProfessorInline(admin.TabularInline):
    model = Professor
class TurmaAdmin(admin.ModelAdmin):
    inlines = [
        ProfessorInline
    ]
admin.site.register(Turma)
admin.site.register(Curso,CursoAdmin)
admin.site.register(Professor,ProfessorAdmin)



