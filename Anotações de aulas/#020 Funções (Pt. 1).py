# -*- coding: utf-8 -*-
"""
Created on Mon Jun  8 16:01:14 2020

@author: jfpas
"""

"""
Função é uma rotina padronizada que utilizamos no código.

O python já traz uma série de funções:
    int(); print(); float()...

def mostraLinha():
    print('-'*30)

def mensagem(msg):
    print('-'*30)
    print(msg)
    print('-'*30)
"""

# Exemplo 1:
def mensagem(msg):
    print('-'*30)
    print(msg)
    print('-'*30)
    
mensagem('oi')

# Exemplo 2:
def soma(a, b):
    s = a + b
    print(s)
    
soma(4,5)

# Exemplo 3: Tem como não especificar os valores que serão inseridos em uma 
# função utilizando o comando asterisco
def contador(* núm):
    print(núm)

contador(2, 4)
contador(1, 4 , 8)

# Exemplo 4:
def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1

valores = [1, 2, 3, 4]

dobra(valores)
print(valores)

"""
Desafio 096 - Faça um progama que tenha uma função chamada área(), que receba 
as dimensões de um terreno retangular (largura e comprimento) e mostre a área
do terreno.
"""
def área(largura, comprimento):
    área = largura * comprimento
    print(área)
    
área(2,5)

"""
Desafio 097 - Faça um programa que tenha uma função chamada escreva(), que 
receba um texto qualquer como parâmetro e mostre uma mensagem com tamanho 
adaptável.
"""

def escreva(msg):
    print('-'*len(msg))
    print(msg)
    print('-'*len(msg))

"""
Desafio 098 - Faça uma programa que tenha uma função chamada contador que 
receba três parâmetros: início, fim e passo e realize a contagem.

Seu programa tem que realizar três contagens através da funçãao criada:
    
    a) de 1 até 10, de 1 em 1
    b) de  10 até 0, de 2 em 2
    c) uma contagem personalizada.
"""
from time import sleep 

def contagem(a, b, c):
    if c == 0:
        c = 1
    if a < b:
        while a <= b:
            print(a, end = ' ')
            a += c
            sleep(0.5)
    elif b < a:
        while b <= a:
            print(a, end = ' ')
            if c > 0:
                a -= c
            elif c < 0:
                a += c
            sleep(0.5)
    print()
    print('Fim')


i = 0
print('-=' * 10)
print('Contagem de 1 até 10:')
print('-' * 20)
while i <= 10:
    print(i, end = ' ')
    i += 1
    sleep(1)
print('\nFim')
i = 10
print('-' * 20)
print('Contagem de 10 até 0:')
while i >= 0:
    print(i, end = ' ')
    i -= 2
    sleep(1)
print()
print('-' * 20)
print('\nFim')

print('Contagem personalizada:')
a = int(input('Número inicial: '))
b = int(input('Número Final: '))
c = int(input('Passo da contagem: '))

contagem(a, b, c)
    

"""
Desafio 099 - Faça um programa que tenha uma função maior() que receba vários 
parâmetros com valores inteiros. 

Seu programa tem que analisar todos os valores e dizer qual é o maior.
"""
def maior(*num):
    m = 0
    print('Analisando os números: ')
    for n in num: 
        print(n, end = ' ')
        if n > m:
            m = n
        sleep(0.5)
    print('\nAnalisado!!!')
    print(f'O maior número é {m}')
maior(9, 7, 8, 12, 2, 67, 8)

"""
Desafio 100 - Faça um programa que tenha uma lista chamada de números e duas
funções chamadas sorteia() e somaPar(). A prieira função vai sortear 5 números 
e vai coloca-los dentro da lista e a segunda função vai mostrar a soma entre 
todos os valores PARES sorteados pela função anterior.
"""
from random import randint

def sorteia():
    lst = []
    for i in range(0, 5):
        x = randint(0, 100)
        lst.append(x)
    print(lst)
    
def somaPar(lst):
    sp = 0
    for n in lst:
        if n % 2 == 0:
            sp += n
    if sp != 0:
        print(f'A soma dos números pares foi {sp}')
    else:
        print('Não houveram números pares a serem somados')
    
somaPar(sorteia())
