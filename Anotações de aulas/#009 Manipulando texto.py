# -*- coding: utf-8 -*-
"""
Created on Wed Feb 26 23:04:17 2020

@author: jfpas
"""


frase = 'Curso em Vídeo Python'
frase2 = '   Aprenda Python  '

#1
print('1 é', frase[9:13])
#2
print('2 é', frase[9:21])
#3
print('3 é', frase[9:21:2])
#4
print('4 é',frase[:5])
print('4 tb é',frase [0:5])
#5
print('5 é ',frase[15:])
print('5 tb é ', frase[15:21])
#6
print('6 tb é ',frase[9::3])

frase[1]
frase[1::2]
"""
FATIAMENTO (O PRIMEIRO NÚMERO É ZERO)

É importante lembrar que a contagem de letras em uma string em fatiamento
SEMPRE COMEÇA EM ZERO!!!!!!!

*O primeiro número de um fatiamento indica o inicio em que ele ocorre

**O segundo número do fatiamento indica o fim dele 
(o intervalo percorre até o penultimo número)

***O terceiro número do fatiamento indica o intervalo em que ele ocorrerá

OS EXEMPLOS ACIMA

Curso em Vídeo Python
012345678901234567890 -> Para facilitar a compreensão da númeração

1 - frase[9:13] = Víde
2 - frase[9:21] = Vídeo Python
3 - frase[9:21:2] = VdoPto
4 - frase[:5] == frase [0:5] = Curso
5 - frase[15:] == frase[15:21] = Python
6 - frase[9::3] = VePh

_________FUNÇÔES DE STRING ABAIXO______________________________________________

*1 - len() => retorna quantidade de caracteres

*2 - frase.count() => conta quantas vezes aparece o caractere desejado;

*3 - frase.find() => retorna a posição em que foi encontrada a string em 
questão;

*4 - 'valor' in frase => essa construção devolve true ou false para a
existência ou não do valor na string frase;

*5 - frase.replace('','') => substitui o primeiro valor indicado pelo segundo 
valor  indicado [Essa função não substitui diretamente na string, substitui de 
uma forma secundária].

_____________________FORMATAÇÃO________________________________________________

*1 - frase.upper() => deixa todos os caracteres maiúsculos;

*2 - frase.lower() => transforma todos os caracteres em minúsculos;

*3 - frase.capitalize => transforma o primeiro caractere em maiúsculo e todos;
os outros caracteres em minusculo;

*4 - frase.title => transforma as primeiras letras de cada palavra em 
maiúscula, e o resto fica em minusculo;

*5 - frase.split() => Divide uma string em uma lista, onde cada elemento 
seperado por espaço da string receberá um número 0123... ;
[[OBS.: Existem outras funcionalidades dentro do parenteses que o guanabara não 
explicou;]]

*6 - '-'.join(frase) => Junta uma lista em uma string com o conector 
selecionado, nesse caso o conector é '-' mas pode ser vazio '' também. 
[[OBS.: Esta é uma forma de substituir o replace.]]

REMOVER ESPAÇOS

*1 - frase2.strip => remove todos os espaços inúteis que ficam no inicio ou 
final da string;

*2 - frase2.rstrip => remove os espaços da direita (final da string); 

*3 - frase2.lstrip => remove os espaços da esquerda (início da string)



"""

frase = 'Curso em Vídeo Python'
len(frase)

frase.count('o')
#utilizando count conjuntamente com fatiamento:
frase.count('o',0,13)

frase.find('deo')
frase.find('Android')
#essa construção acima vai retornar o valor -1, dado que ele não existe na 
#string apontada

'Curso' in frase

frase.replace('Python','Android')

frase.upper()
frase.lower()
frase.capitalize

dividido = frase.split()
'-'.join(dividido)


frase2 = '   Aprenda Python  '
frase2.strip()
frase2.rstrip()
frase2.lstrip()

'-----------------------------------------------------------------------------'
#Desafios

"""
Desafio 022 - Crie um programa que leia o nome completo de uma pessoa e mostre:
    - O nome com todas as letras maiúsculas
    - O nome com todas as letras minusculas
    - Quantas letras ao todo (sem considerar espaços)
    - Quantas letras tem o primeiro nome
"""

nome = str(input('Qual o seu nome completo? '))

print(nome.upper())
print(nome.lower())

junta = nome.replace(' ','')
print(len(junta))

separado =nome.split()
print(len(separado[0]))

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
lista_num = num[::1]
#linha abaixo desnecessária. Só a coloquei para ver o que retornava
print(lista_num)

print('O número tem como:')
print('Unidade: {};'.format(lista_num[-1]))
print('Dezena: {};'.format(lista_num[-2]))
print('Centena: {};'.format(lista_num[-3]))
print('Milhar: {}.'.format(lista_num[-4]))

"""
Desafio 024 - Crie um programa que leia o nome de uma cidade e diga se ela 
começa ou não com o nome "SANTO"
"""
n_cidade = str(input('Qual o nome da cidade que você deseja saber? '))

n_cidade_separado = n_cidade.split()

print('A cidade começa com SANTO?\n','SANTO' in n_cidade_separado[0])

"""
Desafio 025 - Crie um programa que leia o nome de uma pessoa e diga se ela tem 
"SILVA" no nome
"""

n_pessoa = str(input('Qual o nome da pessoa? '))

print('Existe SILVA no nome?\n', 'SILVA' in n_pessoa)

"""
Desafio 026 - Faça um programa que leia uma frase pelo teclado e mostre:
    - Quantas vezes aparece a letra "A"
    - Em que posição ela aparece a primeira vez
    - Em que posição ela aparece a última vez
"""
palavra = str(input('Digite a palavra desejada: '))
palavra.find('a')
palavra.find('a')

"""
Desafio 027 - Faça um programa que leia o nome completo de uma pessoa, 
mostrando em seguida o primeiro e o último nome separadamente
Ex.: Ana Maria de Souza
primeiro = Ana
último = Souza
"""
nome = str(input('Digite o nome desejado: '))
nome_separado = nome.split()

print('O primeiro nome é {} e o útlimo é {}'.format(nome_separado[0],
      nome_separado[-1]))















