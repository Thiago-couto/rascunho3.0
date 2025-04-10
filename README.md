# rascunho3.0
####    Objetivos específicos

- Analisar os dados e por meio deles obter informações sobre a demanda do curso Ciência de dados nos estados do Brasil, sendo esse importante para o planejamento do local em que as novas empresas dessa área serão melhor alocadas.

- Analisar os dados e por meio deles obter informações sobre o número de faculdades que atendem a Ciência de Dados nos estados do Brasil, de tal forma a ser importante para a implementação de tal nas regiões que ainda não se efetivou o curso em suas faculdades.

- Produzir um sistema eficiente, capaz de gerar dados que possibilitam expor os municípios que apresentam maiores quantidades de Cientista de Dados qualificados.

- Criar um sistema eficiente, o qual proporciona uma análise mais profunda sobre as qualidades necessárias para que um Cientista de Dados possa ser considerado especializado ( a partir de uma descrição de dados com variáveis).

Na nossa análise da densidade demográfica de Cientistas de Dados, optamos por selecionar certos atributos que se mostraram particularmente relevantes para entender melhor esse cenário. Esses atributos foram escolhidos com base em sua capacidade de fornecer insights significativos sobre a distribuição e as características dessa profissão em diferentes regiões.

- `State_of_data_BR_2023_Kaggle - df_survey_2023.csv`

| Atributos                  | Motivos                                                                                     | Tipo de Dado               |
|----------------------------|---------------------------------------------------------------------------------------------|----------------------------|
| `Gênero`                   | Identificação de gênero dos cientistas de dados, importante para análises de diversidade      | Categórico   (nominal)    |
| `Faixa Etária`             | Classificação etária dos cientistas, útil para entender a distribuição etária na profissão   |  Categórico (ordinal)     |
| `Faixa Salarial`           | Níveis de renda dos cientistas, relevante para análises socioeconômicas da profissão         |  Categórico (ordinal)     |
| `Nível de experiência`     | Avaliação do nível de experiência dos cientistas, importante para entender a qualificação da força de trabalho | Categórico (ordinal)       |
| `Cientista por Estado`     | Quantidade de cientistas de dados em cada estado, essencial para mapear a distribuição geográfica     | Numérico         |
| `Raça/Etnia/Cor`           | Informações sobre a diversidade racial e étnica dos cientistas, importante para análises de inclusão  | Categórico (nominal)       |
| `Cientistas por Região`    | Distribuição de cientistas de dados por região, útil para identificar áreas com maior concentração    | Numérico         |
| `Nível de Ensino`          | Níveis educacionais dos cientistas, relevante para entender a formação acadêmica na área              | Categórico (ordinal)       |
| `Situação Empresarial`     | Status de emprego dos cientistas, importante para análises de mercado de trabalho                     | Categórico (nominal)       |
| `Cargo`                    | Títulos de trabalho ocupados pelos cientistas, útil para entender a hierarquia e funções na área      | Categórico (nominal)       
| `Área de Formação`         | Campos de estudo dos cientistas, importante para analisar a diversidade de formações na profissão     | Categórico (nominal)       |
 
- `Base_Auxiliar.csv`   
     
| Atributo              | Motivos                                                                        |  Tipo de Dado  |
|-----------------------|--------------------------------------------------------------------------------|----------------|
| `CO_CURSO`              | Importante para identificar a formação acadêmica dos profissionais na área   |  Numérico |
| `LATITUDE`              | Essencial para mapear a distribuição geográfica dos Cientistas de Dados      |  Numérico |
| `LONGITUDE`             | Complementa a latitude para a localização precisa dos profissionais          |  Numérico |
| `CO_MUNICIPIO`         | Relevante para analisar a concentração de Cientistas de Dados em diferentes regiões        |  Numérico |
| `NO_CURSO`              | Identificar as formações mais comuns entre os Cientistas de Dados            | Categórico (nominal) |
| `CO_CINE_ROTULO`        | Categorizar dados em análises mais complexas                                 | Numérico |
| `TP_GRAU_ACADEMICO`    | Analisar nível de formação dos profissionais na área                          | Categórico (ordinal) |
| `TP_NIVEL_ACADEMICO`   | Avaliar a qualificação e especialização dos Cientistas de Dados               | Categórico (ordinal) |   

Por outro lado, identificamos que os demais atributos não contribuíram de maneira eficaz para a nossa análise. Isso nos permitiu focar em dados que realmente fazem a diferença, garantindo que nossas conclusões sejam precisas e úteis. Ao concentrar nossos esforços nos atributos mais relevantes, conseguimos obter uma visão mais clara e informada sobre a demografia dos Cientistas de Dados, facilitando a tomada de decisões e o planejamento estratégico.















