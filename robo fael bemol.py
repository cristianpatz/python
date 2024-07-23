import os
import shutil
from datetime import datetime

pasta_principal = r'H:\CUSTODIA\26 SQ FIDC\11 - CNAB\BEMOL\RELATORIO'

data_atual = datetime.now()
data_formatada = data_atual.strftime("%d.%m.%y")

pasta_destino1 = r'H:\INTEGRACOES\VERT\Saida\Gestora\Bemol\06_Estoque'
pasta_destino2 = r'H:\INTEGRACOES\BEMOL\Saida\4.Lastro'
pasta_destino3 = r'H:\INTEGRACOES\BEMOL\Saida\3.DemaisOcorrencias'

pasta_data_atual = os.path.join(pasta_principal, data_formatada)

if os.path.exists(pasta_data_atual):
    for arquivo in os.listdir(pasta_data_atual):
        if arquivo.endswith(".csv"):
            shutil.copy(os.path.join(pasta_data_atual, arquivo), pasta_destino1)
            shutil.copy(os.path.join(pasta_data_atual, arquivo), pasta_destino2)
            shutil.copy(os.path.join(pasta_data_atual, arquivo), pasta_destino3)
    print("Arquivos copiados com sucesso!")
else:
    print("Pasta com a data de hoje não encontrada.")