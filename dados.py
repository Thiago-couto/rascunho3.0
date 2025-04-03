import pandas as pd 
 
 # Carregar os dados de um arquivo CSV
 file_path = "/mnt/data/The Impacts of Seleção de Dados (Base INEP).csv" 
 df = pd.read_csv(file_path) 
 # Selecionar dados com base em uma condição
 dados_selecionados = df[df['coluna A'] == 'valor_desejado']

 # Exibir os dados selecionados
 print(dados_selecionados)
