import pandas as pd
import matplotlib.pyplot as plt
from io import StringIO

# Dados fornecidos
data = """CO_CURSO;LATITUDE;LONGITUDE;CO_MUNICIPIO;NO_CURSO;CO_CINE_ROTULO;TP_GRAU_ACADEMICO
1,521,433;-23.54;-46.63;3550308;CIÊNCIA DE DADOS;0617C01;1
1,521,433;-23.54;-46.63;3550308;CIÊNCIA DE DADOS;1
1,599,656;-23.54;-46.63;3550308;CIÊNCIA DE DADOS;1
1,603,036;-23.54;-46.63;3550308;CIÊNCIA DE DADOS;1
1,538,622;-22.01;-47.89;3548906;CIÊNCIA DE DADOS;1
1,600,504;-19.81;-43.95;3106200;CIÊNCIA DE DADOS;1
1,571,410;-3.68;-39.58;2306306;3
1,550,460;-7.11;-34.86;2507507;3
1,545,554;-23.44;-46.91;3547304;3
1,618,685;-23.6;-46.91;3513009;3
1,589,553;-23.96;-46.33;3548500;3
1,543,013;-22.97;-49.87;3534708;3
1,536,760;-21.68;-51.07;3500105;3
"""

# Ler os dados
df = pd.read_csv(StringIO(data), sep=';')

# Contar a frequência de cada grau acadêmico
grau_academico_counts = df['TP_GRAU_ACADEMICO'].value_counts()

# Criar o gráfico de barras
plt.figure(figsize=(10, 6))
grau_academico_counts.plot(kind='bar', color='skyblue')
plt.title('Distribuição de Grau Acadêmico dos Cientistas de Dados')
plt.xlabel('Grau Acadêmico')
plt.ylabel('Número de Ocorrências')
plt.xticks(rotation=0)
plt.grid(axis='y')

# Mostrar o gráfico
plt.show()
