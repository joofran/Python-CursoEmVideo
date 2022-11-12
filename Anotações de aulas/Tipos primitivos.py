# -*- coding: utf-8 -*-
"""
Created on Thu Feb 20 16:25:09 2020

@author: jfpas
"""

"""
Tipos Primitivos e saída de dados

int - [7;-4;0;9875] números inteiros
float - [4.5;0.076;-12.223;7.0] números reais (ou números de pontos flutuantes)
bool - [Trur;False] booleanos (valores lógicos) -> Obs.: sempre em maiúsculo
str - string ['Olá, mundo';'7.5';''] (valores caracteres)

*A função type() nos retorna o tipo do dado em questão
"""
#Uma forma diferente de se trabalhar com o print
n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o segundo valor: '))

s = n1 + n2

#print('A soma entre', n1, 'e', n2, 'vale',s)
print('A soma entre {} e {} vale {}'.format(n1,n2,s))

n = bool(input('Digite um valor: '))
print(n)

#Descobrindo se um valor é númerico 

x = input('Digite algo: ')
print(x.isnumeric())

#( existe uma série de outras validações)
# esse comando nos mostra 

p = input('Digite algo: ')
print(p.isupper())