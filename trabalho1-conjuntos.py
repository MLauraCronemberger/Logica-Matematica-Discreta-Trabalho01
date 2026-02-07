import random

conjuntoA = set()
conjuntoB = set()

elementosA= input("Escreva abaixo um conjunto que contenha de 4 a 8 elementos, separados por vírgula:")

elementosConjuntoA= elementosA.split(',')
elementosConjuntoA = [int(e) for e in elementosConjuntoA]

quantidadeElementos = len(elementosConjuntoA)

# Verifica se tem entre 4 e 8 elementos
if 4 <= quantidadeElementos <= 8:
    for elemento in elementosConjuntoA:
         conjuntoA.add(elemento)

    print("Conjunto A:", conjuntoA)
else:
    print("O conjunto deve ter entre 4 e 8 elementos.")

numero = random.randint(4, 8) 
print(numero)

while len(conjuntoB) < numero:
    elementoAleatorio = random.randint(0, 9)
    conjuntoB.add(elementoAleatorio)

print("Conjunto B:", conjuntoB)

uniaoConjuntos= conjuntoA.union(conjuntoB)
print("A união dos conjuntos é dada por:", uniaoConjuntos)

intersecaoConjuntos= conjuntoA.intersection(conjuntoB)
print("A intersecao dos conjuntos é dada por:", intersecaoConjuntos)
