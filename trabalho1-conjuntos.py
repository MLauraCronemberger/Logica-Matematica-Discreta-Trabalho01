import random

conjuntoA = set()
conjuntoB = set()

while True:
    elementosA = input("Escreva abaixo um conjunto que contenha de 4 a 8 elementos, separados por vírgula: ")

    elementosConjuntoA = elementosA.split(',')
    elementosConjuntoA = [int(e) for e in elementosConjuntoA]

    # Verifica se tem repetido
    if len(elementosConjuntoA) != len(set(elementosConjuntoA)):
        print("Não pode haver números repetidos. Digite novamente.\n")
        continue

# Verifica se tem entre 4 e 8 elementos
    if 4 <= len(elementosConjuntoA) <= 8:
        for elemento in elementosConjuntoA:
            conjuntoA.add(elemento)
        print("Conjunto A:", conjuntoA)
        break

    else:
        print("O conjunto deve ter entre 4 e 8 elementos.\n")
        continue

numero = random.randint(4, 8) 
# print(numero)

while len(conjuntoB) < numero:
    elementoAleatorio = random.randint(0, 9)
    conjuntoB.add(elementoAleatorio)

print("Conjunto B:", conjuntoB)

uniaoConjuntos= conjuntoA.union(conjuntoB)
print("A∪B=", uniaoConjuntos)

intersecaoConjuntos= conjuntoA.intersection(conjuntoB)
print("A∩B=", intersecaoConjuntos)

diferencaAB= conjuntoA.difference(conjuntoB)
print("A-B=", diferencaAB)

diferencaBA= conjuntoB.difference(conjuntoA)
print("B-A=", diferencaBA)

diferencaSimetrica= conjuntoA.symmetric_difference(conjuntoB)
print("AΔB=", diferencaSimetrica)

cardinalidadeA= len(conjuntoA) + 1
print("|A|=", cardinalidadeA)

cardinalidadeB= len(conjuntoB) + 1
print("|B|=", cardinalidadeB)

cardinalidadeAB= len(uniaoConjuntos) + 1
print("|A∪B|=", cardinalidadeAB)
