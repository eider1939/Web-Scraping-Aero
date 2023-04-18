from selenium import webdriver
import pandas as pd
import time
import itertools

def Scraping_Latam(Urls):
    Datos_completos= pd.DataFrame()
    for iterador in Urls: #iterador es una lista
        try:
            website=iterador[0]
            Departure=iterador[1]
            Arrive=iterador[2]
            fecha=iterador[3]
            option = webdriver.ChromeOptions()
            option.add_argument("--incognito")
            #option.add_argument("--headless")
            #we create the driver specifying the origin of chrome browser
            #option.add_experimental_option('excludeSwitches', ['enable-logging'])
            driver = webdriver.Chrome("C:/Scraping/chromedriver.exe", chrome_options=option)
            driver.get(website)
            time.sleep(6)
            #Extra lo elementos del HTML todos los que coincidan
            Price=driver.find_elements("xpath",'//span[@Class="display-currencystyle__CurrencyAmount-sc__sc-19mlo29-2 fMjBKP"]')
            Hora=driver.find_elements("xpath",'//span[@Class="card-flightstyle__TextHourFlight-sc__sc-16r5pdw-18 kKmcWo"]')
            Tipo=driver.find_elements("xpath",'//div[@Class="card-flightstyle__ContainerFooterCard-sc__sc-16r5pdw-24 iMBDQD"]//a//span')
            #extraemos los datos de sus tags de html y los convertimos ne un lista
            all_Fechas=list(itertools.repeat(fecha, len(Tipo)))
            all_Departure=list(itertools.repeat(Departure, len(Tipo)))
            all_Arrive=list(itertools.repeat(Arrive, len(Tipo)))
            all_Prices=[price.get_attribute('innerText') for price in Price]
            all_Hora=[hora.get_attribute('innerText') for hora in Hora]
            all_Tipo=[T.get_attribute('innerText') for T in Tipo]

            #Separar las horas de Salida y LLegada
            Hora_Salida=[all_Hora[x] for x in range(0,len(all_Hora)) if x % 2 == 0]
            Hora_Llegada=[all_Hora[x] for x in range(0,len(all_Hora)) if x % 2 != 0]
            #Separar Precios
            Prices=[all_Prices[x] for x in range(0,len(all_Prices)) if x % 2 == 0]

            #se crea el dataframe con los datos
            Datos = {
                'Fecha':all_Fechas,
                'Departure' : all_Departure,
                'Arrive': all_Arrive,
                'Hora_Salida':Hora_Salida,
                'Hora_LLegada':Hora_Llegada,
                'Price':Prices,
                'Tipo':all_Tipo
            }
            df = pd.DataFrame(Datos)
            print(df)
            #se almacenas todos los datos de la urls consultadas
            Datos_completos=pd.concat([Datos_completos, df], ignore_index=True)
        except Exception as e:
        # ... PRINT THE ERROR MESSAGE ... #
            print(e)
    return Datos_completos