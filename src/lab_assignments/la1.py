from pyspark import SparkConf, SparkContext

#Set up Spark
conf = SparkConf().setAppName("la1").setMaster("local[*]")
sc = SparkContext(conf=conf)

