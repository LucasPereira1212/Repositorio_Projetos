#IGNORAR, CODIGO NÃO DEU CERTO

def lista(moda_empresa, media_empresa, desvio_padrao_empresa, mediana_empresa, amplitude_empresa, variancia_empresa):

    moda = []
    desvio = []
    media = []
    mediana = []
    amplitude = []
    variancia = []

#adicionar a tabela

    moda.append(moda_empresa)
    desvio.append(desvio_padrao_empresa)
    media.append(media_empresa)
    mediana.append(mediana_empresa)
    amplitude.append(amplitude_empresa)
    variancia.append(variancia_empresa)

#maior resultado

    maior_moda = max(moda)
    maior_desvio = max(desvio)
    maior_media = max(media)
    maior_mediana = max(mediana)
    maior_amplitude = max(amplitude)
    maior_variancia = max(variancia)



#index de cada valor

    index_maior_moda = moda.index(maior_moda)

    if index_maior_moda == 0:
        empresa_maior_moda = 'empresa1'
        return empresa_maior_moda

    elif index_maior_moda == 1:
        empresa_maior_moda = 'empresa2'
        return empresa_maior_moda
    
    elif index_maior_moda == 2:
        empresa_maior_moda = 'empresa3'
        return empresa_maior_moda
    
    elif index_maior_moda == 3:
        empresa_maior_moda = 'empresa4'
        return empresa_maior_moda
    
    elif index_maior_moda == 4:
        empresa_maior_moda = 'empresa5'
        return empresa_maior_moda

    index_maior_desvio = desvio.index(maior_desvio)

    if index_maior_desvio == 0:
        empresa_maior_desvio = 'empresa1'
        return empresa_maior_desvio
    
    elif index_maior_desvio == 1:
        empresa_maior_desvio = 'empresa2'
        return empresa_maior_desvio
    
    elif index_maior_desvio == 2:
        empresa_maior_desvio = 'empresa3'
        return empresa_maior_desvio
    
    elif index_maior_desvio == 3:
        empresa_maior_desvio = 'empresa4'
        return empresa_maior_desvio
    
    elif index_maior_desvio == 4:
        empresa_maior_desvio = 'empresa5'
        return empresa_maior_desvio

    index_maior_media = media.index(maior_media)

    if index_maior_media == 0:
        empresa_maior_media = 'empresa1'
        return empresa_maior_media
    
    elif index_maior_media == 1:
        empresa_maior_media = 'empresa2'
        return empresa_maior_media
    
    elif index_maior_media == 2:
        empresa_maior_media = 'empresa3'
        return empresa_maior_media
    
    elif index_maior_media == 3:
        empresa_maior_media = 'empresa4'
        return empresa_maior_media
    
    elif index_maior_media == 4:
        empresa_maior_media = 'empresa5'
        return empresa_maior_media


    index_maior_mediana = mediana.index(maior_mediana)

    if index_maior_mediana == 0:
        empresa_maior_mediana = 'empresa1'
        return empresa_maior_mediana
    
    elif index_maior_mediana == 1:
        empresa_maior_mediana = 'empresa2'
        return empresa_maior_mediana
    
    elif index_maior_mediana == 2:
        empresa_maior_mediana = 'empresa3'
        return empresa_maior_mediana
    
    elif index_maior_mediana == 3:
        empresa_maior_mediana = 'empresa4'
        return empresa_maior_mediana
    
    elif index_maior_mediana == 4:
        empresa_maior_mediana = 'empresa5'
        return empresa_maior_mediana


    index_maior_amplitude = amplitude.index(maior_amplitude)

    if index_maior_amplitude == 0:
        empresa_maior_amplitude = 'empresa1'
        return empresa_maior_amplitude
    
    elif index_maior_amplitude == 1:
        empresa_maior_amplitude = 'empresa2'
        return empresa_maior_amplitude
    
    elif index_maior_amplitude == 2:
        empresa_maior_amplitude = 'empresa3'
        return empresa_maior_amplitude
    
    elif index_maior_amplitude == 3:
        empresa_maior_amplitude= 'empresa4'
        return empresa_maior_amplitude
    
    elif index_maior_amplitude == 4:
        empresa_maior_amplitude = 'empresa5'
        return empresa_maior_amplitude

    
    index_maior_variancia = variancia.index(maior_variancia)

    if index_maior_variancia == 0:
        empresa_maior_variancia = 'empresa1'
        return empresa_maior_amplitude
    
    elif index_maior_variancia == 1:
        empresa_maior_variancia = 'empresa2'
        return empresa_maior_amplitude
    
    elif index_maior_variancia == 2:
        empresa_maior_variancia = 'empresa3'
        return empresa_maior_amplitude
    
    elif index_maior_variancia == 3:
        empresa_maior_variancia = 'empresa4'
        return empresa_maior_amplitude
    
    elif index_maior_variancia == 4:
        empresa_maior_variancia = 'empresa5'
        return empresa_maior_amplitude




#menor resultado

    menor_moda = min(moda)
    menor_desvio = min(desvio)
    menor_media = min(media)
    menor_mediana = min(mediana)
    menor_amplitude = min(amplitude)
    menor_variancia = min(variancia)



#index de cada valor

    index_menor_moda = moda.index(menor_moda)

    if index_menor_moda == 0:
        empresa_menor_moda = 'empresa1'
        return empresa_menor_moda
    
    elif index_menor_moda == 1:
        empresa_menor_moda = 'empresa2'
        return empresa_menor_moda
    
    elif index_menor_moda == 2:
        empresa_menor_moda = 'empresa3'
        return empresa_menor_moda
    
    elif index_menor_moda == 3:
        empresa_menor_moda = 'empresa4'
        return empresa_menor_moda
    
    elif index_menor_moda == 4:
        empresa_menor_moda = 'empresa5'
        return empresa_menor_moda

    index_menor_desvio = desvio.index(menor_desvio)

    if index_menor_desvio == 0:
        empresa_menor_desvio = 'empresa1'
        return empresa_menor_desvio
    
    elif index_menor_desvio == 1:
        empresa_menor_desvio = 'empresa2'
        return empresa_menor_desvio
    
    elif index_menor_desvio == 2:
        empresa_menor_desvio = 'empresa3'
        return empresa_menor_desvio
    
    elif index_menor_desvio == 3:
        empresa_menor_desvio = 'empresa4'
        return empresa_menor_desvio
    
    elif index_menor_desvio == 4:
        empresa_menor_desvio = 'empresa5'
        return empresa_menor_desvio

    index_menor_media = media.index(menor_media)

    if index_menor_media == 0:
        empresa_menor_media = 'empresa1'
        return empresa_menor_media
    
    elif index_menor_media == 1:
        empresa_menor_media = 'empresa2'
        return empresa_menor_media
    
    elif index_menor_media == 2:
        empresa_menor_media = 'empresa3'
        return empresa_menor_media
    
    elif index_menor_media == 3:
        empresa_menor_media = 'empresa4'
        return empresa_menor_media
    
    elif index_menor_media == 4:
        empresa_menor_media= 'empresa5'
        return empresa_menor_media

    index_menor_mediana = mediana.index(menor_mediana)

    if index_menor_mediana == 0:
        empresa_menor_mediana = 'empresa1'
        return empresa_menor_mediana
    
    elif index_menor_mediana == 1:
        empresa_menor_mediana = 'empresa2'
        return empresa_menor_mediana
    
    elif index_menor_mediana == 2:
        empresa_menor_mediana = 'empresa3'
        return empresa_menor_mediana
    
    elif index_menor_mediana == 3:
        empresa_menor_mediana = 'empresa4'
        return empresa_menor_mediana
    
    elif index_menor_mediana == 4:
        empresa_menor_mediana = 'empresa5'
        return empresa_menor_mediana

    index_menor_amplitude = amplitude.index(menor_amplitude)

    if index_menor_amplitude == 0:
        empresa_menor_amplitude = 'empresa1'
        return empresa_menor_amplitude
    
    elif index_menor_amplitude == 1:
        empresa_menor_amplitude = 'empresa2'
        return empresa_menor_amplitude
    
    elif index_menor_amplitude == 2:
        empresa_menor_amplitude = 'empresa3'
        return empresa_menor_amplitude
    
    elif index_menor_amplitude == 3:
        empresa_menor_amplitude = 'empresa4'
        return empresa_menor_amplitude
    
    elif index_menor_amplitude == 4:
        empresa_menor_amplitude = 'empresa5'
        return empresa_menor_amplitude

    index_menor_variancia = variancia.index(menor_variancia)

    if index_menor_variancia == 0:
        empresa_menor_variancia = 'empresa1'
        return empresa_menor_variancia
    
    elif index_menor_variancia == 1:
        empresa_menor_variancia = 'empresa2'
        return empresa_menor_variancia
    
    elif index_menor_variancia == 2:
        empresa_menor_variancia = 'empresa3'
        return empresa_menor_variancia
    
    elif index_menor_variancia == 3:
        empresa_menor_variancia = 'empresa4'
        return empresa_menor_variancia
    
    elif index_menor_variancia == 4:
        empresa_menor_variancia = 'empresa5'
        return empresa_menor_variancia
        
    print(f'''

        O que você deseja:
          
        1 - Ver a Melhor Empresa
        2 - Ver a Pior Empresa
        3 - Ver todas as Empresas
            
        ''')
    print(empresa_maior_moda)