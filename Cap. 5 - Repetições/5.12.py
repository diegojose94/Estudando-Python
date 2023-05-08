# CAP. 5 - REPETIÇÕES

### Exercício 5.1
##x = 1
##while x <= 100:
##    print(x)
##    x = x + 1

### Exercício 5.2
##x = 50
##while x <= 100:
##    print(x)
##    x = x + 1

### Exercício 5.3
##x = 10
##while x >= 0:
##    print(x)
##    x = x - 1
##print("Fogo!")

## Exercício 5.4
##fim = int(input("Digite um número: "))
##x = 0
##while x <= fim:
##    print(x)
##    x = x + 2
##
##end = float(input("Digite um número: "))
##x = 0
##while x <= end:
##    if x % 2 == 0:
##        print(x)
##    x = x + 1

### Exercício 5.5 [CORRIGIR]
##fim = float(input("Digite um número: "))
##x = 0
##while x <= fim:
##    print(x)
##    x = x + 3
    
### Exercício 5.6
##n = int(input("Tabuada de: "))
##x = 0
##while x <= 10:
##    print (n*x)
##    x = x + 1

### Exercício 5.7
##n = int(input("Tabuada de: "))
##x = int(input("A partir do: "))
##y = int(input("Até o: "))
##while x <= y:
##    print(n*x)
##    x = x +1

### Exercício 5.8
##n1 = int(input("Digite um número: "))
##n2 = int(input("Digite outro número: "))
##x = 1
##y = n1
##while x <= n2:
##    print(n1)
##    n1 = n1 + y
##    x = x + 1

### Exercício 5.9
##n1 = int(input("1º número: "))
##n2 = int(input("2º valor: "))
##y = n2
##x = 0
##while n1 >= 0:
##    print (x, n1)
##    x = x + 1
##    n1 = n1 - n2

### Exercício 5.10
##pontos = 0
##questão = 1
##while questão <= 3:
##    resposta = input("Resposta da questão %d: " %questão)
##    if questão == 1 and resposta == "b" or resposta == "B":
##        pontos = pontos + 1
##    if questão == 2 and resposta == "a" or resposta == "A":
##        pontos = pontos + 1
##    if questão == 3 and resposta == "d" or resposta == "D":
##        pontos = pontos + 1
##    questão += 1
##print("O aluno fez %d ponto(s)" %pontos)

### Exercício 5.11
##dep = float(input("Depósito inicial: "))
##taxa = float(input("Taxa: "))
##x = 1
##soma = 0
##while x <= 24:
##    if taxa > 1:
##        taxa = taxa/100
##    dep = dep + (dep*taxa)
##    x = x + 1
##    print("Ganho mensal: %.2f" %dep)
##print("Total ganho com juros: %.2f" %(taxa*24))
    
# Exercício 5.12
dep = float(input("Depósito inicial: "))

                
