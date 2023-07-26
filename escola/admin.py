from django.contrib import admin
from escola.models import Aluno, Curso

class Alunos(admin.ModelAdmin):
    list_display = ('id', 'name', 'rg', 'cpf', 'birthdate')
    list_display_links = ('id', 'name')
    search_fields = ['name']
    list_per_page = 20

admin.site.register(Aluno, Alunos)

class Cursos(admin.ModelAdmin):
    list_display = ('id', 'code', 'description')
    list_display_links = ('id', 'code')
    search_fields = ['code']

admin.site.register(Curso, Cursos)
