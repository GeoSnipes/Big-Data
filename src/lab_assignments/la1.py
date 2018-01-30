"""This is a tab separated list of "user id | item id | rating | timestamp".
Write Spark Transformations and Actions to find the users who have rated more than 25 items."""

from pyspark import SparkConf, SparkContext


#Set up Spark
conf = SparkConf().setAppName("la1").setMaster("local[*]")
sc = SparkContext(conf=conf)

data = sc.textFile("u.data")

#split each line into its list record
#map 1st element in each list to a value of one and format as a tuple key value pair
#store data in cache instead of hdd
wc = data.map(lambda line: line.split("\t")).map(lambda word: (word[0], 1)).cache()

#combine everywhere the key is the same
wcCount = wc.reduceByKey(lambda x, y: x+y)

#return only entries where count is grater than 25
wcFilter = wcCount.filter(lambda word : word[1] > 25)

if True:
    #output using Spark
    wcFilter.saveAsTextFile("FilterG25")
else:
    #<--------------------Or--------------->
    # Output using regular file write
    output = wcFilter.collect()
    outputText = open("OutputText.txt", "w")
    outputText.write(str(output))
    outputText.close()
