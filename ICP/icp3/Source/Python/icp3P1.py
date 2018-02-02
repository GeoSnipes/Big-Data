"""Implement Linear Regression Model on provided 3D Road Network (North Jutland, Denmark) Data Set.
    1.Build the model using 50 iterations
    2.Split data into 70% training and 30% testing
    3.Report Training Mean Square Error
    4.Report Test Mean Square Error"""

from pyspark import SparkContext, SparkConf
from pyspark.mllib.linalg import Vectors
from pyspark.ml.regression import LinearRegressionModel
from pyspark.mllib.regression import LabeledPoint
from pyspark.mllib.regression import LinearRegressionWithSGD
import math

import numpy

def funcParse(line):
    values = [float(x) for x in line.replace(',', ' ').split(' ')]
    return LabeledPoint(values[0], values[1:])
    #parts = line.split(',')
    #return LabeledPoint(parts[0].toDouble, Vectors.dense(parts[1].split(' ').map(_.toDouble)))

def funcPoint(point):
    prediction = model.predict(point.features)
    return (point.label, prediction)

def funcPow(v):
    return math.pow((v[0] - v[1]), 2)

path = "D:\\Users\\Geovanni\\Sync\\UMKC\\1st 2nd Semester\\Big Data Analytics and Application\\Big-Data\\ICP\icp3\\output"

# Set up
#sc =SparkContext.getOrCreate()
conf = SparkConf().setAppName("ICP3_P1").setMaster("local[*]")
sc = SparkContext(conf=conf)

data = sc.textFile("3D_spatial_network.txt")

parsedData = data.map(funcParse).cache()
#parsedData.foreach(lambda f: print(f))

# Split data into training (95%) and test (5%).
training, test = parsedData.randomSplit([0.7, 0.3])

# Building the model
numIterations = 50
stepSize = 0.00000001
model = LinearRegressionWithSGD.train(training, numIterations, stepSize)

# Evaluate model on training examples and compute training error
valuesAndPreds = training.map(funcPoint)

MSE = valuesAndPreds.map(funcPow).mean()
print("training Mean Squared Error = " + str(MSE))

# Evaluate model on test examples and compute training error
valuesAndPreds2 = test.map(funcPoint)

MSE2 = valuesAndPreds2.map(funcPow).mean()
print("test Mean Squared Error = " + str(MSE2))

# Save and load model
#model.save(sc, path)
#sameModel = LinearRegressionModel.load(sc, path)
