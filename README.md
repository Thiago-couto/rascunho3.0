# rascunho3.0
####    Objetivos específicos

- Analisar os dados e por meio deles obter informações sobre a demanda do curso Ciência de dados nos estados do Brasil, sendo esse importante para o planejamento do local em que as novas empresas dessa área serão melhor alocadas.

- Analisar os dados e por meio deles obter informações sobre o número de faculdades que atendem a Ciência de Dados nos estados do Brasil, de tal forma a ser importante para a implementação de tal nas regiões que ainda não se efetivou o curso em suas faculdades.

- Produzir um sistema eficiente, capaz de gerar dados que possibilitam expor os municípios que apresentam maiores quantidades de Cientista de Dados qualificados.

- Criar um sistema eficiente, o qual proporciona uma análise mais profunda sobre as qualidades necessárias para que um Cientista de Dados possa ser considerado especializado ( a partir de uma descrição de dados com variáveis).

Na nossa análise da densidade demográfica de Cientistas de Dados, optamos por selecionar certos atributos que se mostraram particularmente relevantes para entender melhor esse cenário. Esses atributos foram escolhidos com base em sua capacidade de fornecer insights significativos sobre a distribuição e as características dessa profissão em diferentes regiões.

- `State_of_data_BR_2023_Kaggle - df_survey_2023.csv`

| Atributos                  | Descrição                                         | Tipo de Dado               |
|----------------------------|---------------------------------------------------|----------------------------|
| `Gênero`                 | Masculino, Feminino, Outros                 | Categórico   (nominal)    |
| `Faixa Etária`            | Jovem, Adulto, Idoso                        |  Categórico (ordinal)     |
| `Faixa Salarial`          | Baixa, Média, Alta                          |  Categórico (ordinal)     |
| `Nível de experiência`     | Nenhum, Iniciante, Intermediário, Avançado  | Categórico (ordinal)       |
| `Cientista por Estado`     | Distribuição de cientistas por estado       | Numérico         |
| `Raça/Etnia/Cor`          | Diversidade racial e étnica                 | Categórico (nominal)       |
| `Cientistas por Região`    | Distribuição de cientistas por região       | Numérico         |
| `Nível de Ensino`          | Ensino Médio, Graduação, Pós-graduação      | Categórico (ordinal)       |
| `Situação Empresarial`     | Ativo, Desempregado, Aposentado            | Categórico (nominal)       |
| `Cargo`                   | Títulos de trabalho                          | Categórico (nominal)       
| `Área de Formação`         | Ciências Exatas, Humanas, Biológicas, etc. | Categórico (nominal)       |
 
- `Base_Auxiliar.csv`   
     
| Atributo              | Descrição                          |  Tipo de Dado  |
|-----------------------|------------------------------------|----------------|
| `CO_CURSO`              | Código do curso                    |  Numérico |
| `LATITUDE`              | Latitude do local                  |  Numérico |
| `LONGITUDE`             | Longitude do local                 |  Numérico |
| `CO_MUNICIPIO`         | Código do município                |  Numérico |
| `NO_CURSO`              | Nome do curso                      |  Categórico (nominal) |
| `CO_CINE_ROTULO`       | Código do cine rótulo              | Numérico |
| `TP_GRAU_ACADEMICO`    | Tipo de grau acadêmico             | Categórico (ordinal) |
| `TP_NIVEL_ACADEMICO`   | Tipo de nível acadêmico            | Categórico (ordinal) |   

Por outro lado, identificamos que os demais atributos não contribuíram de maneira eficaz para a nossa análise. Isso nos permitiu focar em dados que realmente fazem a diferença, garantindo que nossas conclusões sejam precisas e úteis. Ao concentrar nossos esforços nos atributos mais relevantes, conseguimos obter uma visão mais clara e informada sobre a demografia dos Cientistas de Dados, facilitando a tomada de decisões e o planejamento estratégico.















