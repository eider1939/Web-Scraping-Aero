import Generadores.Fechas as Fechas
import Generadores.Rutas as Rutas
import Generadores.Urls as Urls
import Page.Latam as Latam
import Page.Wingo as Wingo
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
    fechas=Fechas.Fecha(60)    #genera las fechas
    rutas= Rutas.rutas()
    Departure='MED'  #deben cambiarlo por las rutas que se les asigno no importa el orden
    arrive='SMR'     #solo es para el nombre del archivo
    
    ###  Latam
    urls_latam=Urls.Urls_Latam(fechas,rutas)
    Datos_Latam=Latam.Scraping_Latam(urls_latam)
    Datos_Latam['CaptureDate']=datetime.now().strftime('%Y-%m-%d')
    Datos_Latam['Aerolinea']='Latam'
    Datos_Latam.to_csv("Informes/Scraping_Latam_{}-{}_{}.csv".format(Departure,arrive,Fecha_hoy),index=False)

    ### Wingo
    #urls_wingo=Urls.Urls_wingo(fechas,rutas)
    #Datos_Wingo=Wingo.Scraping_Wingo(urls_wingo)
    #Datos_Wingo['CaptureDate']=datetime.now().strftime('%Y-%m-%d')
    #Datos_Wingo.to_csv("Informes/Scraping_Wingo_{}-{}_{}.csv".format(Departure,arrive,Fecha_hoy),index=False)
    #Datos_Wingo['Aerolinea']='Wingo'
    #print('tiempo de ejecucion ',time.time() - start_time)
