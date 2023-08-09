import math
from django.db import models

class Cliente(models.Model):
    nome = models.CharField(max_length=50)

    def __str__(self):
        return self.nome

    def calcular_valor_total_emprestado(self):
        emprestimos = self.emprestimos.all()
        total_emprestado = sum([emprestimo.valor_emprestado for emprestimo in emprestimos])
        return total_emprestado

    def calcular_valor_total_divida(self):
        emprestimos = self.emprestimos.all()
        total_divida = sum([emprestimo.calcular_valor_total() for emprestimo in emprestimos])
        return total_divida

class Emprestimo(models.Model):
    cliente = models.ForeignKey(Cliente, related_name='emprestimos', on_delete=models.CASCADE)
    valor_emprestado = models.FloatField()
    taxa = models.FloatField()
    tempo = models.IntegerField()

    def __str__(self):
        return f"Empréstimo de {self.cliente} - ID: {self.id}"

    def calcular_valor_total(self):
        if None in (self.valor_emprestado, self.taxa, self.tempo):
            return None
        valor_final = round(self.valor_emprestado * math.pow(1 + self.taxa / 100, self.tempo), 2)
        return valor_final

    def calcular_parcelas(self):
        valor_final = self.calcular_valor_total()
        if valor_final is None or self.tempo == 0:
            return None
        valor_parcela = round(valor_final / self.tempo, 2)
        return valor_parcela
