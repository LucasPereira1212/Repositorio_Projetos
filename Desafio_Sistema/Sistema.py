import tkinter as tk
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import statistics
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg



dados = pd.read_csv('dados1.csv')
vendas = dados['vendas']
vendedor = dados['vendedor']

transformacao1 = np.array(vendas)
transformacao2 = np.array(vendedor)


def grafico1():
    fig, grafico = plt.subplots()
    grafico.bar(vendedor, vendas, color='red')

    canvas = FigureCanvasTkAgg(fig, master = janela)
    canvas.draw()
    canvas.get_tk_widget().pack(side = tk.RIGHT, fill=tk.BOTH, expand=True)

def grafico2():
    fig, grafico = plt.subplots()
    grafico.scatter(vendedor, vendas, color='red')

    canvas = FigureCanvasTkAgg(fig, master = janela)
    canvas.draw()
    canvas.get_tk_widget().pack(side = tk.RIGHT, fill=tk.BOTH, expand=True)

def grafico3():
    fig, grafico = plt.subplots()
    grafico.plot(vendedor, vendas, color='red')

    canvas = FigureCanvasTkAgg(fig, master = janela)
    canvas.draw()
    canvas.get_tk_widget().pack(side = tk.RIGHT, fill=tk.BOTH, expand=True)

def grafico4():
    fig, grafico = plt.subplots()
    grafico.pie(vendas, labels=vendedor, autopct='%.2f')

    canvas = FigureCanvasTkAgg(fig, master = janela)
    canvas.draw()
    canvas.get_tk_widget().pack(side = tk.RIGHT, fill=tk.BOTH, expand=True)

def estatisticas():
    mediana = np.median(transformacao1)
    media = np.median(transformacao1)
    desvio = np.sqrt(transformacao1)
    moda = statistics.mode(transformacao1)
    varianca = np.var(transformacao1)
    text.config(text=f'''MÉDIA:{media}
                        MEDIANA:{mediana}
                        DESVIO:{desvio} 
                        MODA:{moda}
                        VARIANÇA{varianca}
                                                ''')                  

def deletar():
    sair = tk.DISABLED(grafico1)



janela = tk.Tk()
janela.title('Graficos de Vendas')

bt1 = tk.Button(janela, text='Grafico de Barras', command=grafico1)
bt1.pack()

bt2 = tk.Button(janela, text='Graficos de Scatter', command=grafico2)
bt2.pack()

bt3 = tk.Button(janela, text='Graficos de linhas', command=grafico3)
bt3.pack()

bt4 = tk.Button(janela, text='Graficos de pizza', command=grafico4)
bt4.pack()

bt5 = tk.Button(janela, text='Estatisticas', command=estatisticas)
text = tk.Label(janela, text='Estatisticas')

text.pack()
bt5.pack()







janela.mainloop()






