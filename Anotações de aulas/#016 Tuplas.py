# -*- coding: utf-8 -*-
"""
Created on Wed Apr 15 13:42:31 2020

@author: jfpas
"""

"""
A partir de agora aprenderemos variáveis compostas. Estas são as que existem:
    - tuplas      -> ()
    - listas      -> []
    - dicionários -> {}
Começamos tuplas com parenteses. Listas com colchetes. Dicionários com chaves

No Python mais atualizado não há necessidade de parenteses para tuplas

Os elementos da variável composta são identificados por índices numéricos, a 
exemplo das listas:
    
VARIÁVEL
01234567

A aula 16 diz respeito às tuplas



========TUPLAS=================================================================

As tuplas são imutáveis

"""

lanche = ('Hambúrguer', 'Suco', 'Pizza', 'Pudim')
# Não há mais necessidade de parenteses para tuplas, portanto:
lanche = 'Hambúrguer', 'Suco', 'Pizza', 'Pudim'

print(lanche) # ('Hambúrguer', 'Suco', 'Pizza', 'Pudim')
print(lanche[1]) # Suco
print(lanche[3]) # Pudim

# OS PRIMEIROS TERMOS NO PYTHON SEMPRE COMEÇAM COM 0
print(lanche[0]) #imprimirá o Hambúrguer

#Quando começamos com número negativo a tuplas é lida de traz pra frente
#Imprimir o elemento -2:
print(lanche[-2]) #Pizza

#Imprimir do elemento 1 até o 3 (O último elemento 3 fica de fora):
print(lanche[1:3]) #('Suco', 'Pizza')

# Imprimir do elemento 2 até o final:
print(lanche[2:]) #('Pizza', 'Pudim')

# Imprimir do inicio até o elemento 2 (O último elemento 2 é desconsiderado):
print(lanche[:2]) #('Hambúrguer', 'Suco')

#Imprimir do elemento -2 até o final:
print(lanche[-2:]) #('Pizza', 'Pudim')

#PROVANDO QUE TUPLAS SÃO IMUTÁVEIS:
lanche[1] = 'Refrigerante'
print(lanche[1])


# =============================================================================

#TUPLAS COM FOR:
for comida in lanche:
    print(f'Eu vou comer {comida}')
print('COMI PRA CARAMBA')

#Retornando os índices da tuplas
for comida in range(0, len(lanche)):
    print(comida)

#Retornando novamente o que cada índice representa:
for comida in range(0, len(lanche)):
    print(lanche[comida])

#Caso seja necessária saber a posição de cada elemento e eu não quiser utilizar
#range
for pos, comida in enumerate(lanche):
    print(f'Vou comer {comida} na posição {pos}')

#COLOCANDO UMA TUPLA EM ORDEM:
print(sorted(lanche)) # ['Hambúrguer', 'Pizza', 'Pudim', 'Suco']

#JUNTANDO TUPLAS
a = (2, 5, 4)
b = (5, 8, 1, 2)
c = a + b
d = b + a

# PERCBA QUE c != d
print(c) #(2, 5, 4, 5, 8, 1, 2)
print(d) #(5, 8, 1, 2, 2, 5, 4)

#CONTANDO elementos da tuplas:
print(c.count(5)) # 2

#Descobrindo a posição de um elemento
print(c.index(8)) # 4
print(c.index(2)) # 0 -> pega a primeira vez que o termo em questão apareceu

#Devolve a posição do 2 a partir da posição 1 (Existem dois 2)
print(c.index(2, 1)) # 6 

#PODEMOS APAGAR TUPLA, apesar de que não podemos altera-las

del(c)
print(c) #NameError: name 'c' is not defined

#Deletar apenas um item é impossível
del(d[0]) #TypeError: 'tuple' object doesn't support item deletion

# =============================================================================
# AS VARIÁVEIS DO PYTHON ACEITAM ELEMENTOS DE QUALQUER TIPO MISTURADAS
# =============================================================================

#Na Tupla abaixo temos string, int e float:
pessoas = ('Gustavo', 39, 'M', 99.98)
print(pessoas) #('Gustavo', 39, 'M', 99.98)


"""
Desafio 072 - Crie um progama que tenha uma tupla totalmente preenchida por uma 
contagem por extenso, de zero até vinte.

Seu progama deverá ler um número pelo teclado (entre 0 e 20) e mostrálo por
extenso.
"""

n = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito',
'nove', 'dez', 'onze', 'doze', 'treze','catorze', 'quinze', 'dezesseis',
'dezessete', 'dezoito', 'dezenove', 'vinte')

num = int(input('Digite um valor entre 0 e 20: '))
while num > 20 or num < 0:
    num = int(input('Digite um valor entre 0 e 20: '))
print(f'Você digitou o número {n[num]}')

"""
Desafio 073 - Crie uma tupla preenchida com os 20 primeiros colocados da tabela
do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:
    A) Apenas os 5 primeiros colocados;
    B) Os últimos 4 colocados da tabela.
    C) Uma lista com os times em ordem alfabética;
    D) Em que posição da tabela está o time da Chapecoense.
"""
Brasileirão = ('FLAMENGO', 'SANTOS', 'PALMEIRAS', 'GRÊMIO', 'ATHLETICO', 
'SÃO PAULO', 'INTERNACIONAL', 'CORINTHIANS', 'FORTALEZA', 'GOIÁS', 'BAHIA', 
'VASCO', 'ATLÉTICO-MG', 'FLUMINENSE', 'BOTAFOGO', 'CEARÁ', 'CRUZEIRO', 'CSA', 
'CHAPECOENSE', 'AVAÍ')

print(f'Os cincosn Primeiros colocados são: \n{Brasileirão[0:5]}')
print(f'Os 4 últimos colocados são: \n{Brasileirão[-1:-5:-1]}')
print(f'Os participantes da série A em ordem alfabética:\n{sorted(Brasileirão)}')
print('Chapecoense está na {}ª posição'.format(Brasileirão.index('CHAPECOENSE')+1))

"""
Desafio 074 - Crie um progama que vai gerar 5 números aleatórios e colocar em 
uma tupla. Depois disso, mostre a listagem de números gerados e também o menor
e o maior valor que estão na tupla
"""
from random import randint

n = ()
while len(n) < 5:
    x = tuple(str(randint(0,9)))
    n = x + n
print(f'A tupla aleatória é {n}')
print(f'O menor valor é {min(n)}')
print(f'O maior valor é {max(n)}')

"""
Desafio 075 - Desenvolva um programa que leia quatro valores pelo teclado e 
guarde-os em uma tupla. no final mostre:
    a) Quantas vezes apareceu o valor 9
    b) Em que posição foi digitado o primeiro falor
    c) Quais foram os números pares
"""
x=()

while len(x) < 4:
    n = tuple(input('Digite um valor: '))
    x = x + n
print(f'O número 9 aparece {x.count("9")} vezes')
if x.index("3") is False:
    print(f'O número 3 não aparece na tupla')
else:
    print(f'O número 3 aparece na posição {x.index("3") + 1}')

#Não seo fazer a c

"""
Desafio 076 - Crie um progama que tenha uma tupla única com nomes de produtos e
seus respectivos preços, na sequência. 

No final, mostre uma listagem de preços, organizando os dados em forma tabular
"""
lista = ('caneta', 10, 'lapis', 8, 'cereja', 15)

for x in lista:
    print([x], '{:20}')

"""
Desafio 077 - Crie um progama que tenha uma tupla com várias palavras (não usar
acentos). Depois disso, você deve mostrar, para cada palavra, quais são suas 
vogais.
"""




















