from __future__ import print_function

import numpy as np

from pyspark import SparkContext
# $example on$
from pyspark.mllib.stat import Statistics
from pyspark.sql import SparkSession


if __name__ == "__main__":

    spark = SparkSession\
        .builder\
        .appName("test")\
        .getOrCreate()

	#Helloworld    
    print("HELLO WORLD!!")

    #read CSV
    df = spark.read.csv("datasets/Pokemon.csv")
    df.show()
    
    df.printSchema()

    df.select("_c1").show()

    spark.stop()