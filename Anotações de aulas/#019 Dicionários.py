# -*- coding: utf-8 -*-
"""
Created on Wed Apr 29 16:12:33 2020

@author: jfpas
"""

"""
DICIONÁRIOS - última estrutura de variável composta

* IDENTIFICADOS POR chaves {} ou pelo comando dict()
* Nos dicionários podemos nomear os índices.  (Nas listas e tuplas apenas o 
identificamos por números)

EXEMPLO:
    dados = {'nome': 'Pedro', 'idade':25}
    - O que fica antes do : são os nomes dos índices

    - print(dados['nome']) retorna Pedro
    - print(dados['idade']) retorna 25

AUMENTANDO DICIONÁRIOS

* O append não funciona, é sódeclarar o novo índice com sua variável que ele é 
adicionado ao dicionário:
        -dados['sexo'] = 'M'

REMOVENDO ELEMENTOS DO DICIONÁRIO

    - del dados['idade']

ENTENDENDO A ESTRUTURA DO DICIONÁRIO:
    1 - KEYS (chaves)
    2 - VALUES (valores)
    3 - ITENS (ITEMS)
    
* No python, os índices nomeados do dicionário se chamam keys(chaves) e eles 
carregam valores:
    
    - filme = {'titulo': 'Star Wars', 'ano': 1977, 'diretor': 'George Lucas'}
        1 - As keys são: 'título'; 'ano';'diretor'
        2 - Os values são: 'Star Wars', 1977, 'George Lucas'
        3 - Os itens são os dois conjuntos acima

EXEMPLO APLICAÇÃO ITEMS:
    for k, v in filme.items():
        print(f'O {k} é {v}')
        
    RETORNO:
        O titulo é Star Wars
        O ano é 1977
        O diretor é George Lucas
        
MISTURANDO LISTAS E DICIONÁRIOS:
    locadora = [{},{}, {}]
    
    
"""
#PRÁTICA

filme = {'titulo': 'Star Wars', 'ano': 1977, 'diretor': 'George Lucas'}

for k, v in filme.items():
    print(f'O {k} é {v}')

pessoas = {'nome': 'Gustavo', 'sexo': 'M', 'idade': 22} 
print(pessoas) #{'nome': 'Gustavo', 'sexo': 'M', 'idade': 22}
print(pessoas[0]) #ERRO -> o elemento 0 é o nome 
print(pessoas['nome']) #Gustavo

print(f'O {pessoas["nome"]} tem {pessoas["idade"]}') #importante diferencias as aspas
# O Gustavo tem 22

print(pessoas.keys()) #dict_keys(['nome', 'sexo', 'idade'])
print(pessoas.values()) #dict_values(['Gustavo', 'M', 22])
print(pessoas.items()) #dict_items([('nome', 'Gustavo'), ('sexo', 'M'), ('idade', 22)])

pessoas['peso'] = 98.5
print(pessoas) #{'nome': 'Gustavo', 'sexo': 'M', 'idade': 22, 'peso': 98.5}

pessoas['nome'] = 'Leandro'
print(pessoas['nome']) #Leandro


#DICIONARIO DENTRO DA LISTA

brasil = []
estado1 = {'uf': 'Rio de Janeiro', 'sigla': 'RJ'}
estado2 = {'uf': 'São Paulo', 'sigla': 'SP'}
brasil.append(estado1)
brasil.append(estado2)



####
estado = {}
brasil = []

for c in range(0,3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla do Estado: '))
    brasil.append(estado.copy()) #o fatiamento [:] não funciona no dicionpario

for e in brasil:
    for k, v in e.items():
        print(f'O campo {k} tem valor {v}')


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

"""
Desafio 091 - Crie um progama onde 4 jogadores joguem um dado e tenham 
resultados aleatórios. Guarde esses resultados em um dicionário. No final, 
coloque esse dicionário em ordem, sabendo que o vencendor tirou o maior número 
no dado
"""

from random import randint
from time import sleep

dados = {}

for j in range(1,5):
    dados['jogador{j}'] = randint(1,6)
    print(f'O jogador {j} tirou {dados["Resultado"]}')
    sleep(1)
print(dados)

ranking = {}
ranking - sorted(dados)

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
BT['idade'] = ano_atual - x
BT['CT'] = int(input('Carteira de Trabalho (0 caso não tenha): '))
if BT['CT'] != 0:
    BT['Ano CT'] = int(input('Ano de contratação: '))
    BT['Sal'] = float(input('Salário: '))
    BT['idade_aposentadoria'] = BT['Ano CT'] + 35 - BT['Nasc']

for k, v in BT.items():
    print(f'{k} tem valor {v}')

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
    BJ['gols'] = gols
    if c == BJ['partidas'] - 1:
        for g in gols:
            total = total + g
        BJ['total'] = total
print('=-'*12)
for k, v in BJ.items():
    print(f'O campo {k} tem valor {v}')
print('=-'*12)  
print(f'O jogador {BJ["nome"]} fez {BJ["total"]} gols em {BJ["partidas"]} jogos')
for i, p in enumerate(gols):
    print(f'=> No jogo {i+1}, fez {p} gols')

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
    P['Nome'] = str(input('Nome: '))
    P['Sexo'] = str(input('Sexo [M/F]: ')).upper().strip()[0]
    while P['Sexo'] not in 'MF':
        P['Sexo'] = str(input('Sexo [M/F]: ')).upper().strip()[0]
    P['Idade'] = int(input('Idade: '))
    L.append(P.copy())
    continuação = ' '
    while continuação not in 'SN':
        print('Erro!!! digite um valor válido')
        continuação = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if continuação == 'N':
        break
for p in L:
    if P['Sexo'] == 'F':
        print(f'Lista de Mulheres: {P["Nome"]}')
    soma = soma + P['Idade']
média = soma/len(L)
print(L)
print(P)

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
    















