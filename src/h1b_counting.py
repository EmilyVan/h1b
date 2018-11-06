# Python 2.7
import sys
import string
import collections

# Open CSV file and read each line into tuple list
def readFile(filePath):
    try:
        file = open(filePath)
        list = []

        line = file.readline()
        temp = line.split(';')
        statusIndex = 0
        for columnName in temp:
            if 'STATUS' in columnName:
                break
            statusIndex += 1
        list.append(temp)
        while line:
            temp = line.split(';')
            if temp[statusIndex] == 'CERTIFIED':
                list.append(temp)
            line = file.readline()
    except IOError as e:
        print "I/O error({0}): {1}".format(e.errno, e.strerror)

    return list

def findTopOccupations(list):
    socNameIndex = 0
    socNameList = []

    for columnName in list[0]:
        if 'SOC_NAME' in columnName:
            break
        socNameIndex += 1
    for i in range(1, len(list)):
        socNameList.append(list[i][socNameIndex].replace('\"',''))

    return collections.Counter(socNameList).most_common(10)

def findTop10States(list):
    stateIndex = 0
    stateList = []

    for columnName in list[0]:
        if 'WORKSITE_STATE' in columnName:
            break
        stateIndex += 1
    for i in range(1, len(list)):
        stateList.append(list[i][stateIndex])

    return collections.Counter(stateList).most_common(10)

def calculatePercentage(totalNum, top10List):
    newTop10list = []
    for item in top10List:
        percentage = item[1] / float(totalNum)
        newItem = (item[0], item[1], str('{:.1%}'.format(percentage)))
        newTop10list.append(newItem)

    return newTop10list

def writeToFile(filename, list):
    f = open(filename, 'w')
    if 'top_10_occupations' in filename:
        f.write('TOP_OCCUPATIONS;NUMBER_CERTIFIED_APPLICATIONS;PERCENTAGE\n')
    else:
        f.write('TOP_STATES;NUMBER_CERTIFIED_APPLICATIONS;PERCENTAGE\n')
    for item in list:
        f.write(';'.join(str(s) for s in item))
        f.write('\n')
    f.close()

def main():
    if len(sys.argv) == 4:
        inputFile = sys.argv[1]
        outputTopOccupationsFile = sys.argv[2]
        outputTop10StatesFile = sys.argv[3]
    else:
        print "Please Use Correct Arguments"
        exit(1)

    dateList = readFile(inputFile)
    totalNum = len(dateList) - 1

    topOccupations = findTopOccupations(dateList)
    top10States = findTop10States(dateList)

    finalTopOccupations = sorted(calculatePercentage(totalNum, topOccupations), key = lambda x: (-x[1], x[0]))
    finalTop10States = sorted(calculatePercentage(totalNum, top10States), key = lambda x: (-x[1], x[0]))

    writeToFile(outputTopOccupationsFile, finalTopOccupations)
    writeToFile(outputTop10StatesFile, finalTop10States)

if __name__ == '__main__':
    main()



