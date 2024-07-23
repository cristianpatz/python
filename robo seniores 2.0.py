import pandas as pd
import os
from datetime import datetime
import tkinter as tk
from tkinter import ttk, messagebox

def processar_arquivos_e_exportar():
    diretorio = r'H:\CUSTODIA\26 SQ FIDC\3 - FIDC\Seniores'
    data = entry_data.get()

    try:
        df = []

        for arquivo in os.listdir(diretorio):
            if arquivo.endswith('.xlsx'):
                df.append(pd.read_excel(os.path.join(diretorio, arquivo)))

        df_princial = pd.concat(df, axis=0)

        data2 = datetime.strptime(data, "%d/%m/%Y")
        data_formatada = data2.strftime("%d%m%Y")

        filtro = df_princial[df_princial['Data'].isin([data])]
        dfvlcot = filtro['Valor pós amort']
        dfemissao = filtro['Emissão']

        MTM = pd.DataFrame(filtro, columns= ['tipoManual','codfeeder','datBase', 'codresp', 'codcart', 'cnpjcpf', 'codtitulo', 'codemissao', 'codoperorig','mtmpontatermo', 'tipcot', 'txapropope', 'basecot', 'vlcot', 'codremu', 'codserie', 'PUCURVA'])
        MTM['tipoManual'] = 'rendafixa'
        MTM['datBase'] = data_formatada
        MTM['codfeeder'] = 'AMPLIS'
        MTM['codresp'] = 'OLIVEIRA TRUST'
        MTM['codcart'] = ' '
        MTM['cnpjcpf'] = ' '
        MTM['codtitulo'] = 'CLASSES SUPERIORES'
        MTM['codemissao'] = dfemissao
        MTM['codoperorig'] = ' '
        MTM['mtmpontatermo'] = 'AM'
        MTM['tipcot'] = 1
        MTM['txapropope'] = ' '
        MTM['basecot'] = 3
        MTM['vlcot'] = dfvlcot
        MTM['codremu'] = ' '
        MTM['codserie'] = ' '
        MTM['PUCURVA'] = dfvlcot

        
        MTM.to_csv(os.path.join(diretorio, 'MTM DIARIO', 'MTM.csv'), sep=';', decimal=',', index=False)

        messagebox.showinfo("Concluído", "Arquivo MTM.csv criado com sucesso!")

    except Exception as e:
        messagebox.showerror("Erro", f"Ocorreu um erro: {e}")


root = tk.Tk()
root.title("Robô Seniores 2.0")
root.geometry("300x150")

label_data = ttk.Label(root, text="Digite a data (DD/MM/AAAA):")
label_data.pack(pady=5)
entry_data = ttk.Entry(root)
entry_data.pack(pady=5)

button_processar = ttk.Button(root, text="Gerar arquivo", command=processar_arquivos_e_exportar)
button_processar.pack(pady=5)

root.mainloop()