# -*- coding: utf-8 -*-
"""
Created on Thu Jun 25 00:26:41 2020

@author: jfpas
"""
def fatorial(n):
    f = 1
    for i in range(0, n+1):
        f *= i
    return f

num = int(input('Digite um valor: '))
fat = fatorial(num)
print(f'O fatorial de {num} é {fat}.')