
def propagar(lista):
    '''
    Recorre la lista original y crea una segunda lista con los 1 propagados a la derecha
    '''

    pos = 0
    nueva_l = []
    pos_fuego = lista.index(1)
    
    for e in lista:
        pos += 1
        if e == 0:
            if pos == (pos_fuego +1):
                e = 1
                pos_fuego = pos
            
            #Esto funcionaba pero no tomaba el último 0 de la izq de la propagación
            #así que empecé a invertir listas
            #if pos == (pos_fuego -1): 
             #   e = 1
              #  pos_fuego = pos
                
        elif e == 1: 
            pos_fuego = pos

        nueva_l.append(e)

    '''
    Crea una tercera lista con la inversa de la segunda.
    '''
    invertida = []
    i = len(lista)
    
    for x in nueva_l:
        i = i -1 
        invertida.append(nueva_l[i])
        
        
    '''
    Recorre la tercera lista y crea una cuarta con los 1 propagados a la derecha
    '''    
    
    pos_inv = 0
    pos_f_inv = invertida.index(1)
    
    l_interm = []
        
    for x in invertida:
        pos_inv += 1
        
        if x == 0:
            if pos_inv == (pos_f_inv +1):
                x = 1
                pos_f_inv = pos_inv
                
        elif x == 1: 
            pos_f_inv = pos_inv

        l_interm.append(x)
        
    '''
    Crea una quinta lista con la inversa de la cuarta.
    '''    
    
    l_final = []
    h = len(l_interm)
        
    for y in l_interm:
        h = h -1 
        l_final.append(l_interm[h])
       
    return l_final


l = [0, -1, 0, 1, 0, 0, 1, -1, 1, 0,-1, 0, 0,-1, 0, 1, 0, 0, 1]

print(propagar(l))
