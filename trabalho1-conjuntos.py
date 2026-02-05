import random

conjuntoA= []
conjuntoB= []

elementosA= input("Escreva abaixo um conjunto que contenha de 4 a 8 elementos, separados por vírgula:")

elementosConjuntoA= elementosA.split(',')
elementosConjuntoA = [int(e) for e in elementosConjuntoA]

quantidadeElementos = len(elementosConjuntoA)

# Verifica se tem entre 4 e 8 elementos
if 4 <= quantidadeElementos <= 8:
    for elemento in elementosConjuntoA:
        conjuntoA.append(elemento)

    print("Conjunto A:", conjuntoA)
else:
    print("O conjunto deve ter entre 4 e 8 elementos.")

numero = random.randint(4, 8) 
print(numero)

for i in range(numero):
    numeroAleatorio = random.randint(0, 10)
    conjuntoB.append(numeroAleatorio)

print("Conjunto B:", conjuntoB)
