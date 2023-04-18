from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
import pandas as pd
import time
from datetime import datetime
from datetime import timedelta
import itertools
import numpy as np

def Scraping_Viva(Urls):
    Datos_completos= pd.DataFrame()
    for iterador in Urls: #iterador es una lista
        try:
            website=iterador[0]
            Departure=iterador[1]
            Arrive=iterador[2]
            fecha=iterador[3]
            option = webdriver.ChromeOptions()
            option.add_argument("--incognito")
            option.add_argument("--headless")
            #we create the driver specifying the origin of chrome browser
            driver = webdriver.Chrome("C:/Scraping/chromedriver.exe", chrome_options=option)
            driver.get(website)
            time.sleep(3)
            #Extra lo elementos del HTML todos los que coincidan
            Price=driver.find_elements("xpath",'//span[@class = "lowest-fare__price"]')
            Hora=driver.find_elements("xpath",'//div[@class = "time d-flex flex-row align-items-baseline"]/h3')
            Am_pm=driver.find_elements("xpath",'//div[@class = "time d-flex flex-row align-items-baseline"]/span')
            Info_Vuelo=driver.find_elements("xpath",'//div[@class = "detail--flight-segment d-flex flex-column justify-content-center"]/h5')
            Tipo=driver.find_elements("xpath",'//div[@class = "details__type-and-stops-wrapper d-flex align-items-start justify-content-between"]/h5')

            #extraemos los datos de sus tags de html y los convertimos ne un lista
            Tamaño_df=min(len(Price),len(Hora),len(Tipo))
            all_Fechas=list(itertools.repeat(fecha, len(Price)))
            all_Departure=list(itertools.repeat(Departure, len(Price)))
            all_Arrive=list(itertools.repeat(Arrive, len(Price)))
            all_Hora=[hora.get_attribute('innerText') for hora in Hora]
            all_Am_pm=[periodo.get_attribute('innerText') for periodo in Am_pm]
            all_Info_vuelo=[info.get_attribute('innerText') for info in Info_Vuelo]
            all_Tipo=[T.get_attribute('innerText') for T in Tipo]
            all_Prices=[price.get_attribute('innerText') for price in Price]

            #Separar las horas de Salida y LLegada
            all_Hora_Salida=[all_Hora[x] for x in range(0,len(all_Hora)) if x % 2 == 0]
            all_Hora_Llegada=[all_Hora[x] for x in range(0,len(all_Hora)) if x % 2 != 0]
            #Separar los AM y PM
            all_Salida=[all_Am_pm[x] for x in range(0,len(all_Am_pm)) if x % 2 == 0]
            all_Llegada=[all_Am_pm[x] for x in range(0,len(all_Am_pm)) if x % 2 != 0]
            #Unir Horas con los Periodo am Y pm
            Hora_Salida=[]
            Hora_Llegada=[]
            for i in range(0,len(all_Hora_Llegada)): #ciclo recorre las listas con hora y perido
                H_S=all_Hora_Salida[i]+" "+all_Salida[i]  # los concatena para luego converirlo en tipo hora
                H_L=all_Hora_Llegada[i]+" "+all_Llegada[i] # y agregarlos a a las listas Hora tando salida como llegada
                Hora_Salida.append(H_S)
                Hora_Llegada.append(H_L)

            #Separar los ID de vuelo de las tarifas
            all_Aviones=[all_Info_vuelo[x] for x in range(0,len(all_Info_vuelo)) if x % 2 == 0]
            all_Tarifa=[all_Info_vuelo[x] for x in range(0,len(all_Info_vuelo)) if x % 2 != 0]

            Datos = {
                'Fecha':all_Fechas,
                'Departure' : all_Departure,
                'Arrive': all_Arrive,
                'Hora_Salida':Hora_Salida,
                'Hora_LLegada':Hora_Llegada,
                'Vuelos':all_Aviones,
                'Tarifa':all_Tarifa,
                'Price':all_Prices,
                'Tipo':all_Tipo
            }
            df = pd.DataFrame(Datos)
            #print(df)
            Datos_completos=pd.concat([Datos_completos, df], ignore_index=True)
            #print(fecha," ",Departure," : ",Arrive)
        except Exception as e:
            print(e)
    return Datos_completos