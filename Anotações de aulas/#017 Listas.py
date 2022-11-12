# -*- coding: utf-8 -*-
"""
Created on Wed Apr 22 01:57:54 2020

@author: jfpas
"""

"""
ESTUDAREMOS LISTAS !!!!!!!!

________________Introidução:

*Listas, assim como as tuplas, são variáveis compostas. 
*O grande diferencial das lisatas é a sua capacidade de ser mutáveis. Podemos 
adicionar valores ou mudar a sua composição
*Identificamos listas com colchetes []

PARA DECLARAR UMA LISTGA:
    Podemos usar a função list:
        valores = list(range(4,11)) 
    Ou podemos usar os colchetes:
        valores = [4, 5, 8, 10, 56]


-----------MUTAÇÕES NAS LISTAS:

OBS.: nas anotações abaixo:
    - n representa o índice da lista
    - x represente um valor qualquer
    
*para aumentar listas:
    - lista.append('x') 
    - ou lista.insert(n,'x') 

*para apagar um valor de uma lista: 
    - del lista[n] ou 
    - lista.pop(n) ou 
    - lista.remove('x')
        .if 'x' in lista:
            lista.remove('x')

*para alterar um valor x da lista:
    - lista[n] = 'x'
    
--------------FUNCIONALIDADES:
    
*PARA ORDENAR UMA LISTA:
    valores = [60, 5, 22, 10, 56]
    valores.sort () = [5, 10, 22, 56, 60]
    
*ORDENAR REVERSAMENTE:
    valores.sort(reverse=True) = [60, 56, 22, 10, 5]

*DESCOBRIR O TAMANHO DE UMA LISTA
    len(valores) = 5
"""

num = 2, 5, 9, 1
print(num) #(2, 5, 9, 1)
num[2] = 3 #não pode pq tupla é imutável

num = [2, 5, 9, 1]
num[2] = 3
print(num) # [2, 5, 3, 1]
'num [4] = 7' #Não pode adicionar valores na lista assim
num.append(7) #forma correta de adicionar valor na lista
print(num) # [2, 5, 3, 1, 7]
num.sort() #ordena os valores
print(num) # [1, 2, 3, 5, 7]
num.sort(reverse = True) #ordena os valores reversamente
print(num) # [7, 5, 3, 2, 1]
num.insert(2, 0) #insere o valor 0 na posição 2
print(num) #[7, 5, 0, 3, 2, 1]
print(len(num)) #comprimento da lista que é 6
num.pop() #elimina o último valor
print(num) #[7, 5, 0, 3, 2]
num.pop(2) #elimina o elemento na posição 2
print(num) #[7, 5, 3, 2]
num.insert(2,2) #Insere na posição 2 o elemento 2
print(num) #[7, 5, 2, 3, 2]
num.remove(2) #Vai eleiminar apenas o primeiro número 2
print(num) #[7, 5, 3, 2]
num.remove(4) #remover um valor que não esta na lista retorna em erro
if 4 in num: 
    num.remove(4) #resolvendo o problema acima

#--------------------------------------

valores = []
valores.append(5)
valores.append(9)
valores.append(4)

print(valores) #[5, 9, 4]

for v in valores:
    print(f'{v}...', end = '') #5...9...4...
for c, v in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {v}...') 
'''Na posição 0 encontrei o valor 5...
Na posição 1 encontrei o valor 9...
Na posição 2 encontrei o valor 4...'''

#------------------

valores = list()
for cont in range(0,5):
    valores.append(int(input('Digite um valor:')))
for c, v in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {v}...') 

#------------------------------
#Quando igualamos listas no Python existe uma ligação entre elas
a = [2, 3, 4, 7]
b = a
b[2] = 8

print(a) #[2, 3, 8, 7]
print(b) #[2, 3, 8, 7]

#Para criar uma cópia e não uma ligação de listas
a = [2, 3, 4, 7]
b = a[:]
b[2] = 8

print(a) #[2, 3, 4, 7]
print(b) #[2, 3, 8, 7]


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
    if contin == 'N':
        break
print(f'Você digitou a lista {l}')
l.sort()
print(f'Colocando em ordem crescente ela fica {l}')

"""
Desafio 080 - Crie um progama onde o usuário possa digitar cinco valores 
numéricos e cadastre-se em uma lista, já na posição correta de inserção 
(sem usar o sort()).

No final, mostre a lista ordenada na tela.
"""
l = []
for c in range(0,5):
    n = int(input('Digite um número: '))
    if c == 0:
        l.append(n)
    elif n < min(l):
        l.insert(0,n)
    elif n > l[c-1]:
        l.append(n)              
    else: 
        for i, x in enumerate(l):
            if l[i-1] < n < l[i]:
                l.insert(i,n)
    print(f'O valor {n} foi adicionado na posição {l.index(n)}')
print(l)

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
    print('o número 5 não está na lista')

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

"""
Desafio 083 - Crie um progama onde um usuário digite uma expressão qualquer que
use parenteses. Seu aplicativo deverá analisar se a expressão passada esta com
os parênteses abertoe e fechados na ordem correta.
"""

l = str(input('Digite a expressão: '))
d = 0
f = 0

for i, c in enumerate(l):
    if c == '(':
        d =+ 1
    elif c == ')':
        f =+ 1
if d == 0 and ')' in l:
    print('Expressão inválida')
elif d == f:
    print('Expressão válida')
else:
    print('Expressão inválida')
        
        
        








