# -*- coding: utf-8 -*-
"""
Created on Wed Apr  1 16:01:37 2020

@author: jfpas
"""

"""
Estrutura de controles - LAÇO
laço de repetição
iteração

Laço com variável de controle
Estrutura de laço que ocorre até o encontro da variável de controle

Indetação
Espaço para indicar que um comando esta aninhado em outro

--------------------------EXEMPLOS-----------------------
for é uma estrutura de repetição com variável de controle


for c in range(1,10):
    passo
pega

for c in range(0,3):
    passo
    pula
passo
pega

for c in range(0,23):
    if moeda:
        pega
    passo 
    pula
passo
pega

----------------------------------------------------------
"""

for c in range(1,6):
    print('Oi')
print('FIM')

for c in range(1,6):
    print(c)
    print('FIM')


for c in range(1,6):
    print(c)
print('FIM')

for c in range(1,7):
    print(c)
print('FIM')

#maneira errada de traz pra frente

for c in range(6,0 ):
    print(c)
print('FIM')

# A última virgula diz respeito a como será realizada a iteração

for c in range(6, 0, -1):
    print(c)
print('FIM')

for c in range(0, 7, 2):
    print(c)
print('FIM')

n = int(input('Digite um número: '))
for c in range(0, n+1):
    print(c)
print('Fim')

i = int(input('Início: '))
f = int(input('Fim: '))
p = int(input('Passo: '))

for c in range(i, f+1, p):
    print(c)

for c in range(0,3):
    n = int(input('Digite um valor: '))
print('FIM')

#Fazendo uma somadora:

s = 0
for c in range(0,4):
    n = int(input('Digite um valor: '))
    s += n
print('O somatório dos valores foi {}'.format(s))

"""
Desafio - 046 Faça um progrma que mostre na tela uma contagem regressiva para o
estouro de fogos de artificio, indo de 10 até 0, com uma pausa de 1 segundo 
entre eles.
"""

from time import sleep

for c in range(10, -1, -1):
    print(c)
    sleep(1)
print('KABUM!!!')

"""
Desafio 047 - Crie um progama que mostre na tela todos os números pares que 
estão no intervalo entre 1 e 50
"""

for c in range(2, 51, 2):
    print(c)

"""
Desafio 048 - Faça um progama que calcule a soma entre todos os números ímpares
que são múltiplos de três que se encontram no intervalo de 1 até 500.
"""
s = 0
for c in range(3, 500, 3):
    s +=c
print (s)

"""
Desafio 049 - Refaça o desafio 009, mostrando a tabuada de um número que o
usuário escolher, só que agora utilizando um laço for.
"""

t = int(input('Qual o número que você deseja saber a tabuada? '))

print('A tabuada de {} é:'.format(t))

for c in range(1,11):
    print('{} x {} = '.format(t,c),t*c)
print('Aí está a tabuada de {}'.format(t))

"""
Desafio 050 - Desenvolva um programa que leia seis números inteiros e mostre a
soma apenas daqueles que forem par. Se for ímpar, desconsidere-o.
"""

s = 0

for c in range(0,3):
    n = int(input('Digite um valor: '))
    if n % 2 == 0:
        s += n
print(s)

"""
Desafio 051 - Desenvolva um programa que leia o primeiro termo e a razão de uma
PA.No final mostre os 10 primeiros termos dessa progressão
"""

a1 = int(input('Qual o primeiro termo da progressão aritmética? '))
r = int(input('Qual a razão da Progressão Aritmética? '))


for c in range(1,11):
    PA = a1*(r**c)
    print('A{} = {}'.format(c,PA))
print('Estes são os dez primeiros termos')

"""
Desafio 052 - Faça um programa que leia um número inteiro e diga se ele é ou 
não é um número primo.
"""

n = int(input('Digite um número inteiro: '))
t = 0

for c in range(1, n +1):
    if n % c == 0:
        t = t + 1
if t == 2:
    print('Este número é divisivel apenas por 1 e ele mesmo, portanto, ele é' 
          ' primo')
elif n == 1 or n == 2:
    print('O número 1 é primo')
else:
    print('Este número é divisível por {} números além de 1 e ele mesmo,' 
          'portanto, ele não é primo'.format(t-2))

"""
DESAFIO 053 - Crie um progama que leia uma frase qualquer e diga se ela é um 
palindromo, desconsiderando os espaços.
EX:APOS A SOPA
A SACADA DA CASA
A TORRE DA DERROTA
O LOBO AMA BOLO
ANOTARAM A DATA DA MARATONA
"""
pal = str(input('DIGITE UMA PALAVRA AÍ: '))
pal_junto = pal.replace(' ', '')
inverso =''

for c in range(len(pal_junto) - 1, -1, -1):
    inverso += pal_junto[c]
print('O inverso de {} é {}'.format(inverso, pal_junto))
if inverso == pal_junto:
    print('A palavra é um palindromo')
else:
    print('a frase digitada não é um palindromo')


"""
DESAFIO 054 - Crie um programa que leia o ano de nascimento de sete pessoas. No
final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são 
maiores
"""
from datetime import date

ano_atual = date.today().year

t = 0
m = 0

for c in range(0,7):
    anos = int(input('Qual o ani de nascimento da pessoa? '))
    idade = ano_atual - anos
    if idade >= 21:
            t += 1
    elif idade < 21:
            m +=1
print('Das sete pessoas digitadas {} são maiores de idade e {} são menores de'
      'idade'.format(t,m))

""" 
Desafio 055 - Faça um programa que leia o peso de cinco pessoas. No final,
mostre qual foi o maior e o menor peso lidos.
"""
maior = 0
menor = 0

for c in range (0,5):
    p = float(input('Qual o peso da {}ª pessoa? Kg '.format(p)))
    if p > maior:
        maior = p
    if p < menor or menor ==0:
        menor = p
print('O maior peso foi de {}kg e o menor peso foi de {}kg'
      .format(maior,menor))

"""
Desafio 056 - Desenvolva um programa que leia nome, idade e sexo de 4 pessoas. 
No final do programa mostre:
    - A média de idade do grupo
    - Gual o nome do homem mais velho
    - Quantas mulheres tem menos de 20 anos
"""

maior_h = 0
cont_m =0
s_i = 0

for c in range (1,5):
    n = str(input('Qual o nome da {}ª pessoa? '.format(c)))
    i = int(input('Digite a idade da {}ª pessoa: '.format(c)))
    s_i += i
    sex = int(input('Digite 1 se a pessoa for mulher e 2 para se for homem:' ))
    if sex == 2 and i > maior_h:
        maior_h = i
        mais_velho = n
    elif sex == 1 and i> 20:
        cont_m += 1
m_i = s_i/4
print('O grupo possui média de idade de {} anos. O homem mais velho é {} com'
      '{} anos e {} mulheres são maiores de 20 anos.'
      .format(m_i,mais_velho,maior_h,cont_m))







