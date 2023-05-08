### Exercício 4.1
### O que acontece se a for igual a b? 
##a = int(input("Digite um número: "))
##b = int(input("Digite um número: "))
##if a > b:
##    print("O primeiro número é maior")
##if a < b:
##    print("O segundo número é maior")
### Caso a seja igual b, o programa não devolve nenhuma resposta


# Exercício 4.2
vel = int(input("Qual a velocidade do carro? "))
if vel > 80:
    val = (vel - 80) * 5
    print("Eba, você foi multado :D")
    print("O valor da sua multa é R$%.2f" % val)
    
