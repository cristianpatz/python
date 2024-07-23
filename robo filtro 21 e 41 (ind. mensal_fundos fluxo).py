import pandas as pd
import tkinter as tk
from tkinter import filedialog
import time

def selecionar_arquivo():
    root = tk.Tk()
    root.withdraw()  # Ocultar a janela principal
    caminho_arquivo = filedialog.askopenfilename(
        title="Selecione o arquivo CSV",
        filetypes=[("CSV files", "*.csv")],
        initialdir="/"
    )
    return caminho_arquivo

arquivo_selecionado = selecionar_arquivo()

fort = pd.read_csv(arquivo_selecionado, sep=';', encoding='latin')

def calcular_soma_dividida(modalidade):
    filtro = fort[fort['modalidade'].isin([modalidade])]  # Filtra a modalidade
    filtro1 = filtro['vp_proj_ajustada'].str.replace(',', '.').astype(float)
    filtro2 = filtro['cet'].str.replace(',', '.').astype(float)

    multiplicando = filtro1 * filtro2  # Multiplica vp_proj x cet
    soma_filtro1 = filtro1.sum()  # Soma valor total de vp_proj
    divisao = multiplicando / soma_filtro1  # Divide os valores da multiplicação pela soma 
    divisao_soma = divisao.sum()  # Soma os valores que foram divididos
    return divisao_soma

modalidade_41 = calcular_soma_dividida(41)
print(f"Resultado para modalidade 41: {modalidade_41}")

modalidade_21 = calcular_soma_dividida(21)
print(f"Resultado para modalidade 21: {modalidade_21}")

time.sleep(60)