##Exercício 5.11: Escreva um programa que pergunte o depósito inicial e a taxa de juros de uma poupança.
##Exiba os valores mês a mês para os 24 primeiros meses. Escreva o total ganho com juros no período.
dep = float(input("Depósito inicial: "))
taxa = float(input("Taxa de juros: "))
x = 1
while x <= 24:
    dep = dep + (dep*taxa/100)
    x = x + 1
    print(f"Juros mensal: R${dep:.2f}")
print(f"Juros total: R$ {dep:.2f}")
