import pandas as pd
import os
from datetime import datetime

diretorio = r'H:\CUSTODIA\26 SQ FIDC\3 - FIDC\Seniores'   

df = []

for arquivo in os.listdir(diretorio):
    if arquivo.endswith('.xlsx'):
        df.append(pd.read_excel(os.path.join(diretorio, arquivo)))

df_princial = pd.concat(df, axis=0)

data = input('Qual data você deseja? (formato AAAA-MM-DD)')
data2 = datetime.strptime(data, "%Y-%m-%d")
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

MTM.to_csv('H:/CUSTODIA/26 SQ FIDC/3 - FIDC/Seniores/MTM DIARIO/MTM.csv', sep= ';', decimal=',')