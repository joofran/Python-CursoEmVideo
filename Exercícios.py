# -*- coding: utf-8 -*-
"""
Created on Wed Feb 19 15:49:47 2020

@author: jfpas
"""

#Ex 001

Msg = 'Olá, Mundo'

print(Msg)

#Ex 002

nome=input("Digite o seu nome: ")

print("É um prazer te conhecer,",nome)

#EX 003

n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o segundo valor: '))

s = n1 + n2

print('A soma entre {} e {} vale {}'.format(n1,n2,s))
"OUTRA FORMA: print('A soma entre', n1, 'e', n2, 'vale',s)"

#EX 004

algo = input('Digite algo: ')
print('Só tem espaço?', algo.isspace())
print('É um número?', algo.isalnum())
print('É alfabético?', algo.isalpha())
print('É alfanúmerico?', algo.isalnum())
print('Está em maiúsculo?', algo.isupper())
print('Está em minúsculo?', algo.islower())
print('Está capitalizada?',algo.istitle())

print('A palavra {} é um número?'.format(algo), algo.isnumeric())

#Ex 005

nn1 = int(input('Qual o número? '))
print('O antecessor de {} é {}, e o seu sucessor é {}'.format(nn1,nn1-1,nn1+1))

#Ex 006

print('O dobro de {} é {}, o seu triplo é {} e a sua raiz quadrada é {:.2f}.'
      .format(nn1,nn1*2,nn1*3,nn1**(1/2)))
print('A raiz quadrada de {} é {}.'.format(nn1,pow(nn1,(1/2))))


#Ex 007

p1 = float(input('Qual foi a priimeira nota? '))
p2 = float(input('Qual foi a segunda nota? ' ))

print('A sua média foi {}'.format((p1+p2)/2))

#Ex 008

cov=float(input('Qual valor em metros você deseja converter? '))
print('O valor de {} metros equivale a {:.1f} cm, e a {:.0f} mm'
      .format(cov,cov*100,cov*1000))

#EX 009

t = int(input('Qual o número que você deseja saber a tabuada? '))

print('-' * 11)

print('1x{}={}\n2x{}={}\n3x{}={}\n4x{}={}'.format(t,t*1,t,t*2,t,t*3,t,t*4))
print('5x{}={}\n6x{}={}\n7x{}={}\n8x{}={}'.format(t,t*5,t,t*6,t,t*7,t,t*8))
print('9x{}={}\n10x{}={}'.format(t,t*9,t,t*10))

print('{} x {:2} = {}'.format(t,1,t*1))
print('{} x {:2} = {}'.format(t,2,t*2))
print('{} x {:2} = {}'.format(t,3,t*3))
print('{} x {:2} = {}'.format(t,4,t*4))
print('{} x {:2} = {}'.format(t,5,t*5))
print('{} x {:2} = {}'.format(t,6,t*6))
print('{} x {:2} = {}'.format(t,7,t*7))
print('{} x {:2} = {}'.format(t,8,t*8))
print('{} x {:2} = {}'.format(t,9,t*9))
print('{} x {:2} = {}'.format(t,10,t*10))

print('-' * 11)

#EX 010

real = float(input('Quantos reais você possui na carteira? R$ '))
dol = real/3.27

print('Com R$ {} você pode comprar US$ {:.2f}'.format(real,dol))

#EX 011

h = float(input('Qual a altura da parede? ' ))
l = float(input('Qual a largura da parede? ' ))

A = h*l
lt = A/2

print('A área da parede é {}m², portanto, serão necessários {}l'.format(A,lt), 
      'litros de tinta para pintá-la')

#EX 012

pç = float(input('Qual o preço do produto? R$ '))

print('O preço do produto com 5% de desconto é: R$ {:.2f}'.format(pç*0.95))

#EX 013

sal = float(input('Qual é o salário do funcionário? R$ '))
print('O salário do funcionário com 15% de aumento é R$ {:.2f}'.format(sal*1.15))

#EX 014 - conversor de temperatura

celsius = float(input('Qual a Temperatura em graus celsius? '))
fahren = celsius * 9/5 + 32

print('{}ºC é igual a {}ºF'.format(celsius,fahren))

#EX 015 
"""
Escreva um programa que pergunte a quantidade de Km percorridos por um carro 
alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a 
pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.
"""
Km_rod = int(input(
    'Quantos quilômetros foram rodados com o carro durante o aluguel? ' ))
D_alug = float(input('Por quantos dias o carro foi alugado? '))
aluguel = D_alug*60 + Km_rod*0.15

print('O valor da aluguel para {} dias e {} Km rodados é igual a {}'.format(D_alug,Km_rod,aluguel))


"""
---------------------------AULA 08---------------------------------------------
"""

#EX 016
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


#EX 017
"""
Desafio 17 - Faça um programa que leia o comprimento do cateto oposto e do 
caateto adjacente de um triângulo retângulo, calcule e mostre o comprimento da 
hipotenusa
"""

from math import hypot
cat1 = float(input('Quanto é o primeiro cateto? '))
cat2 = float(input('Quanto é o segundo cateto? '))
hip = hypot(cat1,cat2)

print('A hipotenusa do triângulo com catetos {} e {} é igual a {}'
      .format(cat1,cat2,hip))

#EX 018
"""
Desafio 18 - Faça um programa que leia um ângulo qualquer e mostre na tela o 
valor do sen, cosseno e tangente desse ângulo.
"""
from math import radians, sin, cos, tan

ang = float(input('Qual o ângulo que você deseja saber os valores? '))
rad = radians(ang)
sen = sin(rad)
cos = cos(rad)
tg = tan(rad)

print('O ângulo {} em radianos equivale a {:.2f}.'
      'Ele tem como seno, {:.2f}, como cosseno, {:.2f}.'
        'e como tangente ele possui{:.2f}'.format(ang,rad,sen,cos,tg))

#EX 019
"""
Desafio 019 - Um professor quer sortear um dos seus quatro alunos para apagar o
 quadro. Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome escolhido.
"""

from random import choice, shuffle

um = input('Qual o nome do primeiro aluno? ')
dois = input('Qual o nome do segundo aluno? ')
três = input('Qual o nome do terceiro aluno? ')
quatro = input('Qual o nome do quarto aluno? ')

lista = [um, dois, três, quatro]
escolha = choice(lista)

print('O aluno escolhido foi: {}'.format(escolha))

#EX 020

"""
Desafio 020 - O mesmo professor do desafio anterior quer sortear a ordem de 
apresentação de trabalhos dos alunos. Faça um programa que leia o nome dos 
quatro alunos e mostre a ordem sorteada.
"""

shuffle(lista)
print('A ordem de apresentação é: ')
print(lista)

# Tentei muito criar uma variável para representar o shuffle 
# (na forma sorteio = shuffle(lista)) e não entendi por que isso não pode ser 
# feito até agora, simplesmente sei que não pode ser feito


#EX 021

"""
Desafio 021 - Faça um programa de Python que abra e reproduza um arquivo de 
MP3.
"""

#REVER ESSE CÓDIGO
import wave

ope = input('Insira o endereço de onde se esncontra o arquivo no computador: ')
wave.open(ope)

import pygame
pygame.inite
pygame.mixer.music.load('Ala.WAV')
# REVER ESSE CÓDIGO

"""
---------------------------AULA 09---------------------------------------------
"""
#EX 022
"""
Desafio 022 - Crie um programa que leia o nome completo de uma pessoa e mostre:
    - O nome com todas as letras maiúsculas
    - O nome com todas as letras minusculas
    - Quantas letras ao todo (sem considerar espaços)
    - Quantas letras tem o primeiro nome
"""

nome = str(input('Qual o seu nome completo? '))

##NOME MAIÚSCULO
print('Seu nome em maiúsculo é: {}'.format(nome.upper()))

##NOME MINÚSCULO
print('Seu nome em minúsculo é: {}'.format(nome.lower()))

##QUANTIDADE DE LETRAS
nome_junto = nome.replace(' ','')
print('Seu nome possui {} letras ao todo'.format(len(nome_junto)))

###OUTRA RESOLUÇÃO DO ACIMA
nome_espaços_removido = nome.strip()
print('Seu nome possui {} letras ao todo'
      .format(len(nome_espaços_removido)-nome_espaços_removido.count(' ')))

##QUANTIDADE DE LETRAS PRIMEIRO NOME
nome_separado = nome.split()
print('Seu primeiro nome é {} e possui {} letras'.format(nome_separado[0],
      len(nome_separado[0])))

###OUTRA RESOLUÇÃO DO ACIMA
nome_espaços_removido = nome.strip()
print('Seu primeiro nome possui {} letras'
      .format(nome_espaços_removido.find(' ')))


#EX 023
"""
Desafio 023 - Faça um programa que leia um número de 0 a 9999 e mostre na tela 
cada um dos dígitos separados.
Ex.: 
    Digite um número: 1834
        unidade:1
        dezena:8
        centena:3
        milhar:4
"""

num = str(input('Digite o número: '))

print('O número tem como:')
print('Unidade: {};'.format(num[-1]))
print('Dezena: {};'.format(num[-2]))
print('Centena: {};'.format(num[-3]))
print('Milhar: {}.'.format(num[-4]))
#Resolução acime é feita com string porém precisamos de if else para resolver 
#os casos de números com 3 dígitos ou menos

num = int(input('Digite o número: '))

print('O número {} tem como:'.format(num))

print('Milhar: {};'.format(num // 1000))
print('Centena: {};'.format(num // 100 % 10))
print('Dezena: {};'.format(num // 10 % 10))
print('Unidade: {}.'.format(num % 10))

#EX 024
"""
Desafio 024 - Crie um programa que leia o nome de uma cidade e diga se ela 
começa ou não com o nome "SANTO"
"""
cid = str(input('Qual o nome da cidade que você deseja saber? '))

cid_separado = cid.split()

print('A cidade começa com SANTO?\n','SANTO' in cid_separado[0].upper())

##Solução do Guanabara
cid = str(input('Qual o nome da cidade que você deseja saber? '))
print(cid[:5].upper() == 'SANTO')

#EX 025

"""
Desafio 025 - Crie um programa que leia o nome de uma pessoa e diga se ela tem 
"SILVA" no nome
"""

n_pessoa = str(input('Qual o nome da pessoa? ')).strip()

print('Existe SILVA no nome?\n', 'SILVA' in n_pessoa.upper())

#EX 026
"""
Desafio 026 - Faça um programa que leia uma frase pelo teclado e mostre:
    - Quantas vezes aparece a letra "A"
    - Em que posição ela aparece a primeira vez
    - Em que posição ela aparece a última vez
"""
palavra = str(input('Digite a palavra desejada: ')).strip()

print('Quantas vezes aparece a letra "a" na palavra {}: {}'
    .format(palavra,palavra.lower().count('a')))
print('A primeira letra "a" aparece na posição: {}'
      .format(palavra.lower().find('a') + 1))
print('A última letra "a" aparece na posição: {}'
      .format(palavra.lower().find('a',-1) + 1))

#EX 027

"""
Desafio 027 - Faça um programa que leia o nome completo de uma pessoa, 
mostrando em seguida o primeiro e o último nome separadamente
Ex.: Ana Maria de Souza
primeiro = Ana
último = Souza
"""
nome = str(input('Digite o nome desejado: '))
nome_separado = nome.split()

print('O primeiro nome é {} e o último é {}'.format(nome_separado[0],
      nome_separado[-1]))

##SOLUÇÂO GUANABARA 
print('Seu último nome é {}'.format(nome_separado[len(nome_separado)-1]))

#EX 028

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

#EX029

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


#EX 030

"""
Desafio 030 - Crie um programa que leia um número interio e mostre na tela se 
ele é PAR ou ÍMPAR.
"""
n = int(input('Digite um número: '))

if n % 2 == 0:
    print('O número {} é Par'.format(n))
else:
    print('O número {} é Ímpar'.format(n))


#EX 031

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

#EX 032

"""
Desafio 032 - Faça um programa que leia um ano qualquer e mostre se ele é 
BISSEXTO.
"""
ano = int(input('Digite um ano: '))

if ano % 4 == 0 and ano % 400 == 0 or ano % 100 != 0: 
    print('O ano é bissexto!!')
else:
    print('O ano não é bissexto.')


# EX 033

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


#EX 034

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
  
#EX 035    
    
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

#EX 036
    
"""
Desafio 036 - Escreva um progama para aprovar o empréstimo bancário para a 
compra de uma casa. O programa vai perguntar o valor da casa, o salário do 
comprador e em quantos anos ele vai pagar.

Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do
salário ou então o empréstimo será negado.
"""

valor_casa = float(input('Quanto custa a casa que você deseja comprar? R$ '))
salário_comp = float(input('Quanto você ganha por mês? R$ '))
anos_pg = int(input('Em quantos anos você pretende pagar a casa? '))
prestação = valor_casa/(anos_pg*12)
prestação_minima = 0.3*salário_comp

print('O valor da prestação é {:.2f}'.format(prestação))

if prestação <= prestação_minima:
    print('Parabéns!!! Você poderá realizar dado que a prestação de R$ {:.2f} '
          'é inferior a 30% de seu salário'.format(prestação))
else:
    print('Infelizmente você não pode realizar o empréstimo com as condições'
          'informadas')

#EX 037
    

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
    print('Você escolheu a base de conversão Binária \nO número fica {}: {}'
          .format(N,bin(N)[2:]))
elif op == 2:
      print('Você escolheu a base de conversão Octal \nO número fica{}: {}'
            .format(N,oct(N)[2:]))
elif op == 3:
      print('Você escolheu a base de conversão Hexadecimal \nO número '
            'fica {}: {}'.format(N,hex(N)[2:]))
else:
    print('A opção escolhida não corresponde a nenhuma das bases de conversão '
          'disponíveis')

#EX 038
    
"""
Desafio 038 - Escreva um programa que leia dois números inteiros e compare-os, 
mostrando na tela uma mensagem:
    - o primeiro valor é maior
    - o segundo valor é maior 
    - Não existe valor maior, os dois são iguais
"""
n1 = int(input('Insira o primeiro valor: '))
n2 = int(input('Insira o segundo valor: '))

if n1 > n2:
    print('O primeiro valor {} é o maior'.format(n1))
elif n2 > n1:
    print('O segundo valor {} é o maior'.format(n2))
else:
    print('Não existe valor maior, ambos são iguais')

#EX 039

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
id_ano = ano - ano_nasc

if id_ano == 18:
    print('Você faz 18 anos esse ano, portanto, deve se alistar.')
elif id_ano < 18:
    print('Você terá {} anos neste ano, portanto ainda não deve se alistar.'
          .format(id_ano))
else:
    print('Você terá {} até o final desse ano, portanto, já passou do seu '
          'período de alistamento. Procure a junta militar mais próximo caso '
          'ainda não tenha se alistado.'.format(id_ano))
    
#EX 040

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
elif 5.0 <= média < 7.0:
    print('Você está em recuperação')
else:
    print('Parabéns! Você foi aprovado!')

#EX 041
    
"""
Desafio 041 - A Confederação Nacional de Natação precisa de um programa que 
leia o ano de nascimento de um atleta e mostre a sua categora, de acordo com a 
idade:
    - Até 9 anos: MIRIM
    - Até 14 anos: INFANTIL
    - Até 25 anos: SÊNIOR
    - Acima: MASTER
"""
from datetime import date

hoje = date.today().year
nasc = int(input('Em que ano o atleta nasceu? '))
anos = hoje - nasc

if anos <= 9:
    print('O atleta possui {} anos e está na categoria MIRIM'.format(anos))
elif 9 < anos <= 14:
    print('O atleta possui {} anos e está na categoria INFANTIL'.format(anos))
elif 14 < anos <= 19:
    print('O atleta possui {} anos e está na categoria JUNIOR'.format(anos))
elif 19 < anos <= 25:
    print('O atleta possui {} anos e está na categoria SÊNIOR'.format(anos))
else:
    print('O atleta possui {} anos e está na categoria MASTER'.format(anos))

#EX 042
    
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
elif cond1 and cond2 and cond3 is True and  a != b != c != a:
    print('Os valores que você inseriu retornam um triângulo e ele é Escaleno')
else:
    print('Os valores que você inseriu não formam um triângulo')

#RESOLUÇÃO GUANABARA

import math
a = float(input('Insira o primeiro lado do triângulo: '))
b = float(input('Insira o segundo lado do triângulo: '))
c = float(input('Insira o terceiro lado do triângulo: '))

cond1 = math.fabs(b - c) < a < b + c
cond2 = math.fabs(a - c) < b < a + c
cond3 = math.fabs(a - b) < c < a + b

if cond1 and cond2 and cond3 is True:
    print('Os valores que você inseriu retornam um triângulo e ele é', end='')
    if a == b == c:
        print('Equilatéro')
    elif a != b != c != a:
        print('Escaleno')
    else:
        print('Isósceles')
else:
    print('Os valores que você inseriu não formam um triângulo')
    
#EX 043
    
"""
Desafio 043 - Desenvolva uma lógica que leia o peso e a altura de uma pessoa, 
calcule seu IMC e mostre seu status de acordo com a tabela abaixo:
    - Abaixo de 18.5: Abaixo do peso
    - Entre 18.5 e 25: Peso ideal
    - 25 até 30: Sobrepeso 
    - 30 a 40: Obesidade 
    - Acima de 40: Obesidade mórbida
"""

h = float(input('Digite a sua altura em metros: '))
p = float(input('Digite o seu peso em quilogramas: '))

IMC = (p)/(h*h)

print(' Você possui IMC de {:.2f}'.format(IMC))

if IMC < 18.5:
    status = 'abaixo do peso'
elif 18.5 <= IMC < 25:
    status = 'com peso ideal'
elif 25 <= IMC < 30:
    status = 'com sobrepeso'
elif 30 <= IMC < 40:
    status = 'com obesidade'
elif IMC >= 40:
    status = 'com obesidade mórbida'

print('Seu IMC indica que você está {}'.format(status))

#EX 044

"""
Desafio 044 - Elabore um progama que calcule o valor a ser pago por um produto,
considerando o seu preço normal e acondição de pagamento:
    - à vista dinheiro/cheque: 10% de desconto
    - à vista no cartão: 5% de desconto
    - em até 2 vezes no cartão: preço normal
    - 3x ou mais no cartão: 20% de juros
"""

valor = float(input('Qual o valor original do produto? R$ '))
print('{:~^40}'.format('LOJA JOFA'))
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


#EX045

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
    print('Você nem consegue escolher uma opção direito... \nEU GANHEI')

#EX 046 -----------------------------------------------------------------------

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

#EX047 -----------------------------------------------------------------------

"""
Desafio 047 - Crie um progama que mostre na tela todos os números pares que 
estão no intervalo entre 1 e 50
"""

for c in range(2, 51, 2):
    print('{}'.format(c), end =' ')

#EX 048 -----------------------------------------------------------------------

"""
Desafio 048 - Faça um progama que calcule a soma entre todos os números ímpares
que são múltiplos de três que se encontram no intervalo de 1 até 500.
"""
s = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        s += c
print ('A soma de todos os números ímpares múltiplos de 3 entre 0 e 500 é {}'
       .format(s))

#EX 049 -----------------------------------------------------------------------

"""
Desafio 049 - Refaça o desafio 009, mostrando a tabuada de um número que o
usuário escolher, só que agora utilizando um laço for.
"""

t = int(input('Qual o número que você deseja saber a tabuada? '))

print('A tabuada de {} é:'.format(t))

for c in range(1,11):
    print('{} x {:2} = '.format(t,c),t*c)
print('Aí está a tabuada de {}'.format(t))

#EX 050 -----------------------------------------------------------------------

"""
Desafio 050 - Desenvolva um programa que leia seis números inteiros e mostre a
soma apenas daqueles que forem par. Se for ímpar, desconsidere-o.
"""

s = 0

for c in range(0,6):
    n = int(input('Digite um valor: '))
    if n % 2 == 0:
        s += n
print(s)

#EX 051 -----------------------------------------------------------------------

"""
Desafio 051 - Desenvolva um programa que leia o primeiro termo e a razão de uma
PA.No final mostre os 10 primeiros termos dessa progressão
"""
#MINHA RESOLUÇÃO

a1 = int(input('Qual o primeiro termo da progressão aritmética? '))
r = int(input('Qual a razão da Progressão Aritmética? '))

for c in range(0,10):
    PA = a1 + r*c
    print('A{:2} = {}'.format(c,PA))
print('Estes são os dez primeiros termos')

#GUANABRA RESOLUÇÃO

a1 = int(input('Qual o primeiro termo da progressão aritmética? '))
r = int(input('Qual a razão da Progressão Aritmética? '))
décimo = a1 + (10-1) * r
for c in range(a1, décimo + r, r):
    print('{}'.format(c), end = ' -> ')
print('Acabou')

#EX 052 -----------------------------------------------------------------------

"""
Desafio 052 - Faça um programa que leia um número inteiro e diga se ele é ou 
não é um número primo.
"""
#MINHA SOLUÇÃO:

n = int(input('Digite um número inteiro: '))
t = 0

for c in range(1, n +1):
    if n % c == 0:
        t = t + 1
if t == 2:
    print('É PRIMO')
else:
    print('NÃO É PRIMO')

#SOLUÇÃO GUANABARA
    
núm = int(input('Digite um número: '))
tot = 0
for c in range(1, núm + 1):
    if núm % c == 0:
        print('\033[32m', end= '')
        tot +=1
    else:
        print('\033[m', end ='')
    print('{} '.format(c), end = '')
print(' O número {} foi divísivel {} vezes'.format(núm, tot))
if tot == 2:
    print('Por isso ele é primo')
else:
    print('Por isso ele não é primo')

#EX 053 -----------------------------------------------------------------------


"""
DESAFIO 053 - Crie um progama que leia uma frase qualquer e diga se ela é um 
palindromo, desconsiderando os espaços.
EX:APOS A SOPA
A SACADA DA CASA
A TORRE DA DERROTA
O LOBO AMA BOLO
ANOTARAM A DATA DA MARATONA
"""
#RESOLVI MAS PRECISEI DE AJUDA

pal = str(input('DIGITE UMA PALAVRA AÍ: ')).upper()
pal_junto = pal.replace(' ', '')
inverso =''

for c in range(len(pal_junto) - 1, -1, -1):
    inverso += pal_junto[c]

print('O inverso de {} é {}'.format(inverso, pal_junto))

if inverso == pal_junto:
    print('A palavra é um palindromo')
else:
    print('A frase digitada não é um palindromo')

#GUANABARA TOTAL

frase = str(input('DIGITE UMA PALAVRA AÍ: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)

inverso = junto[::-1]

print('O inverso de {} é {}'.format(inverso, pal_junto))

if inverso == pal_junto:
    print('A palavra é um palindromo')
else:
    print('A frase digitada não é um palindromo')

#EX 054 -----------------------------------------------------------------------

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
    anos = int(input('Qual o ano de nascimento da pessoa? '))
    idade = ano_atual - anos
    if idade >= 21:
            t += 1
    elif idade < 21:
            m +=1
print('Das sete pessoas digitadas {} são maiores de idade e {} são menores de'
      'idade'.format(t,m))

#EX 055 -----------------------------------------------------------------------

""" 
Desafio 055 - Faça um programa que leia o peso de cinco pessoas. No final,
mostre qual foi o maior e o menor peso lidos.
"""

# FUI CAPAZ DE REALIZAR DEPOIS QUE VI O GUANABARA DEFININDO MAIOR E MENOR = 0
maior = 0
menor = 0

for c in range (0,5):
    p = float(input('Qual o peso da {}ª pessoa? Kg '.format(c)))
    if p > maior:
        maior = p
    if p < menor or menor ==0:
        menor = p
print('O maior peso foi de {}kg e o menor peso foi de {}kg'
      .format(maior,menor))

#SOLUÇÃO GUANABARA

maior = 0
menor = 0

for c in range(1,6):
    p = float(input('Qual o peso da {}ª pessoa? Kg '.format(c)))
    if c == 1:
        maior = p
        menor = p
    else:
        if p > maior:
            maior = p
        if p < menor:
            menor = p
print('O maior peso foi de {}kg e o menor peso foi de {}kg'
      .format(maior,menor))

#EX 056 -----------------------------------------------------------------------

"""
Desafio 056 - Desenvolva um programa que leia nome, idade e sexo de 4 pessoas. 
No final do programa mostre:
    - A média de idade do grupo
    - Gual o nome do homem mais velho
    - Quantas mulheres tem menos de 20 anos
"""

#CONSEGUIR RESOLVER MAS MELHOREI COM DICAS

maior_h = 0
cont_m =0
s_i = 0

for c in range (1,5):
    print('----- {}ª PESSOA -----'.format(c))
    n = str(input('Qual o nome da {}ª pessoa? '.format(c)))
    i = int(input('Digite a idade da {}ª pessoa: '.format(c)))
    s_i += i
    sex = str(input('Qual o sexo [M/F] ? ' )).strip()
    if sex in 'Mm' and i > maior_h:
        maior_h = i
        mais_velho = n
    elif sex in 'Ff' and i< 20:
        cont_m += 1
m_i = s_i/4
print('O grupo possui média de idade de {} anos. O homem mais velho é {} com'
      ' {} anos e {} mulheres são menores de 20 anos.'
      .format(m_i,mais_velho,maior_h,cont_m))

#EX 057 -----------------------------------------------------------------------

"""
Desafio 057 - Faça um progama que leia o sexo de uma pessoa mas só aceite M ou 
F, Caso esteja errado pela a digitação npvamente até ter um valor correto
"""

r = 'S'
s = str(input('Qual o sexo da pessoa [M/F]? ')).upper()

while r == 'S':
    if s == 'F' or s == 'M':
        r = str(input('Você deseja continuar digitando? ')).upper()
    else:
        print('Essa opção de sexo não existe!!!!!!!!!!!\n' 
              'DIGITE OUTRA')
print('ACABOU')

#GUANABARA

sexo = str(input('Informe seu sexo [M/F] ')).strip().upper()[0]
while sexo not in 'MF':
    sexo = str(input('DADOS INCORRETOS. Por favor, informe seu sexo: ')).strip().upper()[0]
print('Sexo {} registrado com sucesso'.format(sexo))

#EX 058 -----------------------------------------------------------------------

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

n_pc = randint(0,10)
n_usu = int(input('Tente acertar o número que pensei entre 0 e 10: '))

print('PROCESSANDO...')

sleep(2)
t = 1
while n_usu != n_pc:
    print('Você ERROU!!!')
    if n_usu > n_pc:
        print('Tente um número menor')
    if n_usu < n_pc:
        print('Tente um número maior')
    n_usu = int(input('Digite outro número: '))
    t += 1
if t == 1:
    print('VOCÊ ACERTOU DE PRIMEIRA!!!!! \nBRABO!')
elif 1 < t < 4:
    print('Você acertou e precisou de {} tentativas!'.format(t))
else:
    print('Ave-Maria, finalmente.....\nForam necessárias {} tentativas'
          ' para descobrir que o número que escolhi foi o {}.'.format(t,n_pc))

# GUANABARA
from random import randint
computador = randint(0,10)
print('Sou seu computador... Acabei de pensar em um número entre 0 e 10.')
print('Será que você consegue acertar qual é esse número?')
acertou = False
palpites = 0
while not acertou:
    jogador = int(input('Qual o seu palipite? '))
    palpites += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais... Tente novamente')
        elif jogador > computador:
            print('Menos... Tente novamente')
print('Acertou com {} tentativas.'.format(palpites))

#EX 059 -----------------------------------------------------------------------

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
    print('''ESSAS SÃO SUAS OPÇÕES:
        [1] para Somar;
        [2] para Multiplicar;
        [3] para saber o maior valor;
        [4] para Digitar novos números;
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
    elif n > 5:
        print('Opção inválida, tente novamente')
print('Até Mais')

#EX 060 -----------------------------------------------------------------------

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

#GUANABARA
n = int(input('Digite um número para calcular o seu fatorial: '))
c = n 
print('Calculando {}! = '.format(n), end = '')
while c > 0:
    print('{}'.format(c),end = '')
    print(' x ' if c > 1 else ' = ', end = '')
    f *- c
    c -= 1
print('{}'.format(f))

#EX 061 -----------------------------------------------------------------------

"""
Desafio 061 - Refaça o Desafio 051, lendo o primeiro termo e a razão de uma PA,
mostrando os 10 primeiros termos da progressão usando a estrutura while.
"""

print('Calcularemos a P.A. do número que você deseha')

a1 = int(input('Digite o número que você deseja: '))
r = int(input('Digite a razão que você deseja: '))

c = 0
while c != 10:
    pa = a1+r*c
    c += 1
    print('a{:<2} = {}'.format(c,pa))

#EX 062 -----------------------------------------------------------------------

"""
Desafio 062 - Melhore o Desafio 061, perguntando para o usuário se ele quer 
mostrar mais alguns termos. O progama encerra quando ele disser que quer 
mostrar 0 termos
"""

a1 = int(input('Digite o número que você deseja: '))
r = int(input('Digite a razão que você deseja: '))

c = 0
x = 10
while c != x:
    pa = a1+r*c
    c += 1
    print('a{} = {}'.format(c,pa))
    if c == x:
        mais = int(input('Você quer ver mais termos da P.A.? Se sim indique quantos,'
                 'se não, digite 0: '))
        x = x + mais
print('Você solicitou {} termos'.format(c))

#EX 063 -----------------------------------------------------------------------

"""
Desafio 063 - Escreva um progama que leia um número n inteiro qualquer e mostre
na tela os n primeiros elementos de uma sequência de Fibonacci.

Exemplo> 0 -> 1 -> 2 -> 3 -> 4 -> 5 -> 8
"""

q = int(input('Quantos termos da sequência você necessita saber? '))
a1 = 0
a2 = 1
f = a1
c=1

while c != q:
    if c == 1:
        print(f)
    print(f)
    a3 = a1 + a2
    a1 = a2
    a2 = a3
    f= a3
    c += 1

#EX 064 -----------------------------------------------------------------------


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

#EX 065 -----------------------------------------------------------------------

"""
Desafio 065 - Crie um progama que leia vários números inteiros pelo teclado. No
final da execução, mostre a média entre todos os valores qual foi o maior e o
menor valores lidos. O progama deve perguntar ao usuário se ele quer ou não 
continuar a digitar valores.
"""    

resp = "Sim"
c = 0
maior = menor = s = 0
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
print('A sua média foi de {:2}. O maior número é {}, e o menor {}. Foram '
      'digitados {} números'.format(média, maior, menor, c))

#EX 066 -----------------------------------------------------------------------

"""
Desafio 066 - Crie um progama que leia vários números inteiros pelo teclado. O
progama só vai parar quando o usuário digitar o valor 999, que é a condição de 
parada. No final mostre quantos números foram digitados e qual foi a soma entre
eles (desconsiderando o flag)
"""

c = s = 0
while True:
    n = int(input('Digite um número [999 para parar]: '))
    if n == 999:
        break
    c += 1
    s = s + n
print('Você digitou {} números e a soma entre eles é {}.'.format(c,s))


#EX 067 -----------------------------------------------------------------------

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

#EX 068 -----------------------------------------------------------------------

"""
Desafio 068 - Faça um progama que jogue par ou ímpar com o computador. O jogo 
será interrompido quando o jogador PERDER, mostrando o total de vitórias 
consecutivas que ele conquistou
"""
from random import randint
c = 0
while True:
    usup = str(input('Você escolhe par ou ímpar? [P/I] ')).lower().strip()[0]
    while usup not in 'pi':
        usup = str(input('Você escolhe par ou ímpar? [P/I] ')).lower().strip()[0]
    usu = int(input('Escolha um número entre 0 e 10: '))
    while 0 < usu > 10:
        usu = int(input('Escolha um número entre 0 e 10: '))
    pc = randint(0,10)
    s = usu + pc
    if s % 2 == 0:
        r = 'p'
        re = 'par'
    elif s % 2 != 0:
        r = 'i'
        re = 'ímpar'
    print(f'Eu escolhi {pc}. Você escolheu {usu}.\nA soma é {s}, um número {re}.')
    if r == usup:
        print('Você ganhou')
        c += 1
    elif r != usup:
        print('Você perdeu')
        break
print(f'Você ganhou {c} vezes')

#EX 069 -----------------------------------------------------------------------

"""
Desafio 069 - Crie um progama que leia a idade e o sexo de várias pessoas. A 
cada pessoa o progama deverá perguntar se o usuário quer continuar. No final 
mostre:
    a) quantas pessoas tem mais de 18 anos;
    b) quantos homens foram cadastrados;
    c) quantas mulheres tem mais de 20 anos.
"""

adulto = sex_masc = adulto_fem = 0

while True:
    age = int(input('Idade: '))
    if age > 18:
        adulto += 1
    sex = str(input('Sexo [M/F]: ')).upper().strip()[0]
    while sex not in 'MF':
        sex = str(input('Sexo [M/F]: ')).upper().strip()[0]
    if sex == 'M':
        sex_masc += 1
    if sex =='F' and age > 20:
        adulto_fem += 1
    cont = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    while cont not in 'SN':
        cont = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if cont == 'N':
        break
print(f'{adulto} tem mais de 18; \n{sex_masc} são homens; \n{adulto_fem}'
' são mulheres maiores de 20 anos')

#EX 070 -----------------------------------------------------------------------

"""
Desafio 070 - Crie um progama que leia o nome e o preço de vários produtos. O 
progama deverá perguntar se o usuário vai continuar. No final mostre:
    a) qual é o total de gasto na compra;
    b) quantos produtos curstam mais de R$ 1000;
    c) qual é o produto mais barato.
"""

print('{:~^40}'.format('LOJOFA'))
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
print(f'''Você gastou R$ {s}; 
Custaram mais de mil reais {c} produtos;
O produto mais barato foi {prod} e ele custou R$ {m}.''')

#EX 071 -----------------------------------------------------------------------

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

#GUANABARA

valor = int(input('Qual valor você deseja sacar? R$ '))
total = valor
céd = 50
tot_céd = 0
while True:
    if total >= céd:
        total -= céd
        tot_céd +=1
    else:
        if tot_céd > 0:
            print(f'Total de {tot_céd} cédulas de R$ {céd}')
        if céd == 50:
            céd = 20
        elif céd == 20:
            céd =10
        elif céd == 10:
            céd = 1
        tot_céd = 0
        if total == 0:
            break

#EX 072 -----------------------------------------------------------------------

"""
Desafio 072 - Crie um progama que tenha uma tupla totalmente preenchida por uma 
contagem por extenso, de zero até vinte.

Seu progama deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por
extenso.
"""

n = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito',
'nove', 'dez', 'onze', 'doze', 'treze','catorze', 'quinze', 'dezesseis',
'dezessete', 'dezoito', 'dezenove', 'vinte')

num = int(input('Digite um valor entre 0 e 20: '))
while num > 20 or num < 0:
    num = int(input('Digite um valor entre 0 e 20: '))
print(f'Você digitou o número {n[num]}')


#EX 073 -----------------------------------------------------------------------

"""
Desafio 073 - Crie uma tupla preenchida com os 20 primeiros colocados da tabela
do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:
    A) Apenas os 5 primeiros colocados;
    B) Os últimos 4 colocados da tabela.
    C) Uma lista com os times em ordem alfabética;
    D) Em que posição da tabela está o time da Chapecoense.
"""
Brasileirão = ('FLAMENGO', 'SANTOS', 'PALMEIRAS', 'GRÊMIO', 'ATHLETICO', 
'SÃO PAULO', 'INTERNACIONAL', 'CORINTHIANS', 'FORTALEZA', 'GOIÁS', 'BAHIA', 
'VASCO', 'ATLÉTICO-MG', 'FLUMINENSE', 'BOTAFOGO', 'CEARÁ', 'CRUZEIRO', 'CSA', 
'CHAPECOENSE', 'AVAÍ')

print(f'Os cincosn Primeiros colocados são: \n{Brasileirão[0:5]}')
print(f'Os 4 últimos colocados são: \n{Brasileirão[-1:-5:-1]}')
print(f'Os 4 últimos colocados são: \n{Brasileirão[-4:]}')
print(f'Os participantes da série A em ordem alfabética:\n{sorted(Brasileirão)}')
print('Chapecoense está na {}ª posição'.format(Brasileirão.index('CHAPECOENSE')+1))
print(f'Chapecoense está na {Brasileirão.index("CHAPECOENSE")+1}ª posição')

#EX 074 -----------------------------------------------------------------------

"""
Desafio 074 - Crie um progama que vai gerar 5 números aleatórios e colocar em 
uma tupla. Depois disso, mostre a listagem de números gerados e também o menor
e o maior valor que estão na tupla
"""
from random import randint

n = ()
while len(n) < 5:
    #NÃO SEI PQ: quando coloco até 10 ele é separado em (1,0) quando sorteado
    #Tuplas tb n aceitam int
    x = tuple(str(randint(0,9)))
    n = x + n
print(f'A tupla aleatória é {n}')
print(f'O menor valor é {min(n)}')
print(f'O maior valor é {max(n)}')

#GUANABARA
from random import randint
n = (randint(0,10),randint(0,10),randint(0,10),randint(0,10),randint(0,10))

print('Os valores sorteados foram: ')
for c in n:
    print(f'{c}', end =' ')
print(f'O menor valor é {min(n)}')
print(f'O maior valor é {max(n)}')

#EX 075 -----------------------------------------------------------------------

"""
Desafio 075 - Desenvolva um programa que leia quatro valores pelo teclado e 
guarde-os em uma tupla. no final mostre:
    a) Quantas vezes apareceu o valor 9
    b) Em que posição foi digitado o primeiro falor
    c) Quais foram os números pares
"""
#MINHA TENTATIVA ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
""" MINHA TENTATIVA 
x=()
while len(x) < 4:
    n = tuple(input('Digite um valor: '))
    x = x + n
print(f'O número 9 aparece {x.count("9")} vezes')

print(f'O número 3 aparece na posição {x.index("3") + 1}')
for c in x:
    if int(c) % 2 ==0:
        print(c)
"""
#GUANABARA ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

num = (int(input('Digite um número: ')), int(input('Digite um número: ')), 
       int(input('Digite um número: ')), int(input('Digite um número: ')))

print(f'Você digitou os valores {num}')
print(f'O valor nove apareceu {num.count(9)} vezes')
if 3 in num:
    print(f'O número 3 apereceu na {num.index(3)+1}ª posição')
else:
    print('O 3 não foi digitado')
print('Os valores pares digitados foram: ', end = '')
for n in num:
    if n % 2 == 0:
        print(n, end = ' ')

#EX 076 -----------------------------------------------------------------------


"""
Desafio 076 - Crie um progama que tenha uma tupla única com nomes de produtos e
seus respectivos preços, na sequência. 

No final, mostre uma listagem de preços, organizando os dados em forma tabular
"""
lista = ('caneta', 10, 'lapis', 8, 'cereja', 15, 'cerveja', 4.57)

""" Não pode ser assim tem que ser com range
for x in lista:
    print([x], '{:20}')
"""
print('-' * 30)
print(f'{"LISTA":^30}')
print('-' * 30)

for pos in range(0, len(lista)):
    if pos % 2 == 0:
        print(f'{lista[pos]:.<30}', end = '')
    if pos % 2 != 0:
        print(f'R$ {lista[pos]:>6.2f}')

#EX 077 -----------------------------------------------------------------------

"""
Desafio 077 - Crie um progama que tenha uma tupla com várias palavras (não usar
acentos). Depois disso, você deve mostrar, para cada palavra, quais são suas 
vogais.
"""

palavras = ('sol', 'lua', 'estrelas', 'mar', 'cheiro', 'amor', 'esforço', 
            'trabalho')
for p in palavras:
    print(f'\nNa palavra {p.upper()} temos: ', end = ' ')
    for letra in p:
        if letra in 'aeiou':
            print(letra.lower(), end = ' ')

#EX 078 -----------------------------------------------------------------------

"""
DESAFIO 078 - Faça um progama que leia 5 valores numéricos e guarde-os em uma
lista. 

No final mostre qual foi o maior e o menor valor digitado  e as suas 
respectivas posições na lista.
"""

x = []
me = ma = 0
while len(x) < 5:
    x.append(int(input('Digite um valor: ')))
    for pos, v in enumerate(x):
        if pos == 0 or v < me:
            me = v
            pme = pos + 1
        if v > ma:
            ma = v
            pma = pos + 1
print(f'Sua lista é {x}')
print(f'O menor valor da lista é {me} na {pme}ª posição')
print(f'O maior valor da lista é {ma} na {pma}ª posição')

#Minha solução não considerou os maiores valores se repetirem
#Refazendo com considerações do Guana

x = []
me = ma = 0
for c in range(0,5):
    x.append(int(input('Digite um valor: ')))
    if c == 0 or x[c] < me:
        me = x[c]
    if x[c] > ma:
        ma = x[c]
print(f'Sua lista é {x}')
print(f'O menor valor da lista é {me} nas posições: ', end = '')
for i, v in enumerate(x):
    if v == me:
        print(f'{i}...', end= '')
print(f'O maior valor da lista é {ma} nas posições: ', end = '')
for i, v in enumerate(x):
    if v == ma:
        print(f'{i}...', end= '')

#EX 079 -----------------------------------------------------------------------

"""
Desafio 079 - Crie um progama onde o usuário possa digitar vários valores 
numéricos e cadastre-os em uma lista. Caso o número já exista lá dentro ele não
será adicionado. No final, serão exibidos todos os valores únicos digitados, 
em ordem crescente.
"""

l = []
while True:
    l.append(int(input('Digite um valor: ')))
    if l.count(l[-1]) == 1:
        print('Valor adicionado com sucesso!')
    elif l.count(l[-1]) > 1:
        print('Valor duplicado, não será adicionado!')
        l.pop()
    contin = (str(input('Quer continuar? [S/N] '))).upper()[0]
    while contin not in 'SN':
        contin = (str(input('Quer continuar? [S/N] '))).upper()[0]
    if contin in 'N':
        break
print(f'Você digitou a lista {l}')
l.sort()
print(f'Colocando em ordem crescente ela fica {l}')

#GUANABARA

l = []
while True:
    n = int(input('Digite um valor: '))
    if n not in l:
        l.append(n)
        print('Valor adicionado com sucesso!')
    else:
        print('Valor já digitado, não será adicionado!')
    contin = (str(input('Quer continuar? [S/N] '))).upper()[0]
    while contin not in 'SN':
        contin = (str(input('Quer continuar? [S/N] '))).upper()[0]
    if contin in 'N':
        break
print(f'Você digitou a lista {l}')
l.sort()
print(f'Colocando em ordem crescente ela fica {l}')

#EX 080 -----------------------------------------------------------------------


"""
Desafio 080 - Crie um progama onde o usuário possa digitar cinco valores 
numéricos e cadastre-se em uma lista, já na posição correta de inserção 
(sem usar o sort()).

No final, mostre a lista ordenada na tela.
"""
l = []
for c in range(0,5):
    n = int(input('Digite um número: '))
    if c == 0 or n > l[c-1]:
        l.append(n)
    elif n < min(l):
        l.insert(0,n)
    else: 
        for i, x in enumerate(l):
            if l[i-1] < n < l[i]:
                l.insert(i,n)
    print(f'O valor {n} foi adicionado na posição {l.index(n)}')
print(l)

#GUANABARA

lista = []
for c in range(0,5):
    n = int(input('Digite um valor: '))
    if c == 0 or n > lista[-1]:
        lista.append(n)
    else:
        pos = 0 
        while pos < len(lista):
            if n <= lista[pos]:
                lista.insert(pos, n)
                break
            pos += 1
print(l)

#EX 081 -----------------------------------------------------------------------

"""
Desafio 081 - Crie um progama que vai ler vários números e colocar em uma lista.
Depois disso, mostre:
    a) Quantos números foram digitados.
    b) A lista de valores, ordenada de forma decrescente.
    c) se o valor 5 está ou não na lista.
"""

l = []
while True:
    l.append(int(input('Digite um valor: ')))
    contin = ' '
    while contin not in 'SN':
        contin = (str(input('Quer continuar? [S/N] '))).upper()[0]
    if contin == 'N':
        break
print(f'Você digitou {len(l)} números')
l.sort(reverse=True)
print(f'Em ordem decrescente eles ficam {l}')
if 5 in l:
    print('O número 5 está na lista')
else:
    print('O número 5 não está na lista')

#EX 082 -----------------------------------------------------------------------

"""
Desafio 082 - Crie um progama que vai ler vários números e colocar em uma lista.

Depois disso, crie duas listas extras que vão contar apenas os valores pares e 
os valores ímpares digitados, respectivamente.

Ao final, mostre o conteúdo das três listas geradas.
"""

l = []
while True:
    l.append(int(input('Digite um valor: ')))
    contin = ' '
    while contin not in 'SN':
        contin = (str(input('Quer continuar? [S/N] '))).upper()[0]
    if contin == 'N':
        break
p = []
i = []
for v in l:
    if v % 2 ==0:
        p.append(v)
    elif v % 2 != 0:
        i.append(v)

print(f'A lista completa é {l};\nA de pares é {p};\nA de ímpares é {i}.')

#EX 083 -----------------------------------------------------------------------


"""
Desafio 083 - Crie um progama onde um usuário digite uma expressão qualquer que
use parenteses. Seu aplicativo deverá analisar se a expressão passada esta com
os parênteses abertoe e fechados na ordem correta.
"""
#ERREI. A minha não mostra hierarquia

l = str(input('Digite a expressão: '))
d = 0
f = 0

for i, c in enumerate(l):
    if l[i] == '(':
        d += 1
    elif l[i] == ')':
        f += 1

if d == f:
    print('Expressão válida')
else:
    print('Expressão inválida')
     

#Guanabra

expr = str(input('Digite a expressão: '))
pilha = []
for símb in expr:
    if símb == '(':
        pilha.append('(')
        print(pilha, 'if (')
    elif símb == ')':
            if len(pilha) > 0:
                pilha.pop()
                print(pilha, 'if )')
            else:
                pilha.append(')')
                print(pilha, 'else')
                break
if len(pilha) == 0:
    print('Expressão válida')
else:
    print('Expressão inválida')

#EX 084 -----------------------------------------------------------------------

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

#EX 085 -----------------------------------------------------------------------

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

#Como o gunabara queria que resolvesse:

valor = 0
num = [[], []]
for c in range(1,8):
    v = int(input(f'Digite o {c}º valor: '))
    if v % 2 == 0:
        num[0].append(v)
    else:
        num[1].append(v)
num[0].sort()
print(f'Os valores pares são {num[0]}')
num[1].sort()
print(f'Os valores pares são {num[1]}')

#EX 086 -----------------------------------------------------------------------

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
    for z in l:
        print(f'[{z:^5}]', end = '')
    print()


#EX 087 -----------------------------------------------------------------------

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
    for z in l:
        print(f'[{z:^5}]', end = '')
    print()

for x, y in enumerate(matriz):
    for z, f in enumerate(y):
        if f % 2 == 0:
            spa += f
        if z == 2:
            s3 += f
        elif x == 1:
            if y[z] > ma:
                ma = f
print(f'A soma dos valores pares é {spa}.')
print(f'A soma dos valores da terceira coluna é {s3}')
print(f'O maior valor da segunda linha é {ma}')

#EX 088 -----------------------------------------------------------------------

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
        x = randint(1,60)
        if x not in j:
            j.append(x)
    j.sort()
    T.append(j[:])
    j.clear()
print(f'Você solicitou {n} jogos e eles são: ')    
for i, x in enumerate(T):
    print(f'Jogo {i+1}: {x}')
    sleep(1)

#EX 089 -----------------------------------------------------------------------

"""
Desafio 089 - Crie um progama que leia nome e duas notas de vários alunos e 
guarde tudo em uma lista composta. No final, mostre um boletim contendo a 
média de cada um e permita que o usuário possa mostrar as notas de cada aluno 
individualmente.
"""

# =============================================================================
# Eu queria resolver esse exerrcicio sem utilizar duas variáveis para nota mas 
# não consegui. Tive que criar nota 1 e nota2 para calcular a média. Não sei 
# como acessar um valor em uma lista e fazer calculos com ele.
# =============================================================================

# O ERRO ACIMA OCORRIA PQ EU TRANSFORMAVA CADA UM DOS COMPONENTES DA LISTA 
# EM UMA LISTA, AÍ NÃO DAVA PARA REALIZR OPERAÇÕES COM ELAS

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

#EX 090 -----------------------------------------------------------------------

"""
Desafio 090 - Faça um progama que leia nome e média de um aluno, guardando 
também em um dicionário. No final mostre o conteúdo da estrutura na tela.
"""

alu = {}

alu['Nome'] = str(input('Nome: '))
alu['Média'] = int(input('Média: '))
if alu['Média'] >= 5:
    alu['Situação'] = 'Aprovado'
else:
    alu['Situação'] = 'Reprovado'

for k, v in alu.items():
    print(f'{k} é igual a {v}')

#EX 091 -----------------------------------------------------------------------

"""
Desafio 091 - Crie um progama onde 4 jogadores joguem um dado e tenham 
resultados aleatórios. Guarde esses resultados em um dicionário. No final, 
coloque esse dicionário em ordem, sabendo que o vencendor tirou o maior número 
no dado

OBS.: - DICIONÁRIO EM ORDEM 
      - ORDEM CRESCNTE
"""
# =============================================================================
# AVISO!!!!
# =============================================================================
"""
Tentei realizar essa questão fazendo um laço mas ainda não sei ao certo como.
Resolverei como o Guanabara resolveu.

for j in range(1,5):
    dados['jogador{j}'] = randint(1,6)
    print(f'O jogador {j} tirou {dados["Resultado"]}')
    sleep(1)
print(dados)

ranking = {}
ranking - sorted(dados)
"""

from random import randint
from time import sleep
from operator import itemgetter

jogo = {'jogador1': randint(1,6), 'jogador2': randint(1,6),
        'jogador3': randint(1,6),'jogador4': randint(1,6)}
ranking = []
for k, v in jogo.items():
    print(f'O {k} tirou {v}')
    sleep(1)
ranking = sorted(jogo.items(), key = itemgetter(1), reverse = True)
print('Ranking ddos jogadores')
for i, n in enumerate(ranking):
    print(f'{i+1}º lugar: {n[0]} com {n[1]}')
    sleep(1)

#EX 092 -----------------------------------------------------------------------

"""
Desafio 092 - Crie um progama que leia nome, ano de nascimento e carteira de 
trabalho e cadastre-os (com idade) em um dicionário, se por acaso a CTPS for 
diferente de zero, o dicionário receberá també o ano de contratação e o 
salário. Calcule e acrescente, além da idade, com quantos anos a pessoa vai 
se aposentar.

35 anos de contribuição para se aposentar
"""

from datetime import date

ano_atual = date.today().year
print(ano_atual)
BT = {}

BT['Nome'] = str(input('Nome: '))
x = int(input('Ano de Nacimento: '))
BT['Idade'] = ano_atual - x
BT['CTPS'] = int(input('Carteira de Trabalho (0 caso não tenha): '))
if BT['CTPS'] != 0:
    BT['Contratação'] = int(input('Ano de contratação: '))
    BT['Sal'] = float(input('Salário: '))
    BT['aposentadoria'] = BT['Contratação'] + 35 - x

for k, v in BT.items():
    print(f'{k} tem valor {v}')

#EX 093 -----------------------------------------------------------------------

"""
Desafio 093 - Crie um progama que gerencie o aproveitamento de um jogador de 
futebol. O progama vai ler o nome do jogador e quantas partidas ele jogou. 
Depois vai ler a quantidade de gols feitos em cada partida. No fim, tudo isso 
será guardado em um dicionário, incluindo total de gols feitos durante o 
campeonato.
"""

gols = []
BJ = {}
total = 0
BJ['nome'] = str(input('Nome do jogador: '))
BJ['partidas'] = int(input('Quantidade de partidas: '))
for c in range(0, BJ['partidas']):
    gols.append(int(input(f'Quantos gols ele fez no jogo {c+1}? ')))
BJ['total'] = sum(gols)
BJ['gols'] = gols[:]
print('=-'*12)
for k, v in BJ.items():
    print(f'O campo {k} tem valor {v}')
print('=-'*12)  
print(f'O jogador {BJ["nome"]} fez {BJ["total"]} gols em {BJ["partidas"]} jogos')
for i, p in enumerate(gols):
    print(f'=> No jogo {i+1}, fez {p} gols')

#EX 094 -----------------------------------------------------------------------

"""
Desafio 094 - Crie um progama que leia nome, sexo e idade de várias pessoas, 
guardando os dados de cada pessoa em um dicionário e todos os dicionários em 
uma lista. No final, mostre:
    A) Quantas pessoas foram cadastradas;
    B) A média de idade do grupo;
    C) Uma lista com todas as mulheres;
    D) Uma lista com todas as pessoas com idade acima da média.
"""

L = []
P = {}
soma = 0
while True:
    P.clear()
    P['Nome'] = str(input('Nome: '))
    P['Sexo'] = str(input('Sexo [M/F]: ')).upper().strip()[0]
    while P['Sexo'] not in 'MF':
        P['Sexo'] = str(input('Sexo [M/F]: ')).upper().strip()[0]
    P['Idade'] = int(input('Idade: '))
    soma = soma + P['Idade'] 
    L.append(P.copy())
    continuação = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    while continuação not in 'SN':
        print('Erro!!! digite um valor válido')
        continuação = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if continuação == 'N':
        break

média = soma/len(L)
print(f'Ao todo, tivemos {len(L)} pessoas cadastradas')
print(f'A média de idade é {média:5.2f} anos')
for p in L:
    if p['Sexo'] in 'F':
        print(f'Lista de Mulheres: {p["Nome"]}')
    if p['Idade'] > média:
        print(f'Lista de pessoas com idade acima da média = {p["Nome"]}')
print(L)
print(P)

#EX 095 -----------------------------------------------------------------------

""" 
Desafio 095 - Aprimore o Desafio 093 para que ele funcione com vários
jogadores, incluindo um sistema de visualização de detalhes de aproveitamento 
do jogado que for indicado
"""

time = []
gols = []
jogador = {}
while True:
    jogador['nome'] = str(input('Nome do jogador: '))
    jogador['partidas'] = int(input('Quantidade de partidas: '))
    for c in range(0, jogador['partidas']):
        gols.append(int(input(f'Quantos gols ele fez no jogo {c+1}? ')))
        jogador['gols'] = gols[:]
    jogador['total'] = sum(gols)
    time.append(jogador.copy())
    jogador.clear()
    gols.clear()
    continuação = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    while continuação not in 'SN':
        print('Erro!!! digite um valor válido')
        continuação = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if continuação == 'N':
        break
print(time)
print('=-'*20)
print(f'{"COD":<3} {"Nome":12} {"Partidas":<8}  {"Gols":<20} {"Total":^5}')

for k, v in enumerate(time):
    print(f'{k:<3} {v["nome"]:12} {v["partidas"]:<8}  {str(v["gols"]):<20} {v["total"]:^5}')
print('=-'*20)
while True:
    x = int(input('Mostrar dados de qual jogador? [999 p/ sair] '))
    if x == 999:
        break
    print(f'O jogador {time[x]["nome"]} fez {time[x]["total"]} gols em {time[x]["partidas"]} jogos')
    for i, p in enumerate(time[x]['gols']):
        print(f'=> No jogo {i+1}, fez {p} gols')
    
# =============================================================================
# Aqui embaixo imprimirei uma base com base em key e values (FERRAMENTA UTIL)
# =============================================================================
print('Cod', end = ' ')
for k in time[0].keys():
    print(f'{k:^20}', end = '')
print()
for i, jog in enumerate(time):
    print(f'{i:^3}', end = '')
    for v in jog.values():
        print(f'{str(v):^20}', end = '')
    print()

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

def sorteia(lista):
    for i in range(0, 5):
        x = randint(0, 100)
        lista.append(x)
    print(lista)
def somaPar(lista):
    sp = 0
    for n in lista:
        if n % 2 == 0:
            sp += n
    if sp != 0:
        print(f'A soma dos números pares foi {sp}')
    else:
        print('Não houveram números pares a serem somados')

números = []
sorteia(números)
somaPar(números)


"""
Desafio 101 - Crie um programa que tenha uma função chamada voto() que vai 
receber como parâmetro o ano de nascimento de uma pessoa, retornando um valor 
literal indicando se uma pessoa tem voto Negado, Opcional ou Obrigatório nas 
eleições.
"""

def voto(ano):
    from datetime import date
    hoje = int(date.today().year)
    idade = hoje - ano
    if idade < 16:
        return f'Com {idade} anos: Não vota'
    elif 16 <= idade < 18 or idade > 65:
        return f'Com {idade} anos: Voto opcional'
    else:
        return f'Com {idade} anos: Voto Obrigatório'

print(voto(2005))

"""
Desafio 102 - Crie um programa que ternha uma função fatorial() que receba 
dois parâmetros: o primeiro que indique o número a calcular e o outro chamado 
show, que será um valor lógico (opcional) indicando se será mostrado ou não na 
tela o processo de cálculo fatorial.
"""

def fatorial(n, show=False):
    """
    Função que retorna o Fatorial do Número

    Parameters
    ----------
    n : int
        O número que você deseja o fatorial.
    show : bool, optional
        Caso seja True ele mostr o processo de cáculo da fatorial. The default is False.

    Returns
    -------
    None.

    """
    f = 1
    for i in range(1, n+1):
        f *= i
        if show:
            print(f'{i}', end = '')
            print(' x ' if i < n else ' = ', end = '')
    return f


fatorial(5, show=True)

help(fatorial)

"""
Desafio 103 - Faça um programa que tenha uma função chamada ficha(), que 
receba dois parâmetros opcionais: o nome de um jogador e quantos gols ele 
marcou. 

O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum 
dado não tenha sido informado corretamente
"""
def ficha(nome='desconhecido',gols=0):
    if nome is not str:
        nome = 'desconhecido'
    if gols is not int:
        gols = 0
    return f'O jogador {nome} marcou {gols}'

ficha(4, 'xx')


"""
Desafio 104 - Crie um programa que tenha a função leiaint(), que vai funcionar
de forma semelhante à função input() do Python, só que fazendo a validação
para aceitar apenas um valor numérico.

Ex:
    n = leiaInt('Digite um n')
"""
def leiaInt(inp='Digite um número: '):
    n = input(inp)
    
    if n.isnumeric():
        n = int(n)
        return f'Você digitou o número {n}.'
    else:
        while n.isnumeric() is False:
            print('Digite um número inteiro!!!')
            n = input(inp)
        return f'Você digitou o número {n}.'

leiaInt()
leiaInt()
leiaInt()

inp = 'Digite um número: '
n = input(inp)
type(n)
while n is not int():
    print('Digite um número inteiro!!!')
    n = input(inp)

print(f'Você digitou o número {n}.')

"""
Desafio 105 - Faça um programa que tenha um afunção notas() que pode receber 
várias notas e vai retornar um dicionário com as seguintes informações:
    
    - Quantidade de notas
    - A maior nota
    - A menor nota
    - A média da turma
    - A situação(opcional)

Adicione também as docstrings
"""
def notas(*notas, sit=False):
    maior = menor = media = soma = 0
    quantidade = len(notas)
    for n in notas:
        if n > maior:
            maior = n
        if n < menor or menor == 0:
            menor = menor
        soma += n
    media = soma/quantidade
    
    dados = {}
    dados['quantidade'] = quantidade
    dados['maior'] = maior
    dados['menor'] = menor
    dados['media'] = media
    
    if sit == True:
        if media < 5:
            situaçao = 'Ruim'
        elif 5 <= media < 7:
            situaçao = 'Razoável'
        else:
            situaçao = 'Ruim'
        
        dados['situaçao'] = situaçao

    return dados



notas(4.5, 4.8, 9, sit=True)

"""
Desafio 106 - Faça um mini-sistema que utilize o interactiveHelp do Python. O 
usuário vai digitar o comando e o manual vai aparecer. Quando o usuário 
digitar a palavra 'FIM', o programa se encerrará.
"""
def manual(comando):
    x = help(comando)
    return x

manual(print)














