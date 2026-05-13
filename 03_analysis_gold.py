# Databricks notebook source
from pyspark.sql import functions as F

spark.sql("USE mvp_yelp")

business = spark.table("silver_business_restaurants")
reviews = spark.table("silver_reviews")
users = spark.table("silver_users")

# =====================================
# PERGUNTA 1
# Top 10 cidades com mais restaurantes
# =====================================

top_cities = (
    business.groupBy("city")
    .count()
    .orderBy(F.desc("count"))
)

display(top_cities.limit(10))

# =====================================
# PERGUNTA 2
# Restaurantes com maior avaliação
# =====================================

best_restaurants = (
    business
    .filter(F.col("review_count") > 100)
    .select("name", "city", "stars", "review_count")
    .orderBy(F.desc("stars"))
)

display(best_restaurants.limit(10))

# =====================================
# PERGUNTA 3
# Média de estrelas por cidade
# =====================================

city_avg = (
    business
    .groupBy("city")
    .agg(F.avg("stars").alias("avg_stars"))
    .orderBy(F.desc("avg_stars"))
)

display(city_avg.limit(10))

# =====================================
# PERGUNTA 4
# Usuários mais ativos
# =====================================

top_users = (
    users
    .orderBy(F.desc("review_count"))
)

display(top_users.limit(10))

# =====================================
# PERGUNTA 5
# Distribuição das avaliações
# =====================================

review_distribution = (
    reviews
    .groupBy("stars")
    .count()
    .orderBy("stars")
)

display(review_distribution)