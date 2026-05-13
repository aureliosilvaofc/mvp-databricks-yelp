# Linhagem dos Dados

## Origem dos Dados
Os dados foram obtidos através do Yelp Open Dataset disponível no Kaggle:
https://www.kaggle.com/datasets/yelp-dataset/yelp-dataset

## Processo de Coleta
1. Download manual do dataset.
2. Upload dos arquivos JSON para o Databricks Community Edition.
3. Persistência dos dados em Delta Tables.

## Pipeline de Dados

### Bronze
Ingestão dos arquivos JSON brutos:
- business
- review
- user

### Silver
Transformação e limpeza:
- cast de tipos
- filtro de restaurantes
- seleção de colunas relevantes

### Analysis
Consultas analíticas e exploração dos dados.

## Tecnologias utilizadas
- Databricks
- Apache Spark
- PySpark
- Delta Lake
