##Exercício 5.15: Escreva um programa para controlar uma pequena máquina registradora.
##Você deve solicitar ao usuário que digite o código do produto e a quantidade comprada.
##Utilize a tabela de códigos abaixo para obter o preço de cada produto:
##Código Preço
##  1    0,50
##  2    1,00
##  3    4,00
##  5    7,00
##  9    8,00
##Seu programa deve exibir o total das compras depois que o usuário digitar 0.
##Qualquer outro código deve gerar a mensagem de erro “Código inválido”.
##cont = 0
##soma = 0
while True:
    n = float(input("Código: "))
    if n == 0:
        break
    elif n == 1:
        n = 0.50
    elif n == 2:
        n = 1
    elif n == 3:
        n = 4
    elif n == 5:
        n = 7
    elif n == 9:
        n = 8
    else:
        print("Código inválido")
    qtde = int(input("Quantidade: "))
    preço = n * qtde
    soma = soma + preço
    cont = cont + qtde
print(f"Preço total: R$ {soma:.2f}")
print(f"Qtde total de produtos: {cont:.0f}")
    
