# Databricks notebook source
from pyspark.sql import functions as F

# =====================================
# USAR DATABASE
# =====================================

spark.sql("USE mvp_yelp")

# =====================================
# LER TABELAS BRONZE
# =====================================

business = spark.table("bronze_business")
reviews  = spark.table("bronze_review")
users    = spark.table("bronze_user")

# =====================================
# BUSINESS (somente restaurantes)
# =====================================

silver_business = (
    business
    .withColumn("is_open", F.col("is_open").cast("int"))
    .withColumn("review_count", F.col("review_count").cast("int"))
    .withColumn("stars", F.col("stars").cast("double"))
    .withColumn("categories", F.col("categories").cast("string"))
    .filter(F.col("categories").contains("Restaurants"))
    .select(
        "business_id",
        "name",
        "address",
        "city",
        "state",
        "postal_code",
        "latitude",
        "longitude",
        "stars",
        "review_count",
        "is_open",
        "categories"
    )
)

# =====================================
# REVIEWS
# =====================================

silver_reviews = (
    reviews
    .withColumn("stars", F.col("stars").cast("double"))
    .withColumn("useful", F.col("useful").cast("int"))
    .withColumn("funny", F.col("funny").cast("int"))
    .withColumn("cool", F.col("cool").cast("int"))
    .withColumn("date", F.to_timestamp("date"))
    .select(
        "review_id",
        "user_id",
        "business_id",
        "stars",
        "date",
        "useful",
        "funny",
        "cool"
    )
)

# =====================================
# USERS
# =====================================

silver_users = (
    users
    .withColumn("review_count", F.col("review_count").cast("int"))
    .withColumn("average_stars", F.col("average_stars").cast("double"))
    .withColumn("yelping_since", F.to_timestamp("yelping_since"))
    .select(
        "user_id",
        "name",
        "review_count",
        "yelping_since",
        "average_stars"
    )
)

# =====================================
# SALVAR TABELAS SILVER
# =====================================

silver_business.write.format("delta").mode("overwrite").saveAsTable("silver_business_restaurants")

silver_reviews.write.format("delta").mode("overwrite").saveAsTable("silver_reviews")

silver_users.write.format("delta").mode("overwrite").saveAsTable("silver_users")

# =====================================
# MOSTRAR TABELAS
# =====================================

display(spark.sql("SHOW TABLES IN mvp_yelp"))