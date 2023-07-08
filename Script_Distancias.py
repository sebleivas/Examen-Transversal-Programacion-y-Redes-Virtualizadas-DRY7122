from geopy.geocoders import Nominatim
from geopy import distance

# Función para calcular la duración del viaje
def calcular_duracion(distancia):
    velocidad_promedio = 80  # km/h (puedes ajustar esta velocidad según tus necesidades)
    duracion_horas = distancia / velocidad_promedio
    duracion_minutos = duracion_horas * 60
    duracion_segundos = duracion_minutos * 60
    return duracion_horas, duracion_minutos, duracion_segundos

# Función para calcular el combustible requerido
def calcular_combustible(distancia):
    consumo_promedio = 10  # km/l (puedes ajustar este consumo según tus necesidades)
    combustible_litros = distancia / consumo_promedio
    return combustible_litros

# Obtener las ciudades de origen y destino
ciudad_origen = input("Ciudad de Origen: ")
ciudad_destino = input("Ciudad de Destino: ")

# Obtener las coordenadas geográficas de las ciudades
geolocator = Nominatim(user_agent="myGeocoder")
location_origen = geolocator.geocode(ciudad_origen + ", Chile")
location_destino = geolocator.geocode(ciudad_destino + ", Latin America")

# Verificar si se obtuvieron las coordenadas de las ciudades correctamente
if not location_origen or not location_destino:
    print("No se pudieron obtener las coordenadas geográficas de una o ambas ciudades.")
    exit()

# Calcular la distancia entre las ciudades
coord_origen = (location_origen.latitude, location_origen.longitude)
coord_destino = (location_destino.latitude, location_destino.longitude)
distancia_km = distance.distance(coord_origen, coord_destino).km

# Calcular la duración del viaje
duracion_horas, duracion_minutos, duracion_segundos = calcular_duracion(distancia_km)

# Calcular el combustible requerido
combustible_litros = calcular_combustible(distancia_km)

# Imprimir resultados
print("Duración del viaje: {} horas, {} minutos, {} segundos".format(
    round(duracion_horas, 1), round(duracion_minutos, 1), round(duracion_segundos, 1)))
print("Combustible requerido: {} litros".format(round(combustible_litros, 1)))
print("S")

# Imprimir la narrativa del viaje
print("Viaje desde {} hasta {}. Distancia: {} km".format(ciudad_origen, ciudad_destino, round(distancia_km, 1)))