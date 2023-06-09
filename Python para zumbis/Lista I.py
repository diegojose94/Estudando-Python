##Exercício 1: Peça dois números inteiros e print a soma deles
a = int(input("Digite um número inteiro: "))
b = int(input("Digite um número inteiro: "))
print (a+b)

##Exercício 2: Peça um valor em metros e print sua conversão para centímetros
metro = float(input("Valor em metros: "))
print (f"Conversão para milimetros: {metro*1000}mm)

##Exercício 3: Escreva um programa que leia a quantidade de dias, horas, minutos e segundos do usuário.
##Calcule o total em segundos.
n4 = int(input("Digite o dia: "))
n5 = int(input("Digite a hora (24h): "))
n6 = int(input("Digite os minutos: "))
n7 = int(input("Digite os segundos: "))
d = n4 * 24 * 60 * 60
h = n5 * 60 * 60
m = n6 * 60
print (f"Resultado: {d+h+m+n7} segundos")

##Exercício 4: Faça um programa que calcule o aumento de um salário. Ele deve solicitar o valor do salário e a
##porcentagem do aumento. Exiba o valor do aumento e do novo salário.
s = float(input("Informe o salário (R$): "))
p = int(input("Informe a porcentagem do aumento (%): "))
p1 = s * p / 100
sf = s + p1
print (f"Valor do aumento: R$ {p1:.2f}")
print (f"Novo salário: R$ {sf:.2f}")

##Exercício 5: Solicite o preço de uma mercadoria e o percentual de desconto.
##Exiba o valor do desconto e o preço a pagar.
preço = float(input("Digite o preço: "))
percentual = int(input("Digite o percentual de desconto: "))
a = preço * percentual / 100
b = preço - a
print (f"Valor do desconto: R$ {a}")
print (f"Preço a pagar: R$ {b}")

##Exercício 6: Calcule o tempo de uma viagem de carro. Pergunte a distância a percorrer e a velocidade média
##esperada para a viagem.    
distância = float(input("Digite a distância: "))
velocidade = int(input("Digite a velocidade média: "))
tempo = distância / velocidade
print (f"O tempo estimado é: {tempo}")

##Exercício 7: Converta uma temperatura digitada em Celsius para Fahrenheit.
##F = 9*C/5 + 32   
c = float(input("Digite o grau em Celsius: "))
f = 9 * c / 5 + 32
print (f"A temperatura em Fahrenheit é: {f:.2f}º")

##Exercício 8: Faça agora o contrário, de Fahrenheit para Celsius.
f1 = float(input("Digite o grau em Fahrenheint: "))
c1 = (f1 - 32) / 1.8
print (f"A temperatura em Celsius é: {c1:.2f}º")

##Exercício 9: Escreva um programa que pergunte a quantidade de km percorridos por um carro alugado pelo
##usuário, assim como a quantidade de dias pelos quais o carro foi alugado. Calcule o preço a pagar,
##sabendo que o carro custa R$ 60,00 por dia e R$ 0,15 por km rodado.
km = float(input("Digite a distância percorrida em quilômetros: "))
d = int(input("Digite por quantos dias o carro foi alugado: "))
preçod = d * 60
preçokm = km * 0.15
débito = preçod + preçokm
print (f"O preço a pagar é: R$ {débito:.2f}")
       
##Exercício 10: Escreva um programa para calcular a redução do tempo de vida de um fumante.
##Pergunte a quantidade de cigarros fumados por dia e quantos anos ele já fumou.
##Considere que um fumante perde 10 minutos de vida a cada cigarro,
##calcule quantos dias de vida um fumante perderá. Exiba o total de dias.
cigarrosdia = float(input("Quantos cigarros você fuma por dia? "))
anos = float(input("Há quantos anos você fuma? "))
m = (cigarrosdia * 10 * anos * 365) / 1440
print (f"Você perderá {m:.2f} dias da sua vida.") 

##Exercício 11: Sabendo que str( ) converte valores numéricos para string, calcule quantos dígitos há em 2 elevado
##a um milhão.
exp = 2 ** 1000000
print(len(str(exp))


11)



5)

6)


