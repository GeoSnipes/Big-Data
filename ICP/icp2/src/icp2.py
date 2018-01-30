from pyspark import SparkContext, SparkConf

def printList(groups):
    print(groups[0], end="")
    for li in groups[1]:
        print(", "+li, end="")

#sc =SparkContext.getOrCreate()
conf = SparkConf().setAppName("ICP2").setMaster("local[*]")
sc = SparkContext(conf=conf)

file = sc.textFile("icp2_phrases.txt")
wordGroup = file.flatMap(lambda line: line.split(" ")).map(lambda word: (word[0], word)).cache()
wordGroup = wordGroup.groupByKey().mapValues(list)
TWG = wordGroup.collect()

if True:
    # spark raw output
    wordGroup.saveAsTextFile("Output")
else:
    # in program output
    for val in TWG:
        #print(val) or
        printList(val)
        print()