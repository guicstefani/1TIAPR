"""
Exercicio 5: Laco for - Produto de 1 a 5
Comeca com produto = 1 (elemento neutro da multiplicacao) e multiplica
por cada numero do intervalo de 1 a 5.
"""
produto = 1
for numero in range(1, 6):
    produto *= numero
print("Produto:", produto)
