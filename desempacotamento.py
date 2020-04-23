# coding: utf-8
#desempacotamento
*a,b = [1,2,3,4]
a
b
from random import randint
argumentos = (1,20)
randint(*argumentos)
argumnetos = {"sep": "\t","end":"$$$\n$$$"}
argumentos = {"sep": "\t","end":"$$$\n$$$"}
print('oi','galera','da','quarentena',**argumentos)
def xpto(*args)
def xpto(*args):
    return *args
def xpto(*args):
    return args
    
def ypto(**kwargs):
    return kwargs
    
xpto(1,2,3,4)
ypto('1'=1,'2'=2)
ypto(a=1,b=2)
def soma_pares(*numbers):
    total = 0
    for i in *numbers:
        if i%2 == 0:
            total = total+i
def soma_pares(*numbers):
    total = 0
    for i in numbers:
        if i%2 == 0:
            total = total+i
    return total
    
soma_pares(1,2,3,4)
def produto_pares(fator, *args):
    lista = []
    for i in args:
        if i%2 == 0:
            lista.append(fator*i)
    return lista
    
produto_pares(2,1,2,3,4,5,6)
