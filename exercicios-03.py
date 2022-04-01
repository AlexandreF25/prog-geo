# LEITURA DE VALORES
Xgreen = float(input("Digite o valor para o Xgreen: "))
Xnir = float(input("Digite o valor para o Xnir: "))
Xred = float(input("Digite o valor para o Xred: "))
# FÓRMULAS
ndwi = (Xgreen - Xnir) / (Xgreen + Xnir)
ndvi = (Xnir - Xred) / (Xnir + Xred)
#RESULTADO
print("NDWI:", ndwi, "\nNDVI:", ndvi)