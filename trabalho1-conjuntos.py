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




