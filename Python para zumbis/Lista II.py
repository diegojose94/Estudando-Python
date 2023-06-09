##Exercício 1: Faça um Programa que peça os três lados de um triângulo. O programa deverá informar se os valores podem ser
##um triângulo. Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno.
a = float(input("1º lado: "))
b = float(input("2º lado: "))
c = float(input("3º lado: "))
if a > b + c or b > a + c or c > a + b:
    print("Sua forma não é um triângulo")
if a == b == c:
    print("Triângulo equilátero")
elif a == b or a == c or b == c:
    print("Triângulo isósceles")
else:
    print ("Triângulo escaleno")

##Exercício 2: Determine se um ano é bissexto. Verifique no Google como fazer isso...
from calendar import isleap
year = int(input("Ano: "))
if isleap(year):
    print ("É bissexto")
else:
    print ("Não é bissexto")

##Exercício 3: João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento diário de
##seu trabalho. Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do
##estado de São Paulo (50 quilos) deve pagar uma multa de R$ 4,00 por quilo excedente. João precisa que você
##faça um programa que leia a variável peso (peso de peixes) e verifique se há excesso. Se houver,
##gravar na variável excesso e na variável multa o valor da multa que João deverá pagar.
##Caso contrário mostrar tais variáveis com o conteúdo ZERO.
x = float(input("Peso: "))
excesso = x - 50
multa = (x - 50) * 4
if x > 50:
    print (f"Excesso: {excesso}kg")
    print (f"Multa: R${multa:.2f}")
else:
    print ("Excesso: 0kg")
    print ("Multa: R$0,00")

##Exercício 4: Faça um Programa que leia três números e mostre o maior deles.
aa = float(input("Primeiro número: "))
ab = float(input("Segundo número: "))
ac = float(input("Terceiro número: "))
if aa > ab and aa > ac:
    print(f"{aa} é o maior número")
elif ab > aa and ab > ac:
    print(f"{ab} é o maior número")
elif ac > aa and ac > ab:
    print(f"{ac} é o maior número")

##Exercício 5: Faça um Programa que leia três números e mostre o maior e o menor deles.
a1 = float(input("Primeiro número: "))
a2 = float(input("Segundo número: "))
a3 = float(input("Terceiro número: "))
if a1 < a2 and a1 < a3:
    print(f"{a1} é o menor número")
elif a2 < a3:
    print(f"{a2} é o menor número")
else:
    print(f"{a3} é o menor número")
if a1 > a2 and a1 > a3:
    print(f"{a1} é o maior número")
elif a2 > a1 and a2 > a3:
    print(f"{a2} é o maior número")
elif a3 > a1 and a3 > a2:
    print(f"{a3} é o maior número")

##Exercício 6: Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
##Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda,
##8% para o INSS e 5% para o sindicato, faça um programa que nos dê o salário bruto, quanto pagou ao INSS,
##quanto pagou ao sindicato e o salário líquido.
##Observe que Salário Bruto - Descontos = Salário Líquido. Calcule os descontos e o salário líquido, conforme a tabela abaixo:
##a. + Salário Bruto : R$
##b. - IR (11%) : R$
##c. - INSS (8%) : R$
##d. - Sindicato (5%) : R$
##e. = Salário Liquido : R$
ganho = float(input("Ganho por hora trabalhada: "))
horas = float(input("Horas trabalhadas no mês: "))
salário = ganho * horas
ir = 11 * salário / 100
inss = 8 * salário / 100
sindicato = 5 * salário / 100
salárioliq = salário - (ir + inss + sindicato)
print (f"Salário bruto: RS {salário:.2f}")
print (f"INSS: R$ {inss:.2f}")
print (f"Sindicato: R$ {sindicato:.2f}")
print (f"Imposto de renda: R$ {ir:.2f}")
print (f"Salário líquido: R$ {salárioliq:.2f}")

##Exercício 7: Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a
##ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida
##em latas de 18 litros, que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta a serem
##compradas e o preço total.
##Obs. : somente são vendidos um número inteiro de latas.
area = float(input("Área a ser pintada, em m²: "))
if area % 18 == 0:
    latas = area / 18
else:
    latas = int(area / 18) + 1
preço = latas * 80
print (f"Qtde. de latas: {latas}")
print (f"Preço total: R% {preço:.2f}")

