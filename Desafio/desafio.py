import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import statistics


#Dados
dados = pd.read_csv('Desafio/dados.csv')
dados1 = pd.DataFrame(dados)

compra = dados1['Compra']

#Limpiza de Dados
sudeste = dados1[dados1['Região'] == 'Sudeste']
nordeste = dados1[dados1['Região'] == 'Nordeste']
norte = dados1[dados1['Região'] == 'Norte']
sul = dados1[dados1['Região'] == 'Sul']
centro_oeste = dados1[dados1['Região'] == 'Centro-Oeste']


sudeste_soma = sum(sudeste['Compra'])
nordeste_soma = sum(nordeste['Compra'])
norte_soma = sum(norte['Compra'])
sul_soma = sum(sul['Compra'])
centro_oeste_soma = sum(centro_oeste['Compra'])

lista_regiao = ['Sudeste', 'Nordeste', 'Norte', 'Sul', 'Centro-Oeste']
lista_soma_regiao = []
lista_soma_regiao.append(sudeste_soma)
lista_soma_regiao.append(nordeste_soma)
lista_soma_regiao.append(norte_soma)
lista_soma_regiao.append(sul_soma)
lista_soma_regiao.append(centro_oeste_soma)

medicao = ['Moda', 'Media', 'Mediana', 'Desvio', 'Maximo', 'Minimo']
estatistica_sudeste = []
estatistica_nordeste = []
estatistica_norte = []
estatistica_sul = []
estatistica_centro_oeste = []



moda = statistics.mode(sudeste['Compra'])
estatistica_sudeste.append(moda)
media = statistics.mean(sudeste['Compra'])
estatistica_sudeste.append(media)
mediana = statistics.median(sudeste['Compra'])
estatistica_sudeste.append(mediana)
desvio = statistics.stdev(sudeste['Compra'])
estatistica_sudeste.append(desvio)
maximo = max(sudeste['Compra'])
estatistica_sudeste.append(maximo)
minimo = min(sudeste['Compra'])
estatistica_sudeste.append(minimo)

moda = statistics.mode(nordeste['Compra'])
estatistica_nordeste.append(moda)
media = statistics.mean(nordeste['Compra'])
estatistica_nordeste.append(media)
mediana = statistics.median(nordeste['Compra'])
estatistica_nordeste.append(mediana)
# desvio = statistics.stdev(nordeste['Compra'])
estatistica_nordeste.append(0)
maximo = max(nordeste['Compra'])
estatistica_nordeste.append(maximo)
minimo = min(nordeste['Compra'])
estatistica_nordeste.append(minimo)

moda = statistics.mode(norte['Compra'])
estatistica_norte.append(moda)
media = statistics.mean(norte['Compra'])
estatistica_norte.append(media)
mediana = statistics.median(norte['Compra'])
estatistica_norte.append(mediana)
# desvio = statistics.stdev(norte['Compra'])
estatistica_norte.append(0)
maximo = max(norte['Compra'])
estatistica_norte.append(maximo)
minimo = min(norte['Compra'])
estatistica_norte.append(minimo)

moda = statistics.mode(sul['Compra'])
estatistica_sul.append(moda)
media = statistics.mean(sul['Compra'])
estatistica_sul.append(media)
mediana = statistics.median(sul['Compra'])
estatistica_sul.append(mediana)
desvio = statistics.stdev(sul['Compra'])
estatistica_sul.append(desvio)
maximo = max(sul['Compra'])
estatistica_sul.append(maximo)
minimo = min(sul['Compra'])
estatistica_sul.append(minimo)

moda = statistics.mode(centro_oeste['Compra'])
estatistica_centro_oeste.append(moda)
media = statistics.mean(centro_oeste['Compra'])
estatistica_centro_oeste.append(media)
mediana = statistics.median(centro_oeste['Compra'])
estatistica_centro_oeste.append(mediana)
# desvio = statistics.stdev(centro_oeste['Compra'])
estatistica_centro_oeste.append(0)
maximo = max(centro_oeste['Compra'])
estatistica_centro_oeste.append(maximo)
minimo = min(centro_oeste['Compra'])
estatistica_centro_oeste.append(minimo)









#Parte de Grafico
def regiao():
    plt.subplot(1,2,1)
    plt.title('Região por Vendas')
    plt.bar(lista_regiao, lista_soma_regiao, color='red')
    plt.subplot(1,2,2)
    plt.title('Região Sudeste')
    plt.bar(medicao, estatistica_sudeste, color='black')
    plt.show()
def regiao2():
    plt.subplot(1,2,1)
    plt.title('Região Nordeste')
    plt.bar(medicao, estatistica_nordeste, color='green')
    plt.subplot(1,2,2)
    plt.title('Região Norte')
    plt.bar(medicao, estatistica_norte, color='red')
    plt.show()
def regiao3():
    plt.subplot(1,2,1)
    plt.title('Região Sul')
    plt.bar(medicao, estatistica_sul, color='pink')
    plt.subplot(1,2,2)
    plt.title('Região Centro-Oeste')
    plt.bar(medicao, estatistica_centro_oeste, color='white')
    plt.show()

regiao()
regiao2()
regiao3()

