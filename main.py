import stats_data as sd

lista = []
while True:
    numeros = input("Introduce numeros: ")
    if numeros == "fin":
        break
    numeros = float(numeros)
    lista.append(numeros)
calculo_stats = sd.StatsData(lista)

print("Lista de numeros: ", calculo_stats.l_data)
print("Media: ", calculo_stats.mean)
print("Mediana: ", calculo_stats.median)
print("Varianza: ", calculo_stats.varance)
