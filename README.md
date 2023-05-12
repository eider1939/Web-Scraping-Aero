# Web-Scraping-Aero

App de Scraping de aero proyecto con fines academicos 

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

Los datos estraidos generan los sigueintes dataframes
![](https://github.com/eider1939/Web-Scraping-Aero/blob/main/img/Datos.JPG)

## Depuracion

al tener los informes el archivo join.csv se debe modificar para concat los informes luego se les debe hacer una depuracion la cual se hace en los archivos Limpieza y Depuracion .ipynb 

De las variables extraidas se crean unas nuevas variables 
#### Creacion de las nuevas variables
derivadas de las variables principales

- Fechas: Se deriva como 
Departure_Day: dia del vuelo.
Departure_Month: mes del vuelo.
Departure_Year: año del vuelo.
Weekday: dia de la semana en numero.
Holidays: variable booleana que indica si es una fecha festiva o no.
- Hora_Salida: se deriva
Departure_time: horario del dia en que sale mañana, tarde, noche.
- DepartureDate y Fecha: su difenrecia crea la variable 
Consultation_period: es la cantidad de dias que faltan para el vuelo.

Al final quedan los datos limpios los cuales pueden ser utilizados par aun analisis mayor.

### INFO
![](https://github.com/eider1939/Web-Scraping-Aero/blob/main/img/info_data.JPG)

### DATAFRAME
![](https://github.com/eider1939/Web-Scraping-Aero/blob/main/img/Dataframe.jpg)


### Nota

en el archivo librerias.ipynb tiene ejemplo unitarias de como funciona el scraping


