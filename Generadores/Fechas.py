from datetime import datetime
from datetime import timedelta
'''
    Genera las fechas en formato año-mes-dia retorna una lista de fechas de la fecha actual 
    hasta la fecha actual + Days
    ejemplo:
        Fecha
'''
def Fecha(Days):
    Date_now=datetime.now()
    Fechas=[Date_now+timedelta(days=i) for i in range(0,Days)]
    Fechas=[dia.strftime('%Y-%m-%d') for dia in Fechas]
    return Fechas
    
#print(Fecha(3))