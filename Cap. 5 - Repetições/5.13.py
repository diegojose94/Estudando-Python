##[CORRIGIR]
##Exercício 5.13: Escreva um programa que pergunte o valor inicial de uma dívida e o juro mensal.
##Pergunte também o valor mensal que será pago. Imprima o número de meses para que a dívida seja paga,
##o total pago e o total de juros pago.
divida = float(input("Dívida: "))
jurosMensal = float(input("Juro mensal: "))
pgmtMensal = float(input("Pagamento mensal: "))
prestacoes = divida/pgmtMensal
jurosTotal = 0
x = 0
k = 0
print(f"Número de prestações: {divida/pgmtMensal:.0f}")
while k < divida:
    x = x + 1
    pgmt = float(input(f"{x}º Pagamento: R$ "))
    k = k + pgmt
    jurosTotal = (jurosTotal/100)*divida
    print(f"Valor pago: R$ {k:.2f}")
    
print(f"Juros total: R$ {prestacoes:.2f}")
print(f"Juros total: R$ {jurosTotal:.2f}")

debito = float(input("Valor da dívida: R$ "))
juros = float(input("Juros mensal (%): "))
pgmtMes = float(input("Valor mensal que será pago: R$ "))
debitoTotal = debito*juros*pgmtMes
prestacoes = debitoTotal/pgmtMes
mes = 1
print(debitoTotal)
print(prestacoes)
