def printList(groups):
    print(groups[0], end="")
    for li in groups[1]:
        print(", "+li, end="")

sc =SparkContext.getOrCreate()
file = sc.textFile("phrases.txt")
wordGroup = file.flatMap(lambda line: line.split(" ")).map(lambda word: (word[0], word)).cache()
wordGroup = wordGroup.groupByKey().mapValues(list)
TWG = wordGroup.collect()
for val in TWG:
    #print(val) or
    printList(val)
    print()