# Web-Scraping-Aero

"""
    App de Scraping de aero proyecto con fines academicos 

"""


## el Archivo App.py 
- Ejecuta todo el programa, lo primero que hace es llamar a los archivos en la carpeta generadores
estos de encargan generar las fechas las rutas y los links.

- los archivos Latam.py, Viva.py y Wingo.py contienen funciones las cuales se encargan de realizar es scraping a cada una de las paginas, generando un Dataframe con la informacion extraida

- al final cada Dataframe es gurdado en un arcvhio .csv en la carpeta Informes

### Generadores

esta carpeta contiene lo necesario para generar el link al que se le va hacer el web scraping

### Informes

Esta carpeta funciona como el almacenamineto de las respectivas consultas almacena archivos .csv con los datos recopilados

### Page
Esta pagina tiene la porte logica la cual a traves de selenium ingresa al url de la pagina y retorna los datos, luego almacena los datos en dataframe para al final retornarlo.

Los datos estraidos genran los sigueintes dataframes
![](https://github.com/rgaitanv/Trabajo1_Grupo9_Optimizacion_Heuristica/blob/main/Imagenes/info_del_recorrido.PNG)

## Depuracion

al tener los informes el archivo join.csv se debe modificar para concat los informes luego se les debe hacer una depuracion la cual se hace en los archivos Limpieza y Depuracion .ipynb 

Al final quedan los datos limpios los cuales pueden ser utilizados par aun analisis mayor.

### INFO
![](https://github.com/rgaitanv/Trabajo1_Grupo9_Optimizacion_Heuristica/blob/main/Imagenes/info_del_recorrido.PNG)

### DATAFRAME
![](https://github.com/rgaitanv/Trabajo1_Grupo9_Optimizacion_Heuristica/blob/main/Imagenes/info_del_recorrido.PNG)



