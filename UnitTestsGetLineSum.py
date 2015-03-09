import unittest
from GetLineSum import GetLineSum

# This is used to test functions in class Fibonacci
class GetLineSumTestCase(unittest.TestCase):
    def setUp(self):
        self.getLineSum = GetLineSum()

    # This is used to test function processFile
    def test_getLineSum(self):
        line1 = "1 4 98 19 -1"
        count1, sum1 = self.getLineSum.getLineSum(line1,0,0)
        self.assertEquals(count1, 5)
        self.assertEquals(sum1, 121)
        line2 = "1 4 9%8 19 -1"
        count2, sum2 = self.getLineSum.getLineSum(line2,0,0)
        self.assertEquals(count2, 4)
        self.assertEquals(sum2, 23)


if __name__ == "__main__":
    unittest.main()