
class Cola:
    '''Representa a una cola, con operaciones de encolar y desencolar.
    El primero en ser encolado es tambien el primero en ser desencolado.
    '''

    def __init__(self):
        '''Crea una cola vacia.'''
        self.items = []

    def encolar(self, x):
        '''Encola el elemento x.'''
        self.items.append(x)

    def desencolar(self):
        '''Elimina el primer elemento de la cola 
        y devuelve su valor. 
        Si la cola esta vacia, levanta ValueError.'''
        if self.esta_vacia():
            raise ValueError('La cola esta vacia')
        return self.items.pop(0)

    def esta_vacia(self):
        '''Devuelve 
        True si la cola esta vacia, 
        False si no.'''
        return len(self.items) == 0


#%%
class TorreDeControl:
    def __init__(self):
        self.arribos = Cola()
        self.partidas = Cola()
    
    def nuevo_arribo(self, vuelo):
        self.arribos.encolar(vuelo)
    
    def nueva_partida(self, vuelo):
        self.partidas.encolar(vuelo)
      
    def asignar_pista(self):
        if self.arribos.esta_vacia(): #si no hay arribos
            if self.partidas.esta_vacia(): #si no hay partidas
                raise ValueError('La cola esta vacia')
            else:
                a = self.partidas.desencolar() #si no hay arribos pero sí partidas, despegue
                s = f'El vuelo {a} despegó con éxito.'
        else: #si hay arribos
            a = self.arribos.desencolar() #aterrizaje   
            s = f'El vuelo {a} aterrizó con éxito.'
        return print(s) 
    
    def ver_estado(self):
        if self.arribos.esta_vacia():
            estado_arrib = 'No hay aviones para aterrizar.'
        else:
            estado_arrib = f'Vuelos esperando para aterrizar: {self.arribos.items}.'
       
        if self.partidas.esta_vacia():
            estado_part = 'No hay aviones para despegar.'
        else:
            estado_part = f'Vuelos esperando para despegar {self.partidas.items}.'
        return print(estado_arrib + '\n' + estado_part)


#%%
        
torre = TorreDeControl()
torre.nuevo_arribo('AR156')
torre.nueva_partida('KLM1267')
torre.nuevo_arribo('AR32')
torre.ver_estado()
#torre.asignar_pista()


