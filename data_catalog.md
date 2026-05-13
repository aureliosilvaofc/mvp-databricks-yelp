# Catálogo de Dados

## bronze_business
Tabela contendo os estabelecimentos do Yelp.

### Campos principais
- business_id: identificador único
- name: nome do estabelecimento
- city: cidade
- state: estado
- stars: média de estrelas
- review_count: quantidade de reviews
- categories: categorias do estabelecimento

### Domínios esperados
- stars: valores entre 1 e 5
- review_count: valores maiores ou iguais a 0

---

## bronze_review
Tabela contendo as avaliações.

### Campos principais
- review_id
- user_id
- business_id
- stars
- useful
- funny
- cool

### Domínios esperados
- stars: entre 1 e 5
- useful/funny/cool: >= 0

---

## bronze_user
Tabela contendo usuários da plataforma Yelp.

### Campos principais
- user_id
- name
- review_count
- average_stars

### Domínios esperados
- average_stars: entre 1 e 5
- review_count: >= 0

---

## Silver Layer
Camada responsável pela limpeza, padronização e transformação dos dados.

---

## Gold/Analysis
Camada responsável pelas análises exploratórias e respostas às perguntas de negócio.
