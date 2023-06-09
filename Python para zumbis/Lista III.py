##Exercício 1: Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor
##seja inválido e continue pedindo até que o usuário informe um valor válido.
x = int(input('Insira uma nota: '))
while x > 10 or x < 0:
    print ('Notas inválida')
    x = int(input('Insira uma nota: '))

##Exercício 2: Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao
##nome do usuário, mostrando uma mensagem de erro e voltando a pedir as informações.
user = str(input('Usuário: '))
password = str(input('Senha: '))
while user == password:
    print ('Usuário e senha não podem ser iguais')
    user = str(input('Usuário: '))
    password = str(input('Senha: '))

##Exercício 3: Supondo que a população de um país A seja da ordem de 80000 habitantes com uma taxa
##anual de crescimento de 3% e que a população de B seja 200000 habitantes com uma taxa de
##crescimento de 1.5%. Faça um programa que calcule e escreva o número de anos
##necessários para que a população do país A ultrapasse ou iguale a população do país B,
##mantidas as taxas de crescimento.
a = 80000
b = 200000
anos = 0
while a <= b:
    a = a + a * 0.03
    b = b + b * 0.015
    anos = anos + 1
print (anos)

##Exercício 4: A seqüência de Fibonacci é a seguinte: 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, ... Sua regra de
##formação é simples: os dois primeiros elementos são 1; a partir de então, cada elemento é a
##soma dos dois anteriores. Faça um algoritmo que leia um número inteiro calcule o seu número
##de Fibonacci. F1= 1, F2= 1, F3= 2, etc.
n = int(input('Digite o valor de n: '))
a, b = 1, 1
k = 1
while k <= n-2:
    a, b = b, a + b
    k = k + 1
print (b)

##Exercício 5: Dados dois números inteiros positivos, determinar o máximo divisor comum entre eles usando
##o algoritmo de Euclides.
a = int(input('Valor de a: '))
b = int(input('Valor de b: '))
while a % b != 0:
    a, b = b, a%b
print (f'MDC = {b}')

