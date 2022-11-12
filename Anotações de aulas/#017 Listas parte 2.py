# -*- coding: utf-8 -*-
"""
Created on Sat Apr 25 12:16:55 2020

@author: jfpas
"""

"""
LISTAS PARTE 2 ------------------ LISTAS COMPOSTAS (LISTAS DENTRO DE LISTAS)

Além de componentes normais, podemos inserir dentro de uma lista outra lista:
    
    1 - dados = 'Pedro', 25
    2 - pessoas = list()
    3 - pessoas.append(dados[:])

1 - Dados é uma lista com dois componentes. 'Pedro' e 25
2 - Pessoas é uma nova lista vazia
3 - Adicionamos dentro de pessoas uma cópia da lista dados.
OBS.: A estrutura dados[:] gera um fatiamento completo de dados, criando uma
cópia dela

Outra forma de declarar listas dentro de listas:
    
    pessoas = [['Pedro', 25], ['Maria', 19], ['João', 32]]


****IMPRESSÂO NAS LISTAS COMPOSTAS
print(pessoas[0][0]) -> retorna o componente 0 da lista 0
print(pessoas[1]) -> retorna a lista 1 inteira

"""

teste = list()
teste.append('Gustavo')
teste.append(40)
galera = list()
galera.append(teste[:]) #O que garante que foi feita uma cópia é o [:]
teste[0] = 'Maria'
teste[1] = 22
galera.append(teste[:])
print(galera)


galera = [['João', 19], ['Ana', 33], ['Joaquim', 13], ['Maria', 45]]
print(galera[0][0]) #João
print(galera[2][1]) #13

for p in galera:
    print(p)
"""
['João', 19]
['Ana', 33]
['Joaquim', 13]
['Maria', 45]
"""
for p in galera:
    print(p[0]) #Imprimindo apenas os nomes
"""
João
Ana
Joaquim
Maria
"""

totmai = totmen = 0
galera = list()
dado = list() #necessário para poder categorizar lista dentro de lista
for c in range(0,3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    galera.append(dado[:])
    dado.clear()
print(galera) #[['Ana ', 45], ['João ', 85], ['Pedro', 10]]
    
for p in galera:
    if p[1] >= 21:
        print(f'{p[0]} é maior de idade.')
        totmai += 1
    else:
        print(f'{p[0]} é menor de idade.')
        totmen += 1
print(f'Temos {totmai} maiores de idade e {totmen} menores de idade')

"""
Ana é maior de idade.
João é maior de idade.
Pedro é menor de idade.
Temos 6 maiores de idade e 3 menores de idade
"""

"""
Desafio 084 - Faça um progama que leia nome e peso de várias pessoas, guardando
tudo em uma lista. No final, mostre:
    
    A) Quantas pessoas foram cadastradas.
    B) Uma listagem com as pessoas mais pesadas
    C) Uma listagem com as pessoas mais leves
"""

base = []
coleta = []

while True:
    coleta.append(str(input('Nome: ')))
    coleta.append(float(input('Peso: ')))
    base.append(coleta[:])
    coleta.clear()
    cont = ' '
    while cont not in 'SN':
        cont = (str(input('Quer continuar[S/N] ?'))).upper().strip()[0]
    if cont == 'N':
        break

me = ma = 0
for i, p in enumerate(base):
    if i == 0 or p[1] <= me:
        me = p[1]
    elif p[1] >= ma:
        ma = p[1]
print(f'Você cadastrou {len(base)} pessoas.')
print(f'O maior peso foi de {ma} Kg. Peso de ', end = '')
for p in base:
    if p[1] == ma:
        print(p[0], end = ' ')
print()
print(f'O maior peso foi de {me} Kg. Peso de ', end = '')
for p in base:
    if p[1] == me:
        print(p[0], end = ' ')


"""
Desafio 085 - Crie um progama onde o usuário possa digitar sete valores 
numéricos e cadastre-os em uma lista única que mantenha separados os valores 
pares e ímpares. No final, mostre os valores pares e ímpares em ordem crescente
"""

coleta = []
i = []
p = []
num = [p, i]
for c in range(0,7):
    coleta.append(int(input(f'Digite o {c+1}º valor: ')))
    if coleta[0] % 2 == 0:
        p.append(coleta[:])
    else:
        i.append(coleta[:])
    coleta.clear()
p.sort()
print(f'Os valores pares digitados são {p}')
i.sort()
print(f'Os valores ímpares digitados são {i}')

"""
Desafio 086 - Crie um progama que crie uma matriz de dimensão 3x3 e preencha 
com valores lidos pelo teclado.

No final mostre a matriz na tela, com a formatação correta.
"""

matriz = []
coleta = []
for c in range(0,3):
    for v in range(0,3):
        coleta.append(int(input(f'Digite um valor pra {[c, v]}: ')))
    matriz.append(coleta[0:3])
    coleta.clear()
for l in matriz:
    print(l)

"""
Desafio 087 - Aprimore o desafio anterior, mostrando no final: 
    A) A soma de todos os valores pares digitados. 
    B) A soma dos valores da terceira coluna.
    C) O maior valor da segunda linha.
"""
matriz = []
coleta = []
spa = s3 = ma = 0 
for c in range(0,3):
    for v in range(0,3):
        coleta.append(int(input(f'Digite um valor pra {[c, v]}: ')))
    matriz.append(coleta[0:3])
    coleta.clear()
for l in matriz:
    print(l)

for x, y in enumerate(matriz):
    for z, f in enumerate(y):
        if y[z] % 2 == 0:
            spa += y[z]
        if x == 2:
            s3 += y[z]
        elif x == 1:
            if y[z] > ma:
                ma = y[z]
print(f'A soma dos valores pares é {spa}.')
print(f'A soma dos valores da terceira coluna é {s3}')
print(f'O maior valor da segunda linha é {ma}')


"""
Desafio 088 - Faça um progama que ajude um jogador da MEGA SENA a criar 
palpites. O progama vai perguntar quantos jogos serão gerados e vai sortear 6 
números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.
"""
from random import randint
from time import sleep

j = []
T = []
n = int(input('Quantos jogos de Mega-Sena você deseja? '))
for c in range(0,n):
    while len(j) < 6:
        x = [randint(1,60)]
        if x not in j:
            j.append(x[:])
        x.clear()
    T.append(j[:])
    j.clear()
print(f'Você solicitou {n} jogos e eles são: ')    
for i, x in enumerate(T):
    print(f'Jogo {i+1}: {x}')
    sleep(0.5)


"""
Desafio 089 - Crie um progama que leia nome e duas notas de vários alunos e 
guarde tudo em uma lista composta. No final, mostre um boletim contendo a 
média de cada um e permita que o usuário possa mostrar as notas de cada aluno 
individualmente.
"""

BASE = []
aluno = []
nota = []
while True:
    nome = str(input('Digite o nome: '))
    aluno.append(nome)
    for c in range(1, 3):
        n = float(input(f'Digite a {c}ª nota: '))
        nota.append(n)
    aluno.append(nota[:])
    nota.clear()
    BASE.append(aluno[:])
    aluno.clear()
    continuação = ' '
    while continuação not in 'SN':
        continuação = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if continuação == 'N':
        break
print()
print(f'{"Nº":4} {"Nome":<10} {"MÉDIA":4}')
print('-='*15)
for i, a in enumerate(BASE):
    print(f'{i:<4} {a[0]:<10} {(a[1][0] + a[1][1])/2:.2f}')
print('-='*15)

x = int(input('Você deseja saber as notas de qual aluno? '))

print(f'As notas de {BASE[x][0]} são {BASE[x][1][0]} e {BASE[x][1][1]}')


#GUANABARA
ficha = []
while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    média = (nota1 + nota2) /2
    ficha.append([nome, [nota1, nota2], média])
    continuação = ' '
    while continuação not in 'SN':
        continuação = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if continuação == 'N':
        break
print(f'{"Nº":4} {"Nome":<10} {"MÉDIA":4}')
print('-='*15)
for i, a in enumerate(ficha):
    print(f'{i:<4} {a[0]:<10} {a[2]:>.2f}')
print('-='*15)

x = int(input('Você deseja saber as notas de qual aluno? '))
print(f'As notas de {ficha[0][0]} são {ficha[0][1][0]} e {ficha[0][1][1]}')




