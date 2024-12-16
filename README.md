# **Netflix EDA using Apache Spark (PySpark)**

This project performs **Exploratory Data Analysis (EDA)** on the **Netflix TV Shows & Movies Dataset** using Apache Spark with Python (PySpark). The analysis focuses on understanding the data, identifying patterns, and generating key insights.

## **Project Overview**

The goal of this project is to:
1. Set up and run Apache Spark using Docker.
2. Perform EDA using **PySpark**.
3. Analyze trends, summarize statistics, and derive insights from the dataset.

## **Dataset**

The dataset used is **Netflix TV Shows and Movies**. It contains information about:
- Title, Director, Cast
- Release Year, Duration
- Content Type (Movies/TV Shows)
- Ratings and More.

- **Source**: [Kaggle - Netflix Dataset](https://www.kaggle.com/datasets/shivamb/netflix-shows)  
- **File**: `netflix_titles.csv`

## **Setup Instructions**

### **1. Prerequisites**

Ensure you have the following installed:
- **Docker**: [Install Docker](https://docs.docker.com/get-docker/)
- **Git**: [Install Git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)

### **2. Set Up Apache Spark Using Docker**

1. **Pull Apache Spark Docker Image**:  
   Use the official Spark PySpark image:
   ```bash
   docker pull apache/spark-py
   ```

2. **Run Spark in a Docker Container**:  
   Start the container and mount your project folder:
   ```bash
   docker run -it -p 4040:4040 -v ${PWD}:/data apache/spark-py bash
   ```
   - `-p 4040:4040`: Maps Spark UI to port 4040.
   - `-v ${PWD}:/data`: Maps your local directory to `/data` inside the container.

## **Project Files**

### **Structure**
```plaintext
netflix-spark-eda/
├── data/
│   └── netflix_titles.csv       # Netflix dataset
|   └── scripts/
│       └── netflix_eda.py           # PySpark script for EDA
└── README.md                    # Project documentation
```

## **Running the Project**

### **1. Execute the PySpark Script**

Run the following command inside the container to perform EDA:
```bash
spark-submit /data/scripts/netflix_eda.py
```

## **Code Walkthrough**

### **1. Load Data and Initialize Spark**
The script initializes the Spark session and loads the dataset:
```python
from pyspark.sql import SparkSession

# Start Spark session
spark = SparkSession.builder.appName("Netflix_EDA").getOrCreate()

# Load Dataset
df = spark.read.csv("/data/netflix_titles.csv", header=True, inferSchema=True)

# Show initial rows
df.show(5)
```

### **2. Basic EDA**

- **View Schema**:
   ```python
   df.printSchema()
   ```

- **Total Records**:
   ```python
   print(f"Total Records: {df.count()}")
   ```

- **Basic Statistics**:
   ```python
   df.describe().show()
   ```

### **3. Data Exploration**

- **Count of Movies vs. TV Shows**:
   ```python
   df.groupBy("type").count().show()
   ```

- **Top Directors**:
   ```python
   from pyspark.sql.functions import col

   df.groupBy("director").count() \
     .orderBy(col("count").desc()) \
     .show(5)
   ```

- **Yearly Content Trends**:
   ```python
   df.groupBy("release_year").count() \
     .orderBy("release_year") \
     .show()
   ```

## **Output**

### **Example Insights**:
1. **Count of Movies vs TV Shows**:
   ```
   +---------+-----+
   |    type |count|
   +---------+-----+
   |   Movie |  600|
   | TV Show |  300|
   +---------+-----+
   ```

2. **Top 5 Directors**:
   ```
   +------------------+-----+
   |          director|count|
   +------------------+-----+
   |    Rajiv Chilaka|   19|
   |    Jay Karas     |   14|
   |  Steven Spielberg|   10|
   +------------------+-----+
   ```

3. **Yearly Trends**:
   ```
   +------------+-----+
   |release_year|count|
   +------------+-----+
   |        2021|   45|
   |        2020|   90|
   |        2019|   80|
   +------------+-----+
   ```

## **Spark UI**

- Access the Spark UI on **`http://localhost:4040`** to view job execution details.

## **Author**

- **Obyss**
- **GitHub Profile**: [Github](https://github.com/OpticalAbyss)

## **License**

This project is licensed under the MIT License.
