'''
Genera los trayectos posibles entre Ciudades
'''

def rutas():
    ciudades = ['BOG','CLO']#,'CUC','CTG','ADZ','SMR']
    legs=[]
    for i in ciudades:
        for j in ciudades:
            if i != j:
                legs.append((i,j))
    return legs
"""
def rutas():
    Matriz_rutas=[ ['BOG','MEX'],
    ['BOG','LIM'],
    ['BOG','UIO'],
    ['BOG','CUN'],
    ['BOG','GYE'],
    ['BOG','CCS'],
    ['BOG','SJO'],
    ['BOG','PUJ'],
    ['AUA','BOG'],
    ['BOG','HAV'],
    ['BOG','SDQ'],
    ['BOG','CUR'],
    ['BLB','BOG'],
    ['BOG','SJU']
    ]
    for i in range(0,len(Matriz_rutas)):
        Matriz_rutas.append([Matriz_rutas[i][1],Matriz_rutas[i][0]])
    return Matriz_rutas"""



