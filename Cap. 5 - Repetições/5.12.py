##Exercício 5.12:  Altere o programa anterior de forma a perguntar também o valor depositado mensalmente.
##Esse valor será depositado no início de cada mês, e você deve considerá-lo para o cálculo de juros do mês seguinte.
dep = float(input("Depósito inicial: "))
taxa = float(input("Taxa de juros: "))
x = 1
n = 0
while x <= 24:
    dep = dep + n + (dep*taxa/100) 
    x = x + 1
    print(f"Juros mensal referente ao {x-1} mês: R${dep:.2f}")
    n = float(input("Depósito mensal: R$ "))
print(f"Juros total: R$ {dep:.2f}")
