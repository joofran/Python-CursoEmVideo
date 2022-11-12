# -*- coding: utf-8 -*-
"""
Created on Sun Feb 16 19:51:16 2020

@author: jfpas
"""

print('Olá, Mundo!')

print(7+4)

print('7' + '4')

print('7+4')

print('ola', 5)

#print('ola' + 5) -> ERRO, string + número

# No Python, toda uma variável é um objeto
# Toda variável RECBE um valor na fomra do símbolo '='
nome = 'Guanabara'
idade = 25
peso = 75,8

print(nome,idade,peso)
#print(nome + idade + peso) -> ERRO, string + número

nome = input('Qual é seu nome? ')
idade = input('Quantos anos você tem? ')
peso = input('Quanto você pesa? ')

print(nome, idade, peso)

#Desafio 01

nome=input('Qual o seu nome? ')

print('Bem vindo', nome)

#Desafio 02

dia=input('Qual dia você nasceu?')
mês=input('Que mês você nasceu?')
ano=input('Qual ano você nasceu?')

print('Você nasceu no dia', dia, 'de', mês, 'de', ano)

#Desafio 3

prim_num=input('Qual o primeiro número?')
seg_num=input('Qual é o segundo número?')

print('A soma é', prim_num + seg_num)
