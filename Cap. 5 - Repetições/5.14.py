##Exercício 5.14: Escreva um programa que leia números inteiros do teclado. O programa deve ler os números até que o usuário digite O (zero).
##No final da execução, exiba a quantidade de números digitados, assim como a soma e a média aritmética.
n = 0
cont = 0
soma = 0
while True:
    n = int(input("Número: "))
    cont = cont + 1
    soma = soma + n
    if n == 0:
        break
print(f"Qtde. números digitados: {cont-1}, soma: {soma}, média: {soma/(cont-1)}")
