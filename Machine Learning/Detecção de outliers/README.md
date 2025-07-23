# Detecção de Outliers com KNN

Este exercício tem como objetivo aplicar técnicas de detecção de outliers utilizando o algoritmo KNN (K-Nearest Neighbors) em uma base de dados de cobertura vegetal (`cov_types.csv`) que está salva localmente na máquina.

---

### 1. Carregamento da Base de Dados

A base de dados `cov_types.csv` deve ser carregada diretamente do arquivo salvo na máquina local para o ambiente de trabalho, utilizando uma biblioteca adequada para manipulação de dados, como o pandas.

---

### 2. Análise Exploratória Inicial

Para entender a distribuição dos dados e identificar possíveis valores atípicos visualmente, devem ser criados gráficos do tipo boxplot para as três primeiras variáveis numéricas da base.

Além disso, recomenda-se a criação de scatterplots combinando essas três variáveis entre si para observar a relação entre elas e a presença visual de possíveis outliers.

---

### 3. Aplicação do Detector de Outliers KNN

Utilizando um modelo de detecção de outliers baseado em KNN, aplique este detector somente sobre as variáveis numéricas preditoras da base de dados.

O algoritmo irá analisar os dados e identificar quais instâncias estão distantes dos seus vizinhos mais próximos, classificando essas instâncias como possíveis outliers.

---

### 4. Análise dos Resultados

Após a aplicação do detector, recupere os rótulos atribuídos pelo modelo, onde normalmente:

- **0** indica instâncias consideradas normais (inliers),
- **1** indica instâncias identificadas como outliers.

Conte a frequência de cada rótulo para ter uma noção da quantidade de outliers detectados.

Além disso, obtenha os scores de decisão, que indicam o grau de anomalia de cada instância, sendo valores maiores associados a maior probabilidade de serem outliers.

---

### 5. Extração e Visualização dos Outliers

Com base nos rótulos, filtre os índices das instâncias classificadas como outliers e extraia os dados correspondentes para análise detalhada.

Essa etapa permite examinar quais registros do conjunto de dados foram considerados atípicos pelo modelo, podendo servir para decisões posteriores de tratamento ou investigação.

---

## Considerações Finais

- É importante garantir que todas as bibliotecas necessárias estejam instaladas e importadas corretamente no ambiente.
- A escolha das variáveis numéricas para o detector deve ser feita com cuidado para que o modelo funcione corretamente.
- A visualização inicial com boxplots e scatterplots é fundamental para compreensão dos dados antes da modelagem.
- A detecção de outliers é uma etapa importante em análise de dados para melhorar a qualidade dos modelos preditivos.

---

## 👨‍💻 Autor

Matheus — Estudante de Análise e Desenvolvimento de Sistemas com foco em Ciência de Dados.