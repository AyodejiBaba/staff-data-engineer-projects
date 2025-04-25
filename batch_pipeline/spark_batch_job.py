#!/usr/bin/env python3
from pyspark.sql import SparkSession

def main():
    spark = (
        SparkSession
        .builder
        .appName("SparkBatchJob")
        .getOrCreate()
    )

    # TODO: load some data, transform it, write results
    df = spark.read.json("/data/input/")
    df.printSchema()
    df.show(10)

    spark.stop()

if __name__ == "__main__":
    main()
