#La funcion crea los links que se usarna para el respectivo web scraping
# retorna un matriz en donde cada lista es tiene 4 campos Url,Departure,Arrive,fecha



"""
    The functions "Urls_wingo, Urls_Latam and Urls_viva" generates a list of URLs for flight searches on the website based on
    given dates and legs.
    
    :param fechas: a list of dates in the format "YYYY-MM-DD" for which flight search links will be
    generated
    :param legs: a list of tuples, where each tuple represents a flight leg with two elements: the
    departure airport code and the arrival airport code
    :return: The functions returns a list of lists, where each inner list contains a URL,
    the origin airport code, the destination airport code, and a date.
"""

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


