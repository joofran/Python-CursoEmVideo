# -*- coding: utf-8 -*-
"""
Created on Sat Apr 11 18:39:51 2020

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
    if troféu
        pula
        break
pega

# =============================================================================
# COMANDO BREAK
    -> Interrompe a estrutura While
# =============================================================================
"""
#Jeito com gambiarra
n = s = 0 
while n!= 999:
    n = int(input('Digite um número: '))
    s += n
s -= 999
print('A soma vale {}'.format(s))


#Jeito sem gambiarra com break
n = s = 0 
while True:
    n = int(input('Digite um número: '))
    if n == 999:
        break
    s += n
print(f'A soma vale {s}')


"""
# =============================================================================
# APRENDENDO fstring
# =============================================================================

"""

nome = 'José'
idade = 33
salário = 987.3
print(f'O {nome} tem {idade} anos e ganha R${salário:.2f} ')
print(f'O {nome:^20} tem {idade} anos e ganha R${salário:.2f} ')
print(f'O {nome:>20} tem {idade} anos e ganha R${salário:.2f} ')


"""
Desafio 066 - Crie um progama que leia vários números inteiros pelo teclado. O
progama só vai parar quando o usuário digitar o valor 999, que é a condição de 
parada. No final mostre quantos números foram digitados e qual foi a soma entre
eles (desconsiderando o flag)
"""

n = c = s = 0
while True:
    n = int(input('Digite um número [999 para parar]: '))
    if n == 999:
        break
    c += 1
    s = s + n
print('Você digitou {} números e a soma entre eles é {}.'.format(c,s))

"""
Desafio 067 - Faça um progama que mostre a tabuada de vários números, um de 
cada vez, para cada valor digitado pelo usuário. O progama será interrompido 
quando o número solicitado for negativo.
"""

while True:
    n = int(input('Qual número você deseja saber a tabuada? \n[Digite um número'
' negativo para sair]: '))
    if n < 0:
        break
    for c in range(1,11):
        m = n*c
        print(f'{n} x {c} = {m}')
print('Obrigado')

"""
Desafio 068 - Faça um progama que jogue par ou ímpar com o computador. O jogo 
será interrompido quando o jogador PERDER, mostrando o total de vitórias 
consecutivas que ele conquistou
"""
from random import randint
c = 0
while True:
    usup = str(input('Você escolhe par ou ímpar? ')).lower().strip()
    if usup == 'par' or usup == 'ímpar':
        pc = randint(0,10)
        usu = int(input('Escolha um número entre 0 e 10: '))
        if usu > 10 or usu < 0:
            print('Digite um valor válido')
        else:
            r = usu + pc
            print(f'eu escolhi {pc} e vc escolheu {usu}, a soma é {r}')
            if r % 2 == 0:
                r = 'par'
            elif r % 2 != 0:
                r = 'ímpar'
            if r == usup:
                print('Você ganhou')
                c += 1
            elif r != usup:
                print('Você perdeu')
                break
    else:
        print('Digite par ou ímpar.[ímpar tem acento]: ')
print(f'Você ganhou {c} vezes')

"""
Desafio 069 - Crie um progama que leia a idade e o sexo de várias pessoas. A 
cada pessoa o progama deverá perguntar se o usuário quer continuar. No final 
mostre:
    a) quantas pessoas tem mais de 18 anos;
    b) quantos homens foram cadastrados;
    c) quantas mulheres tem mais de 20 anos.
"""

adulto = sex_macho = adulto_femea = 0

while True:
    age = int(input('Idade: '))
    if age > 18:
        adulto += 1
    sex = str(input('Sexo [M/F]: ')).upper().strip()[0]
    while sex not in 'MF':
        sex = str(input('Sexo [M/F]: ')).upper().strip()[0]
    if sex == 'M':
        sex_macho += 1
    if sex =='F' and age > 20:
        adulto_femea += 1
    cont = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    while cont not in 'SN':
        cont = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if cont == 'N':
        break
print(f'{adulto} tem mais de 18; \n{sex_macho} são homens; \n{adulto_femea}'
' são mulheres maiores de 20 anos')

"""
Desafio 070 - Crie um progama que leia o nome e o preço de vários produtos. O 
progama deverá perguntar se o usuário vai continuar. No final mostre:
    a) qual é o total de gasto na compra;
    b) quantos produtos curstam mais de R$ 1000;
    c) qual é o produto mais barato.
"""

print('LOJOFA')
s = m = c = 0
while True:
    prod = str(input('Nome do produto: '))
    preço = float(input('Preço do produto: R$'))
    s += preço
    if preço > 1000:
        c += 1
    if m == 0 or preço < m:
        m = preço
        b = prod
    cont = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    while cont not in 'SN':
        cont = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if cont == 'N':
        break
print(f'''Você gastou R$ {s}; \nCustaram mais de mil reais {c} produtos \n
O produto mais barato foi {prod} e ele custou R$ {m}''')

"""
Desafio 071 - Crie um progama que simule o funcionamento de um caixa 
eletrônico. No início, pergunte ao usuário qual será o valor a ser sacado 
(número inteiro) e o progama vai informar quantas cédulas de cada valor serão 
entregues.

Obs.: Considere que o caixa possui cédulas de R$ 50; R$ 20; R$ 10 e R$ 1
"""
print('JOFABANK')
valor = int(input('Qual valor você deseja sacar? R$ '))

cinq = valor // 50
resto = valor % 50
if cinq != 0:
    print(f'Total de {cinq} cédulas de R$ 50')
vint = resto // 20
if vint != 0:
    print(f'Total de {vint} cédulas de R$ 20')
resto = resto % 20
dez = resto // 10
if dez != 0:
    print(f'Total de {dez} cédulas de R$ 10')
resto = resto % 10
um = resto // 1
if um != 0:
    print(f'Total de {um} cédulas de R$ 1')











