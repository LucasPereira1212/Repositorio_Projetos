from desvio import desvio
from mediana import mediana
from moda import moda2
from ampliutide import amplitude
from variança import variacao
from media import media



def main():
      empresa1 = [1000,6000,1200,8000,1400]
      empresa2 = [5000,4000,3000,2000,7000]
      empresa3 = [1200,1300,8000,3000,15000]
      empresa4 = [1400,1750,2000,4500,5900]
      empresa5 = [1400,1750,2000,4500,5900]
      empresas = ['Empresa1', 'Empresa2', 'Empresa3', 'Empresa4', 'Empresa5']

      moda = []
      amplitudes = []
      desvios = []
      medianas = []
      variancia = []
      medias = []

      moda1 = moda2(empresa1)
      moda.append(moda1)

      moda3 = moda2(empresa2)
      moda.append(moda3)

      moda4 = moda2(empresa3)
      moda.append(moda4)

      moda5= moda2(empresa4)
      moda.append(moda5)

      moda6 = moda2(empresa5)
      moda.append(moda6)

      amplitude1 = amplitude(empresa1)
      amplitudes.append(amplitude1)

      amplitude2 = amplitude(empresa2)
      amplitudes.append(amplitude2)

      amplitude3 = amplitude(empresa3)
      amplitudes.append(amplitude3)

      amplitude4 = amplitude(empresa4)
      amplitudes.append(amplitude4)

      amplitude5 = amplitude(empresa5)
      amplitudes.append(amplitude5)

      desvios1 = desvio(empresa1)
      desvios.append(desvios1)

      desvio2 = desvio(empresa2)
      desvios.append(desvio2)

      desvio3 = desvio(empresa3)
      desvios.append(desvio3)

      desvio4 = desvio(empresa4)
      desvios.append(desvio4)

      desvio5 = desvio(empresa5)
      desvios.append(desvio5)

      mediana1 = mediana(empresa1)
      medianas.append(mediana1)      

      mediana2 = mediana(empresa2)
      medianas.append(mediana2) 

      mediana3 = mediana(empresa3)
      medianas.append(mediana3) 

      mediana4 = mediana(empresa4)
      medianas.append(mediana4) 

      mediana5 = mediana(empresa5)
      medianas.append(mediana5) 

      variancia1 = variacao(empresa1)
      variancia.append(variancia1)

      variancia2 = variacao(empresa2)
      variancia.append(variancia2)

      variancia3 = variacao(empresa3)
      variancia.append(variancia3)

      variancia4 = variacao(empresa4)
      variancia.append(variancia4)

      variancia5 = variacao(empresa5)
      variancia.append(variancia5)

      media1 = media(empresa1)
      medias.append(media1)

      media2 = media(empresa2)
      medias.append(media2)

      media3 = media(empresa3)
      medias.append(media3)

      media4 = media(empresa4)
      medias.append(media4)

      media5 = media(empresa5)
      medias.append(media5)


      maior_moda = max(moda)
      maior_amplitude = max(amplitudes)
      maior_desvio = max(desvios)
      maior_mediana = max(medianas)
      maior_variancia = max(variancia)
      maior_medias = max(medias)

      index_maior_moda = moda.index(maior_moda)
      index_maior_amplitude = amplitudes.index(maior_amplitude)
      index_maior_desvio = desvios.index(maior_desvio)
      index_maior_mediana = medianas.index(maior_mediana)
      index_maior_variancia= variancia.index(maior_variancia)
      index_maior_medias = medias.index(maior_medias)
      
      print(f'''

            As melhores empresas em cada departamento foi

            Media = {empresas[index_maior_medias]}, com {maior_medias}

            Moda = {empresas[index_maior_moda]}, com {maior_moda}

            Amplitude = {empresas[index_maior_amplitude]}, com {maior_amplitude}

            Variancia = {empresas[index_maior_variancia]}, com {maior_variancia}

            Desvio = {empresas[index_maior_desvio]}, com {maior_desvio}

            Mediana = {empresas[index_maior_mediana]}, com {maior_mediana}


            ''')
main()      

