#BIBLIOTECA
from math import asin, cos, pi, radians, sin, sqrt
#CONSTANTES
# BELÉM
lat1 = -01.46080834 #-1.4558
lon1 = -48.44140705 #-48.5038
# SÃO JOSÉ DOS CAMPOS
lat2 = -23.20713242 #-23.1849
lon2 = -45.86173778 #-45.8708
# RAIO MÉDIO DA TERRA
R = 6371
#CONVERSÃO PARA RADIANOS
# PELA FUNÇÃO
lat1 = radians(lat1)
lat2 = radians(lat2)
lon1 = radians(lon1)
lon2 = radians(lon2)
# POR FÓRMULA
# lat1 = lat1 * pi / 180
# lat2 = lat2 * pi / 180
# lon1 = lon1 * pi / 180
# lon2 = lon2 * pi / 180
#DELTA
dLat = lat2 - lat1
dLon = lon2 - lon1
#FÓRMULA DE HAVERSINE
A = pow(sin(dLat/2), 2)
B = cos(lat1) * cos(lat2)
C = pow(sin(dLon/2), 2)
D = sqrt(A + B * C)
E = 2 * R * asin(D)
print(E)