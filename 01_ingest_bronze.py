# Databricks notebook source
from pyspark.sql import functions as F

# =====================================
# PATH DOS ARQUIVOS
# =====================================

BASE_PATH = "dbfs:/Volumes/workspace/default/yelp"

BUSINESS_FILE = f"{BASE_PATH}/business.json"
REVIEW_FILE   = f"{BASE_PATH}/review.json"
USER_FILE     = f"{BASE_PATH}/user.json"

# =====================================
# CRIAR DATABASE
# =====================================

spark.sql("CREATE DATABASE IF NOT EXISTS mvp_yelp")
spark.sql("USE mvp_yelp")

# =====================================
# LEITURA DOS JSONS
# =====================================

df_business = spark.read.json(BUSINESS_FILE)
df_review   = spark.read.json(REVIEW_FILE)
df_user     = spark.read.json(USER_FILE)

# =====================================
# SALVAR TABELAS BRONZE
# =====================================

(df_business.write
    .format("delta")
    .mode("overwrite")
    .saveAsTable("bronze_business"))

(df_review.write
    .format("delta")
    .mode("overwrite")
    .saveAsTable("bronze_review"))

(df_user.write
    .format("delta")
    .mode("overwrite")
    .saveAsTable("bronze_user"))

# =====================================
# MOSTRAR TABELAS
# =====================================

display(spark.sql("SHOW TABLES IN mvp_yelp"))