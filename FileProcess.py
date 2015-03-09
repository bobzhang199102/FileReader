from GetLineSum import GetLineSum

class FileProcess:
   def processFile(self, FileAddress):
        fp = open(FileAddress, 'r')
        totalSum = 0
        count = 0
        getLineSumInstance = GetLineSum()
        for eachLine in fp:
            count, totalSum = getLineSumInstance.getLineSum(eachLine, count, totalSum)
        return  (totalSum,count)




