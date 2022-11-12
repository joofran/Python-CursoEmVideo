# -*- coding: utf-8 -*-
"""
Created on Mon Jun  8 16:11:52 2020

@author: jfpas
"""
"""
Docstrings:
    podem ser iniciadas incluindo aspas triplas embaixo da função
"""
def mensagem(msg):
    """
    Parameters
    ----------
    msg : str
        Você inclui a mensagem que deseja imprimir no formato desejado.

    Returns None
    -------
    """
    print('-'*30)
    print(msg)
    print('-'*30)



"""
Paramêtro Opcionais:
    Podemos incluir funções com parâmetros opcionais. Neste caso apenas 
    igualamos o parâmetro em questão a zero.
"""
def soma (a,b,c=0):
    s = a + b + c
    print(s)
soma(2,5,4)
soma(2,4)



"""
Escopo de variáveis:
    As variáveis definidas dentro de uma função funcionam apenas no escopo 
    limitado daquela função. Inclusive se hoverem variáveis com o mesmo nome 
    de variáveis globais no progama, vide exemplo abaixo:
"""
def function():
    n1 = 4
    print(f'n1 dentro vale {n1}')


n1 = 2
function()
print(f'n1 fora vale {n1}')



"""
Contornando escopo de váriaveis:
    Podemos tratar uma variável global sem a função criar uma nova em seu 
    escopo utilizando a chmada global. Vide exemplo
"""
def função():
    global n2
    n2 = 4
    print(f'n1 dentro vale {n2}')


n2 = 2
função()
print(f'n1 fora vale {n2}')



"""
Return em funções:
    Podemos atribuir que as funções retornem o valor que geram. Vide exemplo
"""
def somar(a=0, b=0, c=0):
    s = a + b + c
    return s


s1 = somar(2,5,4)
s2 = somar(2,4)

print(s1, s2)

"""
Desafio 101 - Crie um programa que tenha uma função chamada voto() que vai 
receber como parâmetro o ano de nascimento de uma pessoa, retornando um valor 
literal indicando se uma pessoa tem voto Negado, Opcional ou Obrigatório nas 
eleições.
"""
import datetime as dt

def voto(ano):
    hoje = int(dt.date.today().year)
    idade = hoje - ano
    if idade < 16:
        status = 'Negado'
    elif 16 < idade < 18:
        status = 'Opcional'
    else:
        status = 'Obrigatório'
    print(f' Com {ano} anos: voto {status}')

"""
Desafio 102 - Crie um programa que ternha uma função fatorial() que receba 
dois parâmetros: o primeiro que indique o número a calcular e o outro chamado 
show, que será um valor lógico (opcional) indicando se será mostrado ou não na 
tela o processo de cálculo fatorial.
"""

def fatorial(n, show=False):
    f = 1
    for i in range(1, n+1):
        f *= i
        if show:
            print(f'{i}', end = '')
            print(' x ' if i < n else ' = ', end = '')
    print(f'{f}')


fatorial(10, show=True)

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
    
    if int(n) is True:
        return f'Você digitou o número {n}.'
    else:
        while n is not int():
            print('Digite um número inteiro!!!')
            n = input(inp)
        return f'Você digitou o número {n}.'

leiaInt()
leiaInt()
leiaInt()
'''
inp = 'Digite um número: '
n = input(inp)
type(n)
while n is not int():
    print('Digite um número inteiro!!!')
    n = input(inp)

print(f'Você digitou o número {n}.')
'''



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

"""
Teste de variável global
"""

def test():
    global h1, h2, h3, h4
    h1 = '1h'
    h2 = '2h'
    h3 = '3h'
    h4 = '4h'

test()

h1
h2
h3
h4






