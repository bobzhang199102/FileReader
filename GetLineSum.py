from ParseToFloat import ParseToFloat

class GetLineSum:
       def getLineSum(self, eachLine,  count,  totalSum):
        sequence = eachLine.split(" ")
        parseToFloat = ParseToFloat()
        for index, item in enumerate(sequence):
            num, countTemp = parseToFloat.parseToFloat(item, count)
            count = countTemp
            totalSum += num
        return count, totalSum