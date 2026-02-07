# Atividade Prática - Teoria dos Conjuntos em Python

Este repositório contém a implementação de assuntos vistos na Unidade 1 da disciplina de *Lógica e Matemática Discreta*, no que diz respeito ao assunto de **Teoria dos Conjuntos**.


## 📋 Descrição do Problema

Este programa implementa operações fundamentais da teoria dos conjuntos utilizando Python. O objetivo é demonstrar na prática os conceitos de união, interseção, diferença, diferença simétrica entre conjuntos e cardinalidade.

O programa trabalha com dois conjuntos:
- **Conjunto A**: Definido pelo usuário (entrada manual)
- **Conjunto B**: Gerado randomicamente pelo programa

Ambos os conjuntos devem conter entre 4 e 8 elementos numéricos inteiros, sem repetições.

## 🎯 Objetivo

Aplicar os conceitos de teoria dos conjuntos estudados em Lógica e Matemática Discreta, implementando:
- União (A ∪ B)
- Interseção (A ∩ B)
- Diferença (A - B e B - A)
- Diferença Simétrica (A Δ B)
- Cardinalidade (|A|, |B|, |A ∪ B|)

## 🚀 Como Executar

### Pré-requisitos
- Python 3.6 ou superior instalado

### Dependências
O programa utiliza apenas uma biblioteca padrão do Python:
- `random` (para geração do conjunto aleatório)

Não é necessário instalar pacotes adicionais.

### Execução

1. Clone este repositório ou baixe o arquivo `trabalho1-conjuntos.py`
2. Abra o terminal na pasta do projeto
3. Execute o comando:

```bash
python trabalho1-conjuntos.py
```

4. Siga as instruções na tela:
   - Digite de 4 a 8 números inteiros separados por vírgula
   - Exemplo: `1,2,3,4,5`

## 📊 Exemplo de Execução

```
Escreva abaixo um conjunto que contenha de 4 a 8 elementos, separados por vírgula: 1,2,3,4,5
Conjunto A: {1, 2, 3, 4, 5}
Conjunto B: {0, 2, 4, 6, 8}
A ∪ B= {0, 1, 2, 3, 4, 5, 6, 8}
A ∩ B= {2, 4}
A - B= {1, 3, 5}
B - A= {0, 8, 6}
A Δ B= {0, 1, 3, 5, 6, 8}
|A|= 5
|B|= 5
|A ∪ B|= 8
```

## 🔧 Estrutura do Código

O programa está organizado de forma sequencial:

### 1. Inicialização dos Conjuntos
```python
conjuntoA = set()
conjuntoB = set()
```
Criação dos conjuntos vazios que serão preenchidos ao longo do programa.

### 2. Entrada do Usuário (Conjunto A)
- Solicita ao usuário um conjunto de 4 a 8 elementos
- Valida se não há elementos repetidos
- Valida se a quantidade está no intervalo permitido
- Converte a entrada em um conjunto Python (`set`)

### 3. Geração Aleatória (Conjunto B)
- Gera aleatoriamente um número entre 4 e 8 (cardinalidade do conjunto B)
- Preenche o conjunto com números aleatórios de 0 a 9
- Utiliza `set` para evitar automaticamente duplicatas e para converter tudo para um conjunto Python

### 4. Operações de Conjuntos
Implementa todas as operações solicitadas:
- **União**: `conjuntoA.union(conjuntoB)`
- **Interseção**: `conjuntoA.intersection(conjuntoB)`
- **Diferença A-B**: `conjuntoA.difference(conjuntoB)`
- **Diferença B-A**: `conjuntoB.difference(conjuntoA)`
- **Diferença Simétrica**: `conjuntoA.symmetric_difference(conjuntoB)`

### 5. Cálculo de Cardinalidades
- Cardinalidade de A: `len(conjuntoA)-1`
- Cardinalidade de B: `len(conjuntoB)-1`
- Cardinalidade da União: `len(uniaoConjuntos)-1`

## 📚 Conceitos de Teoria dos Conjuntos Aplicados

### União (A ∪ B)
Retorna todos os elementos que pertencem a A **ou** a B (ou ambos). No código, utilizamos o método `.union()` do Python.

### Interseção (A ∩ B)
Retorna apenas os elementos que pertencem simultaneamente a A **e** a B. Implementado com `.intersection()`.

### Diferença (A - B)
Retorna os elementos que estão em A mas **não** estão em B. Utilizamos `.difference()`.

### Diferença (B - A)
Retorna os elementos que estão em B mas **não** estão em A. Utilizamos `.difference()`.

### Diferença Simétrica (A Δ B)
Retorna os elementos que pertencem a A **ou** a B, mas **não** a ambos. É equivalente a (A - B) ∪ (B - A). Implementado com `.symmetric_difference()`.

### Cardinalidade
Representa o número de elementos em um conjunto. Em Python, obtemos através da função `len()`.

## 💡 Escolha da Estrutura de Dados

O programa utiliza o tipo `set` (conjunto) nativo do Python para representar os conjuntos matemáticos. Esta escolha deve-se à simplificação da implementação do código, já que o Python oferece métodos prontos para todas as operações solicitadas (`.union()`, `.intersection()`, `.difference()`, etc.) e garante automaticamente a ausência de elementos duplicados.

Se fossem utilizadas listas ou arrays, seria necessário implementar manualmente todas essas operações com loops e verificações, tornando o código mais extenso e complexo.

## 📝 Observações

- Os elementos dos conjuntos são **números inteiros**  
- Não são permitidos elementos duplicados (validação implementada)  
- A quantidade de elementos do conjunto B é gerada em um intervalo de 4 a 8 elementos  
- O conjunto B é gerado com números no intervalo [0, 9]
- O uso do tipo `set` garante que todas as operações respeitam as propriedades matemáticas dos conjuntos e que nenhum número seja duplicado

## 👥 Créditos

**Aluna:** Maria Laura Rangel Urbano Cronemberger  
**Disciplina:** EECP0015 — Lógica e Matemática Discreta    
**Professor:** Prof. Rondineli Seba  
**Instituição:** UFMA — Universidade Federal do Maranhão  
**Semestre:** 2025.4  

---

<div align="center">

**Este repositório possui fins acadêmicos e educacionais.**