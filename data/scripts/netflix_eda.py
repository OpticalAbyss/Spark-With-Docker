# Import Required Libraries
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, desc, count, when

# Initialize Spark Session
spark = SparkSession.builder \
    .appName("Netflix EDA") \
    .getOrCreate()

print("Spark Session Initialized.")

# Load the Dataset
data_path = "/data/netflix_titles.csv"  # Update with your dataset path
print("Loading dataset...")
df = spark.read.csv(data_path, header=True, inferSchema=True)

# Show first 5 rows
print("Dataset Preview:")
df.show(5)

# Print Schema
print("Dataset Schema:")
df.printSchema()

# Total Records
total_records = df.count()
print(f"Total Records: {total_records}")

# Describe Basic Statistics
print("Basic Statistics:")
df.describe().show()

# Count of Movies vs TV Shows
print("Count of Movies vs TV Shows:")
df.groupBy("type").count().show()

# Top 5 Directors with Most Titles
print("Top 5 Directors with the Most Titles:")
df.groupBy("director").count() \
    .orderBy(desc("count")) \
    .show(5)

# Trends in Content Release by Year
print("Yearly Trends in Content Releases:")
df.groupBy("release_year").count() \
    .orderBy("release_year") \
    .show()

# Check for Missing Values
print("Missing Values in Each Column:")
missing_values = df.select([
    count(when(col(c).isNull(), c)).alias(c) for c in df.columns
])
missing_values.show()

# Stop Spark Session
spark.stop()
print("Spark Session Stopped.")
