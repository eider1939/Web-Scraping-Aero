'''
Genera los trayectos posibles entre Ciudades

['BOG','CLO']--Eider
['BOG','MDE']--andres
['BOG','ADZ']---miguel
['MDE,'SMR']---raul


'''

def rutas():
    """
    The function "rutas" generates all possible legs between a list of cities.
    :return: The function `rutas()` returns a list of tuples representing all possible legs between the
    cities in the `ciudades` list.
    """
<<<<<<< Updated upstream
    ciudades = ['MDE','SMR'] #['BOG','CLO']#['BOG','MDE']#['BOG','ADZ']
=======
    ciudades = ['BOG','MDE']#['BOG','MDE']#['BOG','ADZ']#['MDE,'SMR']
>>>>>>> Stashed changes
    legs=[]
    for i in ciudades:
        for j in ciudades:
            if i != j:
                legs.append((i,j))
    return legs





