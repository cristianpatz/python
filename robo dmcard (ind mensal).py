import pandas as pd
import os

df = []
diretorio = r'H:\CUSTODIA\26 SQ FIDC\3 - FIDC\DM CARD\Robo_Indices_Mensais'

for arquivo in os.listdir(diretorio):
    if arquivo.startswith('DM'):
        try:
            df.append(pd.read_csv(os.path.join(diretorio, arquivo), encoding='latin1', on_bad_lines='skip',sep=';'))
        except pd.errors.ParserError as e:
            print(f"Erro ao ler o arquivo {arquivo}: {e}")

arrecadacao = pd.concat(df, axis=0)

dados_selecionados = arrecadacao[['ID_CONTA', 'VALOR']]
dados_agrupados = dados_selecionados.groupby('ID_CONTA').sum()
arquivo = pd.read_csv(r'H:\CUSTODIA\26 SQ FIDC\3 - FIDC\DM CARD\Robo_Indices_Mensais\saldos\saldo.csv', sep=';')
arquivo['VALOR'] = arquivo['VALOR'].str.replace('.', '').str.replace(',', '.').astype(float)
group_arquivo = arquivo.groupby('ID_CONTA')['VALOR'].sum()
resultado_merge = pd.merge(group_arquivo, dados_agrupados, left_on='ID_CONTA', right_on='ID_CONTA', how='inner')
df_final = pd.DataFrame(resultado_merge)
soma1 = df_final['VALOR_x'].sum()

df2 = []
diretorio2 = r'H:\CUSTODIA\26 SQ FIDC\3 - FIDC\DM CARD\Robo_Indices_Mensais\consolidado'

for arquivo2 in os.listdir(diretorio2):
    if arquivo2.startswith('dmcard'):
        try:
            df2.append(pd.read_csv(os.path.join(diretorio2, arquivo2), encoding='latin1', on_bad_lines='skip',sep=';'))
        except pd.errors.ParserError as e:
            print(f"Erro ao ler o arquivo {arquivo2}: {e}")
    
consolidado = pd.concat(df2)
soma2 = consolidado['Valor conciliado Fundo (referente as contas cedidas - comando 6)'].str.replace('.', '').str.replace(',', '.').astype(float).sum()

resultado = soma1 + soma2
resultado_csv = pd.DataFrame({"Soma dos valores": [resultado]})

resultado_csv.to_csv('H:/CUSTODIA/26 SQ FIDC/3 - FIDC/DM CARD/Robo_Indices_Mensais/resultado.csv', index= False)