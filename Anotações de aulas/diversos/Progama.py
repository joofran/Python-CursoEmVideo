# -*- coding: utf-8 -*-
"""
Created on Thu Apr 30 09:26:51 2020

@author: jfpas
"""

Projetos = []

while True:
    Projetos.append(str(input('Projeto: ')))
    if Projetos[-1] == 'parar':
        break
    Projetos.append(str(input('Autoria: ')))

for i, c in enumerate(Projetos):
    if i % 2 == 0:
        print(f'*{c} (--)*')
    else:
        print(f'*Autoria:* Dep. {c} - ')
        print()






















