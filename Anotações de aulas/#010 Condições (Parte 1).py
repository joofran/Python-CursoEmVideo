# -*- coding: utf-8 -*-
"""
Created on Mon Mar  2 22:11:44 2020

@author: jfpas
"""

"""
carro.siga()
objeto -> carro
método -> .siga() -> método sempre possui parenteses

-------------------Condições---------------------------------------------------
if:
    blabla
    nlasadl
    blabla
else:
    blebleble
    bleble
    lelkal

ESTRUTURA CONDICIONAL SIMPLES
utiliza-se somente if para estrutura simples 

ESTRUTURA CONDICIONAL COMPOSTA
utiliza-se else quando se trata de estrutura composta
"""


nome = str(input('Qual é seu nome? '))
if nome == 'João':
    print('E aí garoto?!')
else:
    print('Vaza, {}'.format(nome))
print('É isso aí')

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1+n2)/2
print('Sua média foi {:.1f}'.format(m))

if m >= 5:
    print('Você passou. Parabéns!')
else:
    print('Você não passou. Tente com mais afinco da próxima vez.')

"""
Desafio 028 - Escreva um programa que faça o computador "pensar" em um número
inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número 
escolhido pelo computador.

O programa deverá escrever na tela se o usuário venceu ou perdeu.
"""

from random import randint
from time import sleep
n_pc = randint(0,5)
n_usu = int(input('Tente acertar o número que pensei entre 0 e 5: '))
print('PROCESSANDO...')

sleep(2)

if n_usu == n_pc:
    print('Parabéns, você acertou!!!')
else:
    print('Não foi dessa vez. Pensei no número {}. \nTente novamente!'
          .format(n_pc))


"""
Desafio 029 - Escreva um programa que leia a velocidade de um carro.
Se ele ultrapassar 80km/h, mostre uma mensagem dizendo que ele foi multado.
A multa vai custar R$ 7,00 por cada Km acima do limite.
"""
v_carro = float(input('Qual a velocidade do carro? '))
v_multa = ((v_carro - 80)*7)

if v_carro > 80:
    print('O valor da sua multa é: R$ {:.2f}'.format(v_multa))
else:
    print('Parabéns, seu carro não foi multado!')

"""
Desafio 030 - Crie um programa que leia um número interio e mostre na tela se 
ele é PAR ou ÍMPAR.
"""
n = int(input('Digite um número: '))

if n % 2 == 0:
    print('O número {} é Par'.format(n))
else:
    print('O número {} é Ímpar'.format(n))

"""
Desafio 031 - Desenvolva um programa que pergunte a distência de uma viagem em
Km. Calcule o preço da passagem, cobrando R$ 0,50 por Km para viagem de aré 
200Km e R$ 0,45 para viagens mais longas.
"""

km_viagem = float(input('Qual a distância da viagem que você deseja realizar? '))
v200 = km_viagem*0.50
v201 = km_viagem*0.45

if km_viagem <= 200:
    print('Sua viagem custará: R${:.2f}'.format(v200))
else:
    print('Sua viagem custará: R${:.2f}'.format(v201))

"""
Desafio 032 - Faça um programa que leia um ano qualquer e mostre se ele é 
BISSEXTO.
"""
ano = int(input('Digite um ano: '))

if ano % 4 == 0 and ano % 400 == 0 or ano % 100 != 0: 
    print('O ano é bissexto!!')
else:
    print('O ano não é bissexto.')

"""
Desafio 033 - Faça um programa que leia três números e mostre qual é o maior e
qual é o menor.
"""
n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
n3 = int(input('Digite o terceiro número: '))

if n3 > n1 and n3 > n2:
    print('{} é o maior número!!'.format(n3))
if n3 < n1 and n3 < n2:
    print('{} é o menor número!!'.format(n3))
if n2 > n1 and n2 > n3:
    print('{} é o maior número!!'.format(n2))
if n2 < n1 and n2 < n3:
    print('{} é o menor número!!'.format(n2))
if n1 > n2 and n1 > n3:
    print('{} é o maior número!!'.format(n1))
if n1 < n2 and n1 < n3:
    print('{} é o menor número!!'.format(n1))

#Forma mais simples de escrever
menor = n1
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3
maior = n1
if n2 > n1 and n2 > n1:
    maior = n2
if n3 > n1 and n3 > n2:
    maior = n3
print('O maior número é {}'.format(maior))
print('O menor número é {}'.format(menor))

"""
Desafio 034 - Escreva um programa que pergunte o salário de um funcionário e
calcule o valor de seu aumento.

Para salários superiores a R$1.250,00, calcule um aumento de 10%
Para salários inferiores ou iguais, o aumento é de 15%.
"""
sal = float(input('Qual o seu salário? R$ '))
a1_sal = sal*1.15
a2_sal = sal*1.1

if sal > 1250.00:
    print('Seu salário é {} e com o aumento ficará {:.2f}'.format(sal,a2_sal))
else:
    print('Seu salário é R$ {} e com o aumento ficará {:.2f}'
          .format(sal,a1_sal))
  
"""
Desafio 035 - Desenvolva um programa que leia o comprimento de três retas e
diga ao usuário se elas podem formar um triângulo
"""
import math
a = float(input('Insira o primeiro lado do triângulo: '))
b = float(input('Insira o segundo lado do triângulo: '))
c = float(input('Insira o terceiro lado do triângulo: '))

cond1 = math.fabs(b - c) < a < b + c
cond2 = math.fabs(a - c) < b < a + c
cond3 = math.fabs(a - b) < c < a + b

if cond1 and cond2 and cond3 is True:
    print('Os valores que você inseriu retornam um triângulo')
else:
    print('Os valores que você inseriu não formam um triângulo')







