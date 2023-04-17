import Generadores.Fechas as Fechas
import Generadores.Rutas as Rutas
import Generadores.Urls as Urls
import Latam as Latam
import Wingo as Wingo
import time
from datetime import datetime
import numpy as np
import pandas as pd

"""
    App de Scraping de aerolineas proyecto con fines academicos 
"""

if __name__ == "__main__":
    start_time=time.time()
    Fecha_hoy=datetime.now().strftime('%Y-%m-%d')
    fechas=Fechas.Fecha(3)    #genera las fechas
    rutas= Rutas.rutas()
    
    ###  Latam
    urls_latam=Urls.Urls_Latam(fechas,rutas)
    Datos_Latam=Latam.Scraping_Latam(urls_latam)
    Datos_Latam.to_csv("Informes/Scraping_Latam_{}.csv".format(Fecha_hoy),index=False)

    ### Wingo
    #urls_wingo=Urls.Urls_wingo(fechas,rutas)
    #Datos_Wingo=Wingo.Scraping_Wingo(urls_wingo)
    #Datos_Wingo.to_csv("Informes/Scraping_Wingo_{}.csv".format(Fecha_hoy),index=False)
    print('tiempo de ejecucion ',time.time() - start_time)
