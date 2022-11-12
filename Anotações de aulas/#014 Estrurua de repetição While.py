# -*- coding: utf-8 -*-
"""
Created on Sun Apr  5 18:41:02 2020

@author: jfpas
"""
"""
WHILE
Estrutura de repetição com teste lógico

while not mação:
    if chão:
        passo
    if buraco:
        pula
    if moeda:
        pega
pega

------------------Comparando FOR e WHILE ----------------------

* Se eu sei o limite eu posso utilizar FOR e WHILE
** Se eu não sei o limite posso utilizar apenas WHILE


"""

#COMPARANDO FOR E WHILE nos casos em que sei o limite

for c in range(1,10):
    print(c)
print('FIM')

c = 1
while c < 10:
    print(c)
    c = c +1
print('FIM')

#EXEMPLO DE WHILE quando não sei o limite

n = 1
while n != 0:
    n = int(input('Digite um valor'))
print('Fim')

r = 'S'
while r == 'S':
    n = int(input('Digite um valor: '))
    r = str(input('Quer continuar? [S\N]')).upper()
print('FIM')

n = 1
par = impar = 0
while n != 0:
    n = int(input('Digite um valor: '))
    if n!= 0:
        if n % 2 == 0:
            par += 1
        else:
            impar += 1
print('Você digitou {} números pares e {} números ímpares.'.format(par, impar))

"""
Desafio 057 - Faça um progama que leia o sexo de uma pessoa mas só aceite M ou 
F, Caso esteja errado pela a digitação npvamente até ter um valor correto
"""

r = 'S'

while r == 'S':
    s = str(input('Qual o sexo da pessoa [M/F]? ')).upper()
    if s == 'F' or s == 'M':
        r = str(input('Você deseja continuar digitando? ')).upper()
    else:
        print('Essa opção de sexo não existe!!!!!!!!!!!' 
              'DIGITE OUTRA')
print('ACABOU')

"""
Desafio 058 - Melhore o jogo do DESAFIO 028 onde o cumputador vai "pensar' em 
um número entre 0 e 10. Só que agora o jogador vai tentar advinhar até acertar, 
mostrando no final quantos palpites foram necessários para vencer

RELEMBRANDO

Desafio 028 - Escreva um programa que faça o computador "pensar" em um número
inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número 
escolhido pelo computador.

O programa deverá escrever na tela se o usuário venceu ou perdeu.
"""

from random import randint
from time import sleep

n_pc = randint(1,10)
n_usu = int(input('Tente acertar o número que pensei entre 0 e 10: '))

print('PROCESSANDO...')

sleep(2)
t = 1
while n_usu != n_pc:
    print('Você ERROU!!! Tente novamente!')
    n_usu = int(input('Digite outro número: '))
    t += 1
    
if t == 1:
    print('VOCÊ ACERTOU DE PRIMEIRA!!!!! \nBRABO!')
elif 1 < t < 5:
    print('Você acertou e precisou de {} tentativas!'.format(t))
else:
    print('Ave-Maria, finalmente.....\nForam necessárias {} tentativas'
          .format(t))
"""
Desafio 059 - Crie um progama qque leia dois valores e mostre um menu na tela:
    [1] Somar
    [2] Multiplicar
    [3] Maior
    [4] Novos Números
    [5] Sair do progama
Seu progama deverá realizar a operação solicitada em cada caso
"""

print('''BEM VINDO À SUA CALCULADORA!!!\n
AQUI VOCÊ PODE SOMAR OU MULTIPLICAR''')
n = 0
r = 0

v1 = int(input('Digite o primeiro valor: '))
v2 = int(input('Digite o segundo valor: '))

while n != 5:
    print('''ESSAS SÃO SUAS OPÇÕES:\n
          [1] para Somar;\n
          [2] para Multiplicar;\n
          [3] para saber o maior valor;\n
          [4] para Digitar novos números;\n
          [5] para sair do progama.''')
    n = int(input('DIGITE A OPÇÃO DESEJADA:'))
    if n == 1:
        r = v1 + v2
        print('O resultado da sua operação foi {}'.format(r))
    elif n == 2:
        r = v1 * v2
        print('O resultado da sua operação foi {}'.format(r))
    elif n == 3:
        if v1 > v2:
            r = v1
            print('{} é o maior número'.format(r))
        elif v2 > v1:
            r = v2
            print('{} é o maior número'.format(r))
        else:
            print('Os dois números são iguais')
    elif n == 4:
        print('Digite os novos valores')
        v1 = int(input('Digite o primeiro valor'))
        v2 = int(input('Digite o segundo valor'))
print('Até Mais')
"""
DESAFIO 060 - Faça um progama que leia um número qualquer e mostre o seu 
fatorial.
Ex:
    5! = 5x4x3x2x1 = 120
"""

print('VAMOS CALCULAR FATORIAL')

n = int(input('Digite o número que você deseja saber o fatorial: '))
c = 0
f = 1
while c != n:
    print(c)
    c += 1
    f = f*c
print('O fatorial {}! é igual a {}'.format(n,f))

"""
Desafio 061 - Refaça o Desafio 051, lendo o primeiro termo e a razão de uma PA,
mostrando os 10 primeiros termos da progressão usando a estrutura while.
"""

print('Calcularemos a P.A. do número que você deseha')

a1 = int(input('Digite o número que você deseja: '))

c = 0
while c != 10:
    c += 1
    pa = a1*c
    print('a{} = {}'.format(c,pa))

"""
Desafio 062 - Melhore o Desafio 061, perguntando para o usuário se ele quer 
mostrar mais alguns termos. O progama encerra quando ele disser que quer 
mostrar 0 termos
"""
    
a1 = int(input('Digite o número que você deseja: '))

c = 0
while c != 10:
    c += 1
    pa = a1*c
    print('a{} = {}'.format(c,pa))

mais = int(input('Você quer ver mais termos da P.A.? Se sim indique quantos,'
                 'se não, digite 0: '))
mais = mais + 10

while c != mais:
    c += 1
    pa = a1*c
    print('a{} = {}'.format(c,pa))

"""
Desafio 063 - Escreva um progama que leia um número n inteiro qualquer e mostre
na tela os n primeiros elementos de uma sequência de Fibonacci.

Exemplo> 0 -> 1 -> 2 -> 3 -> 4 -> 5 -> 8
"""
c=0
q = int(input('Quantos termos da sequência você necessita saber? '))
a0 = 1
a1 = 1
while c != q + 1:
    if c == 0:
        f = 0
    elif c == 1:
        f = 1
    else:
        f = a0 + a1
        a0 = a1
        a1 = f
    c += 1
    print(f)
    
    
"""
Desafio 064 - Crie um proga,a que leia vários números inteiros pelo teclado. 
O progama só vai parar quando o usuário digitar o valor 999, que é a condição 
de parada. No final, mostre quantos números foram digitados e qual foi a soma 
entre eles (desconsiderando o flag)
"""

n = 0
s = 0
c = 0
n = int(input('Digite um número [999 para parar]: '))
while n != 999:
    c += 1
    s = s + n
    n = int(input('Digite um número [999 para parar]: '))
print('Você digitou {} números e a soma entre eles é {}.'.format(c,s))


"""
Desafio 065 - Crie um progama que leia vários números inteiros pelo teclado. No
final da execução, mostre a média entre todos os valores qual foi o maior e o
menor valores lidos. O progama deve perguntar ao usuário se ele quer ou não 
continuar a digitar valores.
"""    

resp = "Sim"
c = 0
maior = menor = média = 0
s = 0
while resp != 'n':
    n = int(input('Digite o número: '))
    if n > maior:
        maior = n
    if n < menor or menor == 0:
        menor = n
    s += n
    c += 1
    média = s/c
    resp = str(input('Você deseja continuar digitando [S/N]? ')).lower()[0]
print('A sua média foi de {:2}. O maior número é {}, e o menor {}. Foram'
      'digitados {} números'.format(média, maior, menor, c))
















