from django.contrib import admin
from .models import Cliente, Emprestimo

class EmprestimoInline(admin.TabularInline):  # ou admin.StackedInline para exibição diferente
    model = Emprestimo
    extra = 0  # Quantidade de campos em branco para exibição inicial

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nome',)
    inlines = [EmprestimoInline]

@admin.register(Emprestimo)
class EmprestimoAdmin(admin.ModelAdmin):
    list_display = ('cliente', 'valor_emprestado', 'taxa', 'tempo', 'valor_total', 'parcelas')
    readonly_fields = ('valor_total', 'parcelas')

    def valor_total(self, obj):
        return obj.calcular_valor_total()
    valor_total.short_description = 'Valor Total'

    def parcelas(self, obj):
        return obj.calcular_parcelas()
    parcelas.short_description = 'Parcelas'
