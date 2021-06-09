# -*- coding: utf-8 -*-

def vida(fecha):
    from datetime import datetime
    from datetime import timedelta
    fecha_nacimiento = datetime.strptime(fecha, '%d/%B/%Y') #convierto str en fecha
    ahora = datetime.now()
    s_vividos = timedelta.total_seconds(ahora - fecha_nacimiento) #resto la fecha actual con la de nacimiento
                                                                    # y convierto a segundos
    return s_vividos


f = '24/May/1990'
print(f'{int(vida(f))} segundos vividos.')


