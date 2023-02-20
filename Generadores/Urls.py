#La funcion crea los links que se usarna para el respectivo web scraping
# retorna un matriz en donde cada lista es tiene 4 campos Url,Departure,Arrive,fecha
def Urls_viva(fechas,legs):
    Links=[]
    for leg in legs:
        for fecha in fechas:
            Url="https://reservas.vivaair.com/co/es/booking/resultados?DepartureCity={}&ArrivalCity={}&DepartureDate={}&Adults=1&Currency=COP".format(leg[0],leg[1],fecha)
            Links.append([Url,leg[0],leg[1],fecha])
    return Links

def Urls_Latam(fechas,legs):
    Links=[]
    for leg in legs:
        for fecha in fechas:
            Url="https://www.latamairlines.com/co/es/ofertas-vuelos?origin={}&inbound=null&outbound={}T17%3A00%3A00.000Z&destination={}&adt=1&chd=0&inf=0&trip=OW&cabin=Economy&redemption=false&sort=RECOMMENDED".format(leg[0],fecha,leg[1])
            Links.append([Url,leg[0],leg[1],fecha])
    return Links

def Urls_wingo(fechas,legs):
    Links=[]
    for leg in legs:
        for fecha in fechas:
            Url="https://booking.wingo.com/es/search/{}/{}/{}/1/0/0/1/COP/0/0".format(leg[0],leg[1],fecha)
            Links.append([Url,leg[0],leg[1],fecha])
    return Links


