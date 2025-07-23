# Análise Estatística de Idades - Censo

## 📄 Descrição do Exercício

Este exercício tem como objetivo praticar o uso de estatísticas descritivas aplicadas a um conjunto de dados reais. Utilizamos o arquivo `census.csv`, que contém diversas informações sobre a população, incluindo a variável de interesse: **idade**.

## 🎯 Objetivo

Realizar a análise estatística da coluna `age`, calculando diferentes medidas de tendência central:

- Média Aritmética
- Média Harmônica
- Média Geométrica
- Média Quadrática
- Mediana
- Moda

## 📊 Medidas Calculadas

Cada uma dessas medidas representa uma forma distinta de "média" ou centro dos dados. Elas nos ajudam a entender a distribuição da variável `idade` sob diferentes perspectivas:

### ▪️ Média Aritmética
É a soma de todas as idades dividida pelo número total de registros. Representa o valor médio clássico.

### ▪️ Média Harmônica
Calculada como o inverso da média dos inversos das idades. Dá mais peso para valores menores.

### ▪️ Média Geométrica
Raiz enésima do produto de todas as idades. É útil quando os dados têm crescimento proporcional.

### ▪️ Média Quadrática (RMS)
Raiz quadrada da média dos quadrados das idades. Dá mais peso para valores altos.

### ▪️ Mediana
Valor central quando as idades estão ordenadas. Não sofre influência de extremos.

### ▪️ Moda
Valor mais frequente na distribuição de idades. Indica a idade com maior ocorrência.

## 📈 Comparação das Médias

A comparação entre os valores obtidos permite observar como os dados estão distribuídos:

- **Se todas as médias forem parecidas**, a distribuição tende a ser simétrica.
- **Se a média aritmética for maior que a mediana**, a distribuição pode estar assimétrica à direita (com valores extremos altos).
- **Se a média harmônica for bem menor que a aritmética**, há muitos valores pequenos influenciando a média.
- **A média quadrática sempre será maior ou igual à aritmética**, pois ela eleva os valores ao quadrado.

## 📌 Conclusão

A análise das diferentes médias, junto com a mediana e a moda, permite uma compreensão mais completa da variável `idade`. Cada medida traz uma nuance diferente e ajuda a identificar características como simetria, presença de outliers e concentração de valores.

---