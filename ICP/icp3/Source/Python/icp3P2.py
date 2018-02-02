"""mplement K-Mean Clustering on provided 3D Road Network (North Jutland, Denmark) Data Set.
  1.Cluster the data into 3 and 4 classes
  2.Evaluate clustering by computing Within Set Sum of Squared Errors
  3.Compare their results"""

from pyspark import SparkContext, SparkConf
from pyspark.mllib.clustering import KMeans, KMeansModel
from pyspark.mllib.linalg import Vectors


# Set up
# sc =SparkContext.getOrCreate()
conf = SparkConf().setAppName("ICP3_P1").setMaster("local[*]")
sc = SparkContext(conf=conf)

# Load and parse the data
data = sc.textFile("3D_spatial_network.txt")
parsedData = data.map(lambda line: [float(x) for x in line.split(',')])

# Look at how training data is!
#parsedData.foreach(lambda x: print(x))

# Cluster the data into three classes using KMeans
numClusters = 3
numIterations = 20
clusters = KMeans.train(parsedData, numClusters, numIterations)

# Evaluate clustering by computing Within Set Sum of Squared Errors
WSSSE = clusters.computeCost(parsedData)
print("\n\nWithin Set Sum of Squared Errors = " + str(WSSSE))

# Look at how the clusters are in training data by making predictions
print("Clustering on training data: ")
clusters.predict(parsedData).zip(parsedData).foreach(lambda x: print("Cluster: {0} \tData: {1}".format(x[0], x[1])))
                                                     # f=>println(f._2,f._1))

# Save and load model
# clusters.save(sc, "data/KMeansModel4")
# sameModel = KMeansModel.load(sc, "data/KMeansModel4")

print("\n\nWithin Set Sum of Squared Errors = " + str(WSSSE))