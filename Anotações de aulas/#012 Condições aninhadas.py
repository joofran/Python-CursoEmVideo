# -*- coding: utf-8 -*-
"""
Created on Tue Mar 10 21:47:07 2020

@author: jfpas
"""

"""
Condições aninhadas 
if:
    blablab
elif:
    blablabla
else:
    bleblebble


OBS.:
    A diferença de uma etrutura condicional formada por varios if e outra 
    formada por if:
        - Quando se é com vários if: todos os if serão rodados se tiverem suas 
        condições atendidas
    formada por elif:
        - O elif só é rodado quando não se atende nenhum if

Portanto:
    if: 1ª ordem de precedência
    elif: 2ª ordem de precedência
    else: 3º ordem de precedência
"""
nome = str(input('Qual é seu nome? '))
if nome == 'João':
    print('Que nome lindo')
elif nome == 'José' or nome == 'Malu':
    print('Seu nome é tão bonito quão João')
else:
    print('Seu nome não é tão bonito quando João')
print('Tenha um bom dia {}!!!'.format(nome))


"""
Desafio 036 - Escreva um progama para aprovar o empréstimo bancário para a 
compra de uma casa. O programa vai perguntar o valor da casa, o salário do 
comprador e em quantos anos ele vai pagar.

Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do
salário ou então o empréstimo será negado.
"""

valor_casa = float(input('Quanto custa a casa que você deseja comprar? '))
salário_comp = float(input('Quanto você ganha por mês? '))
anos_pg = int(input('Em quantos anos você pretende pagar a casa? '))

prestação = valor_casa/(anos_pg*12)

print('O valor da prestação é {:.2f}'.format(prestação))

if prestação <= 0.3*salário_comp:
    print('Parabéns!!! Você poderá realizar dado que a prestação de R$ {:.2f} '
          'é inferior a 30% de seu salário'.format(prestação))
else:
    print('Infelizmente você não pode realizar o empréstimo com as condições'
          'informadas')

"""
Desafio 037 - Escreva um programa que leia um número inteiro qualquer e 
peça para o usuário qual será a base de conversão:
     - 1 para binário
     - 2 para octal
     - 3 para hexadecimal
"""

N = int(input('Digite o número que você deseja converter: '))
print('Você deseja convertar o número em qual base de conversão? \n'
      '[ 1 ] Binária \n' '[ 2 ] Octal \n' '[ 3 ] Hexadecimal')
op = int(input('Digite o número da opção de conversão que você deseja: '))

if op == 1:
    print('Você escolheu a base de conversão Binária \nO número fica {}: {}')
elif op == 2:
      print('Você escolheu a base de conversão Octal \nO número fica{}: {}')
elif op == 3:
      print('Você escolheu a base de conversão Hexadecimal \nO número '
            'fica {}: {}')
else:
    print('A opção escolhida não corresponde a nenhuma das bases de conversão '
          'disponíveis')
    
#NÃO SEI BASES NÚMERICAS. PRECISO VER O VIDEO QUE ENSINA ISSO

"""
Desafio 038 - Escreva um programa que leia dois números inteiros e compare-os, 
mostrando na tela uma mensagem:
    - o primeiro valor é maior
    - o segundo valor é maior 
    - Não existe valor maior, os dois são iguais
"""
n1 = float(input('Insira o primeiro valor: '))
n2 = float(input('Insira o segundo valor: '))

if n1 > n2:
    print('O primeiro valor {} é o maior'.format(n1))
elif n2 > n1:
    print('O segundo valor {} é o maior'.format(n2))
else:
    print('Não existe valor maior, ambos são iguais')

"""
Desafio 039 - Faça um programa que leia o ano de nascimento de um jovem e
informe , de acordo com sua idade:
    - Se ele ainda vai se alistar ao serviço militar.
    - Se é a hora de se alistar.
    - Se já passou o tempo do alistamento
Seu programa também deverá mostrar o tempo que falta ou passou do prazo.
"""
import datetime

today = datetime.date.today()
ano = int(today.year)

ano_nasc = int(input('Em que ano você nasceu? ' ))

if ano - ano_nasc == 18:
    print('Você faz 18 anos esse ano, portanto, deve se alistar.')
elif ano - ano_nasc < 18:
    print('Você não completará 18 anos este ano, portanto não deve se alistar.')
else:
    print('Já passou do seu período de alistamento. Procure o posto de'
          'alistamento mais próximo caso ainda não o tenha feito.')
    
"""
Desafio 040 - Crie um programa que leia duas notas de um aluno e calcule sua 
média, mostrando uma mensagem no final de acordo com a média atingida:
    - Média abaixo de 5.0:
        REPROVADO
    - Média entre 5.0 e 6.9:
        RECUPERAÇÂO
    - Média 7.0 ou superior:
        APROVADO
"""

N1 = float(input("Insira a primeira nota: "))
N2 = float(input('Insira a segunda nota: '))

média = (N1 + N2)/2
média = round(média, 1)

print('A sua média foi: {}'.format(média))
if média < 5.0:
    print('Você foi reprovado')
elif 5.0 < média < 7.0:
    print('Você está em recuperação')
else:
    print('Parabéns! Você foi aprovado!')


"""
Desafio 041 - A Confederação Nacional de Natação precisa de um programa que 
leia o ano de nascimento de um atleta e mostre a sua categora, de acordo com a 
idade:
    - Até 9 anos: MIRIM
    - Até 14 anos: INFANTIL
    - Até 20 anos: SÊNIOR
    - Acima: MASTER
"""
Id = int(input('Quantos anos o atleta possui? '))

if Id <= 9:
    print('O atleta está na categoria MIRIM')
elif 9 < Id <= 14:
    print('O atleta está na categoria INFANTIL')
elif 14 < Id <= 19:
    print('O atleta está na categoria JUNIOR')
elif 19 < Id <= 20:
    print('O atleta está na categoria SÊNIOR')
else:
    print('O atleta está na categoria MASTER')


"""
Desafio 042 - Refaça o Desafio 035 dos triêngulos, acrescentando o recurso de 
mostrar que tipo de triângulo será formado:
    - Equilátero: todos os lados iguais;
    - Isósceles: dois lados iguais;
    - Escaleno: todos os lados diferentes.
"""

import math
a = float(input('Insira o primeiro lado do triângulo: '))
b = float(input('Insira o segundo lado do triângulo: '))
c = float(input('Insira o terceiro lado do triângulo: '))

cond1 = math.fabs(b - c) < a < b + c
cond2 = math.fabs(a - c) < b < a + c
cond3 = math.fabs(a - b) < c < a + b

if cond1 and cond2 and cond3 is True and a == b == c:
    print('Os valores que você inseriu retornam um triângulo e ele é'
          ' Equilatéro')
elif cond1 and cond2 and cond3 is True and a == b or a == c or b == c:
    print('Os valores que você inseriu retornam um triângulo e ele é'
          ' Isosceles')
elif cond1 and cond2 and cond3 is True and  a != b != c:
    print('Os valores que você inseriu retornam um triângulo e ele é Escaleno')
else:
    print('Os valores que você inseriu não formam um triângulo')

"""
Desafio 043 - Desenvolva uma lógica que leia o peso e a altura de uma pessoa, 
calcule seu IMC e mostre seu status de acordo com a tabela abaixo:
    - Abaixo de 18.5: Abaixo do peso
    - Entre 18.5 e 25: Peso ideal
    - 25 até 30: Sobrepeso 
    - 30 a 40: Obesidade 
    - Acima de 40: Obesidade mórbida
"""

h = float(input('Digite a sua altura: '))
p = float(input('Digite o seu peso: '))

IMC = (p)/(h*h)

print(' Você possui IMC de {:.2f}'.format(IMC))

if IMC < 18.5:
    status = 'abaixo do peso'
if 18.5 <= IMC < 25:
    status = 'com peso ideal'
if 25 <= IMC < 30:
    status = 'com sobrepeso'
if 30 <= IMC < 40:
    status = 'com obesidade'
if IMC > 40:
    status = 'com obesidade mórbida'

print('Seu IMC indica que você está {}'.format(status))

"""
Desafio 044 - Elabore um progama que calcule o valor a ser pago por um produto,
considerando o seu preço normal e acondição de pagamento:
    - à vista dinheiro/cheque: 10% de desconto
    - à vista no cartão: 5% de desconto
    - em até 2 vezes no cartão: preço normal
    - 3x ou mais no cartão: 20% de juros
"""

valor = float(input('Qual o valor original do produto? R$ '))

print('As opções de pagamento disponíveis são as descritas abaixo:\n'
      '- [1] À vista dinheiro/cheque: 10% de desconto;\n'
      '- [2] À vista no cartão: 5% de desconto;\n'
      '- [3] Em até 2 vezes no cartão: preço normal;\n'
      '- [4] 3x ou mais no cartão: 20% de juros.')
opç = int(input('Digite a opção desejada: '))

if opç == 1:
    valor = valor*0.9
    print('O valor a ser pago pelo produto corresponde a R$ {}'.format(valor))
elif opç == 2:
    valor = valor*0.95
    print('O valor a ser pago pelo produto corresponde a R$ {}'.format(valor))
elif opç == 3:
    valor = valor
    print('O valor a ser pago pelo produto corresponde a R$ {}'.format(valor))
elif opç == 4:
    valor = valor*1.2
    print('O valor a ser pago pelo produto corresponde a R$ {}'.format(valor))
else:
    print('A opção digitada não corresponde a nenhuma das descritas')

"""
Desafio 045 - Cria um programa que faça o computador jogar jokenpô com você.
"""

from random import randint
from time import sleep

print('Olá!!! Vamos jogar Jokenpô!!! Escolha uma das opções abaixo: ')
print('[1] - Pedra \n'
      '[2] - Papel \n'
      '[3] - Tesoura')
sleep(2)
opç_pc = randint(1,3)

print('JÁ ESCOLHI')

opç_us = int(input('Você quer Pedra, Papel ou Tesoura? '))

if opç_pc == opç_us:
    print('Eu também escolhi {}! Temos um empate!'.format(opç_pc,opç_us))
elif opç_pc == 1 and opç_us == 2:
    print('Eu escolhi {} e você escolheu {}! Parabéns você ganhou!'
          .format('pedra','papel'))
elif opç_pc == 1 and opç_us == 3:
    print('Eu escolhi {} e você escolheu {}! EU GANHEI!'
          .format('pedra','tesoura'))
elif opç_pc == 2 and opç_us == 3:
    print('Eu escolhi {} e você escolheu {}! Parabéns você ganhou!'
          .format('papel','tesoura'))
elif opç_pc == 2 and opç_us == 1:
    print('Eu escolhi {} e você escolheu {}! EU GANHEI!'
          .format('papel','pedra'))
elif opç_pc == 3 and opç_us == 1:
    print('Eu escolhi {} e você escolheu {}! Parabéns você ganhou!'
          .format('tesoura','pedra'))
elif opç_pc == 3 and opç_us == 2:
    print('Eu escolhi {} e você escolheu {}! EU GANHEI!'
          .format('tesoura','papel'))
else:
    print('Você nem consegue escolher uma opção direito... \n EU GANHEI')
















