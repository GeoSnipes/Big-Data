"""Write a spark program to group the words in a given text file based on their starting letters."""
from pyspark import SparkContext, SparkConf

def printList(groups):
    print(groups[0], end="")
    for li in groups[1]:
        print(", "+li, end="")

# Set up
#sc =SparkContext.getOrCreate()
conf = SparkConf().setAppName("ICP2").setMaster("local[*]")
sc = SparkContext(conf=conf)

file = sc.textFile("icp2_phrases.txt")

# In each line, split by space, and save each
# Take each word and create a key value pair with the first letter being key and value the word
wordGroup = file.flatMap(lambda line: line.split(" ")).map(lambda word: (word[0], word)).cache()

# Group by key(first letter)
wordGroup = wordGroup.groupByKey().mapValues(list)

if True:
    # spark raw output
    wordGroup.saveAsTextFile("Output")
else:
    # in program output
    TWG = wordGroup.collect()
    for val in TWG:
        #print(val) or
        printList(val)
        print()