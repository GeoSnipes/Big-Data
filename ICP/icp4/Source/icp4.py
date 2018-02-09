"""We have a test dataset of 10 records with expected outcomes and a set of predictions.
 Calculate the Confusion Matrix for the below data(using code)."""

from pyspark import SparkContext, SparkConf
from pyspark.mllib.evaluation import MulticlassMetrics

conf = SparkConf().setAppName("ICP4").setMaster("local[*]")
sc = SparkContext(conf=conf)

#expected   predicted
data = sc.textFile("data.txt")

#as to what i understand, MultiClassMetrics only uses pairs of floats
#so on each line of input I split the classes(man or woman) by space
#then I return 0 if is a man or 1 if is a woman
exp_pre = data.map(lambda line: [(float(0) if x == 'man' else float(1)) for x in line.split(' ')]).cache()

#print out how it looks in the array/list,
#data is small so this is possible
#print(exp_pre.collect())

#convert data into a confusion matrix
metrics = MulticlassMetrics(exp_pre)


#view the confusion matrix
print(metrics.confusionMatrix().toArray())
print("Accuracy: {}".format(metrics.accuracy))
print("Misclassification rate: {:.2f}".format(1-metrics.accuracy)) #format to 2 decimal places, python only
print("True positive rate of man: {:.2f}".format(metrics.truePositiveRate(0.0)))
print("True positive rate of woman: {:.2f}".format(metrics.truePositiveRate(1.0)))
print("False positive rate of man: {:.2f}".format(metrics.falsePositiveRate(0.0)))
print("False positive rate of woman: {:.2f}".format(metrics.falsePositiveRate(1.0)))
print("Specificity of man: {:.2f}".format(1 - metrics.falsePositiveRate(0.0)))
print("Specificity of woman: {:.2f}".format(1 - metrics.falsePositiveRate(1.0)))
print("Precision of man: {:.2f}".format(metrics.precision(0.0)))
print("Precision of woman: {:.2f}".format(metrics.precision(1.0)))
