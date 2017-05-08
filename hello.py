import sys

from pyspark.sql import SparkSession


if __name__ == "__main__":

    spark = SparkSession\
        .builder\
        .appName("hello")\
        .getOrCreate()

    print("HELLO WORLD!!")

    
    
    spark.stop()