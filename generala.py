# -*- coding: utf-8 -*-

import random
from collections import Counter



def tirar():
    tirada = []
    
    for i in range(5):
        tirada.append(random.randint(1,6)) 
    return tirada


t = tirar()
cont = Counter(t)
maximo = max(Counter(t).values())
dados_guard1 = []


for x in cont:
    if cont[x] == maximo:
        dados = x
    
dados_guard1.append(dados)
dados_guard1.append(maximo)


print(f'Tiro y saco {t}')
print(f'Me guardo {maximo} dados de valor {dados}')   

t2 = []

    
for i in range(5 - dados_guard1[1]):
    t2.append(random.randint(1,6)) 


print(f'Tiro de nuevo y saco {t2}')


for x2 in t2:
    if x2 == dados:
        maximo += 1
        

print(f'Tengo {maximo} dados de valor {dados}')


t3 = []

for i in range(5 - maximo):
    t3.append(random.randint(1,6)) 
    
print(f'Tiro una última vez y saco {t3}')


for x3 in t3:
    if x3 == dados:
        maximo += 1
        

print(f'Me anoto {maximo*dados} al {dados}')

#%%
def es_generala(tirada):
    '''Evalúa si sale generala servida'''
    resultado = False
    g1 = [1, 1, 1, 1, 1]
    g2 = [2, 2, 2, 2, 2]
    g3 = [3, 3, 3, 3, 3]
    g4 = [4, 4, 4, 4, 4]
    g5 = [5, 5, 5, 5, 5]
    g6 = [6, 6, 6, 6, 6]
    
    gt = [g1, g2, g3, g4, g5, g6]
    
    for x in gt:    
        if tirada == x:
            resultado = True

    return resultado


#print(tirar())
#print(es_generala(tirar()))
