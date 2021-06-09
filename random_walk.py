# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt

def randomwalk(largo):
    pasos=np.random.randint (-1,2,largo)  
    return pasos.cumsum()

N = 100000

#%%
plt.subplot(2, 1, 1)
mindist = 10000 
maxdist = -10000 #inicializo con valor alto porque después cuento con que
                #la distancia no llega a ese límite
lmax = []
lmin = []

for i in range(12): 
    l = list(randomwalk(N)) #hace una lista con los valores de cada línea
    p = plt.plot(l) #dibuja esa lista
    maximo = max(l)
    lmax.append(maximo) #hace lista de máximos
    minimo = min(l)
    lmin.append(minimo) #hace lista de mínimos
    #print(lmax, lmin)
   
    dist = abs(maximo - minimo)
    #print(f'La distancia es {dist}')
    
    if dist < mindist: #guarda la lista y la distancia si ésta es la menor hasta el momento
        mindist = dist
        minl = l
    if dist > maxdist: #guarda la lista y la distancia si ésta es la mayor
        maxdist = dist
        maxl = l
        

plt.xlabel('Tiempo')
plt.ylabel('Distancia al origen')
plt.title('12 caminatas al azar')

#%%
plt.subplot(2, 2, 3)
plt.plot(maxl)
plt.title('La caminata que más se aleja')
plt.ylim(-600, 600)

#%%
plt.subplot(2, 2, 4)
plt.plot(minl)
plt.title('La caminata que menos se aleja')
plt.ylim(-500, 500)

#%%
plt.tight_layout()
plt.show()