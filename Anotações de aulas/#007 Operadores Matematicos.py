# -*- coding: utf-8 -*-
"""
Created on Fri Feb 21 22:42:43 2020

@author: jfpas
"""

#07 Operadores Aritméricos
"""
Os opradores aritméticos presentes no Python sãp representados como abaixo:
+  Adição
-  Subtração
*  Multiplicação
/  Divisão
** Potenciação -> Também pode ser feita pela função pow(,)
// Divisão inteira 
%  Resto da divisão (Módulo)

ORDEM DE PRECEDÊNCIA
1.() -> no py, utilizamos apenas () para operações aritméticas, esqueça [] e {}
2.**
3.*;/;//;%
4.+;-

"""

#Funcionalidade do Print

nome = input('Qual é seu nome? ')
print('Prazer em te conhecer {:20}!'.format(nome))
print('Prazer em te conhecer {:>20}!'.format(nome))
print('Prazer em te conhecer {:+<20}!'.format(nome))
print('Prazer em te conhecer {:^20}!'.format(nome))
print('Prazer em te conhecer {:=^20}!'.format(nome))

#Quando não se precisa da soma em outras partes do código, não precisamos criar
#... uma variavel para ele e escrever da forma abaixo:

n1 = int(input('Um valor: '))
n2 = int(input('Outro valor: '))
print('A soma vale {}'.format(n1+n2))
    
#Explorando a construção acima

num1 = int(input('Qual o primeiro número? '))
num2 = int(input('Qual o segundo número? '))

s = num1+num2
p = num1*num2
d = num1/num2
di = num1//num2
e = num1**num2

print('A soma é {}, o produto é {} e a divisão é {}'.format(s,p,d))
print('A divisão inteira é {} e a potência, {}'.format(di,e))

#para limitar as casas decimais:

print('A divisão é {:.2f}'.format(d))

#para não quebrar a linha utiliza-se end='', como abaixo:
print('A soma é {}, o produto é {} e a divisão é {}'.format(s,p,d), end=' ')
print('A divisão inteira é {} e a potência, {}'.format(di,e))

#para quebrar a linha utiliza-se \n, como abaixo:
print('A soma é {},\no produto é {}\ne a divisão é {}'.format(s,p,d))

"""
Desafio 005 - Faça um programa que lei aum número e mostre na tela o seu 
sucessor e o seu antecessor
"""
nn1 = int(input('Qual o número? '))
print('O antecessor de {} é {}, e o seu sucessor é {}'.format(nn1,nn1-1,nn1+1))

"""
Desafio 006 - Crie um algoritmo que leia um número e mostre o seu dobre,
triplo e raiz quadrada.
"""

print('O dobro de {} é {}, o seu triplo é {} e a sua raiz quadrada é {}'
      .format(nn1,nn1*2,nn1*3,nn1**(1/2)))

"""
Desafio 007 - Desenvolva um programa que leia as duas notas de um aluno, 
e mostre a sua média
"""

p1 = float(input('Qual foi a priimeira nota? '))
p2 = float(input('Qual foi a segunda nota? ' ))

print('A sua média foi {}'.format((p1+p2)/2))

"""
Desafio 008 - Escreva um programa que leia um valor em metros e o exiba 
convertido em centímetros e em milímetros
"""

cov=float(input('Qual valor em metros você deseja converter?'))
print('O valor de {} metros em centímetros é {:2f}, e em milímetros é {}'
      .format(cov,cov*100,cov*1000))

"""
Desafio 009 - Faça um programa que leia um número inteiro qualquer e mostre na
 tela a sua tabuada
"""

t = int(input('Qual o número que você deseja saber a tabuada? '))

print('1x{}={}\n2x{}={}\n3x{}={}\n4x{}={}'.format(t,t*1,t,t*2,t,t*3,t,t*4))
print('5x{}={}\n6x{}={}\n7x{}={}\n8x{}={}'.format(t,t*5,t,t*6,t,t*7,t,t*8))
print('9x{}={}\n10x{}={}'.format(t,t*9,t,t*10))

"""
Desafio 10 - Crie um programa que leia quanto dinheito uma pessoa tem na
carteira e mostre quantos dólares ela pode comprar.
Considere US$1.00=R$3.27
"""

real = float(input('Quantos reais você possui na carteira? '))
dol = real/3.27

print('Com {} reais você pode comprar {}'.format(real,dol))

"""
Desafio 11 - Faça um programa que leia a largura e a altura de uma parede em 
metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, 
sabendo que cada litro de tinta, pinta uma área de 2m²
"""

h = float(input('Qual a altura da parede?' ))
l = float(input('Qual a largura da parede?' ))

A = h*l
lt = A/2

print('A área da parede é {}, portanto, serão necessários {}'.format(A,lt), 
      'litros de tinta para pintá-la')

"""
Desafio 12 - Faça um algoritmo que leia um preço do produto e mostre seu novo 
preço, com 5% de desconto.
"""

pç = float(input('Qual o preço do produto? '))

print('O preço do produto com 5% de desconto é: {}'.format(pç*0.95))

"""
Desafio 13 - Faça um algoritmo que leia o salário de um funcionário e mostre 
seu novo salário, com 15% de aumento
"""

sal = float(input('Qual é o salário do funcionário? '))
print('O salário do funcionário com 15% de aumento é {}'.format(sal*1.15))
















