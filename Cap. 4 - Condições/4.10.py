### Exercício 4.1
### O que acontece se a for igual a b? 
##a = int(input("Digite um número: "))
##b = int(input("Digite um número: "))
##if a > b:
##    print("O primeiro número é maior")
##if a < b:
##    print("O segundo número é maior")
### Caso a seja igual b, o programa não devolve nenhuma resposta


### Exercício 4.2
##vel = int(input("Qual a velocidade do carro? "))
##if vel > 80:
##    val = (vel - 80) * 5
##    print("Eba, você foi multado :D")
##    print("O valor da sua multa é R$%.2f" % val)
    
### Exercício 4.3
##a = int(input("Fala um número ai: "))
##b = int(input("Fala outro: "))
##c = int(input("Agora o último: "))
##maior = a
##if b > a and b > c:
##    maior = b
##if c > a and c > b:
##    maior = c
##menor = a
##if b < a and b < c:
##    menor = b
##if c < a and c < b:
##    menor = c
##print("%d é o maior número" %maior)
##print("%d é o menor número" %menor)

### Exercício 4.4
##sal = float(input("Salário: R$ "))
##aumento = 0
##if sal > 1250:
##    sal = sal + aumento
##    aumento = sal * 0.10
##    print("Sorria, você não está mais abaixo da linha de pobreza com seu novo aumento de R$%.2f" %aumento)
##if sal <= 1250:
##    sal = sal + aumento
##    aumento = sal * 0.15
##    print("Sorria, você não está mais abaixo da linha de pobreza com seu novo aumento de R$%.2f" %aumento)
##    

### Exercício 4.5
##idade = int(input("Digite a idade do seu carro: "))
##if idade <= 3:
##    print("Seu carro é novo :)")
##else:
##    print("Seu carro talvez esteja um pouquinho velho :(")

### Exercício 4.6
##dist = int(input("Digite a distância a percorrer em km: "))
##if dist <= 200:
##    preço = dist * 0.50
##else:
##    preço = dist * 0.45
##print("Valor a pagar: %2.f" %preço)

# Exercício 4.7
# Rastrear programa com tabela inseridos no livro

### Exercício 4.8
##a = float(input("Insira um número: "))
##b = float(input("Insira outro número: "))
##oper = input("Qual operação deseja realizar? ")
##
##soma = a + b
##multiplicação = a * b
##subtração = a - b
##divisão = a / b
##
##if oper == '+' or oper == 'soma':
##    print("O resultado é: %2.f" %soma)
##elif oper == '*' or oper == 'multiplicação':
##    resultado = a * b
##    print("O resultado é: %2.f" %multiplicação)
##elif oper == '-' or oper == 'subtração':
##    resultado = a - b
##    print("O resultado é: %2.f" %subtração)
##elif oper == '/' or oper == 'divisão':
##    resultado = a / b
##    print("O resultado é: %2.f" %divisão)

### Exercício 4.9
##valor = float(input("Valor da casa: "))
##salario = float(input("Salário: "))
##n_anos = float(input("Nº de prestações: "))
##prestação = valor / (n_anos*12)
##if prestação < (0.30 * salario):
##    print ("Empréstimo aprovado")
##else:
##    print("Empréstimo negado")

# Exercício 4.10
qtde = float(input("Qtde. de kWh consumidas: "))
tipo = input("Tipo de instalação (R - residencial, I - indústrial ou C - comercial): ")
if tipo == 'R':
    if qtde < 500:
        preço = qtde * 0.40
        print ("Valor a pagar: %2.f" %preço)
    else:
        preço = qtde * 0.65
        print ("Valor a pagar: %2.f" %preço)
elif tipo == 'I':
    if qtde < 1000:
        preço = qtde * 0.55
        print ("Valor a pagar: %2.f" %preço)
    else:
        preço = qtde * 0.60
        print ("Valor a pagar: %2.f" %preço)
elif tipo == 'C':
    if qtde < 5000:
        preço = qtde * 0.55
        print ("Valor a pagar: %2.f" %preço)
    else:
        preço = qtde * 0.60
        print ("Valor a pagar: %2.f" %preço)
    
        

 
    
    
