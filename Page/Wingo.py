from selenium import webdriver
import pandas as pd
import time
import itertools

def Scraping_Wingo(Urls):
    """
    This function scrapes flight data from a list of URLs and returns a pandas dataframe with the
    extracted information.
    
    :param Urls: Urls is a list of lists containing the URLs of the websites to scrape, along with the
    departure and arrival locations and the date of the flight. Each inner list contains four elements:
    the website URL, the departure location, the arrival location, and the date of the flight
    :return: a pandas DataFrame with flight information scraped from the provided URLs.
    """
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
            option.add_experimental_option('excludeSwitches', ['enable-logging'])
            driver = webdriver.Chrome("C:/Scraping/chromedriver.exe", chrome_options=option)
            driver.get(website)
            time.sleep(5)

            #Extra lo elementos del HTML todos los que coincidan
            Vuelo=driver.find_elements("xpath",'//span[@Class="label-info-card font-gray-medium-letter font-weight-bold radio-custom-label"]')
            Hora=driver.find_elements("xpath",'//p[@Class="font-gray font-weight-bold"]')
            Tipo=driver.find_elements("xpath",'//p[@Class="m-0 type-info-flight"]')
            Price=driver.find_elements("xpath",'//p[@Class="font-yellow font-weight-bold mt-2"]')
            Tarifa=driver.find_elements("xpath",'//span[@Class="font-weight-bold"]')

            #extraemos los datos de sus tags de html y los convertimos en un lista
            all_Fechas=list(itertools.repeat(fecha, len(Price)))
            all_Departure=list(itertools.repeat(Departure, len(Price)))
            all_Arrive=list(itertools.repeat(Arrive, len(Price)))
            all_Vuelo=[vuelo.get_attribute('innerText') for vuelo in Vuelo]
            all_Hora=[hora.get_attribute('innerText') for hora in Hora]
            all_Tipo=[T.get_attribute('innerText') for T in Tipo]
            all_Prices=[price.get_attribute('innerText') for price in Price]
            all_Tarifa=[tarifa.get_attribute('innerText') for tarifa in Tarifa]

            Hora_Salida=[all_Hora[x] for x in range(0,len(all_Hora)) if x % 2 == 0]
            Hora_Llegada=[all_Hora[x] for x in range(0,len(all_Hora)) if x % 2 != 0]
            Tipos=[all_Tipo[x].split()[0] for x in range(0,len(all_Tipo)) if x % 2==0]

            #se crea un dataframe
            Datos = {
                'Fecha':all_Fechas,
                'Departure' : all_Departure,
                'Arrive': all_Arrive,
                'Hora_Salida':Hora_Salida,
                'Hora_LLegada':Hora_Llegada,
                'Vuelos':all_Vuelo,
                'Tarifa':all_Tarifa,
                'Price':all_Prices,
                'Tipo':Tipos
            }
            df = pd.DataFrame(Datos)
            print(df)
            #se almacenan los datos de todas las Urls consultadas
            Datos_completos=pd.concat([Datos_completos, df], ignore_index=True)
        except Exception as e:
            print(e)
    return Datos_completos