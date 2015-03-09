class ParseToFloat:
    def parseToFloat(self, stringNum, count):
        f = 0
        try:
            f = float(stringNum)
            count+=1
        except ValueError:
            f = 0.0
        return  (f,count)