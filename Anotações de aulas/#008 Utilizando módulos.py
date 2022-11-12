# -*- coding: utf-8 -*-
"""
Created on Wed Feb 26 23:04:17 2020

@author: jfpas
"""

#OBS.: para importar um comando especifico do modulo utilize from
import math
num = int(input('Digite um número: '))
raiz = math.sqrt(num)
print('Araiz de {} é igual a {}'.format(num,raiz))


#OBS Não sei como importar bibliotecas que nçao estão no Python pelo spider.
import emoji
print(emoji.emojize('Olá, mundo :sunglasses'))

"""
Desafio 016 - Crie um progrma que leia um número Real qualquer pelo teclado e 
mostre na tela a sua porção inteira
Exemplo: Digite um número 6.127
O número 6.127 tem a parte inteira 6
"""
import math

f = float(input('Digite o número que você deseja transformar em inteiro: '))
i = math.floor(f)

print('O número {} tem como parte inteira {}'.format(f,i))

#outra forma

f = float(input('Digite o número que você deseja transformar em inteiro: '))
i = int(f//1)

print('O número {} tem como parte inteira {}'.format(f,i))

"""
Desafio 17 - Faça um programa que leia o comprimento do cateto oposto e do 
caateto adjacente de um triângulo retângulo, calcule e mostre o comprimento da 
hipotenusa
"""

import math
cat1 = float(input('Quanto é o primeiro cateto? '))
cat2 = float(input('Quanto é o segundo cateto? '))
hip = math.hypot(cat1,cat2)

print('A hipotenusa do triângulo com catetos {} e {} é igual a {}'
      .format(cat1,cat2,hip))

"""
Desafio 18 - Faça um programa que leia um ângulo qualquer e mostre na tela o 
valor do sen, cosseno e tangente desse ângulo.
"""

ang = float(input('Qual o ângulo que você deseja saber os valores? '))
sen = math.sin(ang)
cos = math.cos(ang)
tg = math.tan(ang)

print('O ângulo {} tem como seno, {}. Como cosseno, {}.'
        'Como tangente ele possui{}'.format(ang,sen,cos,tg))

"""
Desafio 019 - Um professor quer sortear um dos seus quatro alunos para apagar o
 quadro. Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome escolhido.
"""

import random

um = input('Qual o nome do primeiro aluno? ')
dois = input('Qual o nome do segundo aluno? ')
três = input('Qual o nome do terceiro aluno? ')
quatro = input('Qual o nome do quarto aluno? ')

lista = [um, dois, três, quatro]
escolha = random.choice(lista)

print('O aluno escolhido foi: {}'.format(escolha))

"""
Desafio 020 - O mesmo professor do desafio anterior quer sortear a ordem de 
apresentação de trabalhos dos alunos. Faça um programa que leia o nome dos 
quatro alunos e mostre a ordem sorteada.
"""
sorteio = random.shuffle(lista)
print(sorteio)

"""
Desafio 021 - Faça um programa de Python que abra e reproduza um arquivo de 
MP3.
"""







