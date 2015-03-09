import unittest
from ParseToFloat import ParseToFloat

# This is used to test functions in class ParseToFloat
class parseToFloatTestCase(unittest.TestCase):
    def setUp(self):
        self.parseToFloat = ParseToFloat()

    # This is used to test function processFile
    def test_parseToFloat(self):
        float1, count1 = self.parseToFloat.parseToFloat('19.000', 0)
        self.assertEquals(count1, 1)
        self.assertEquals(float1, 19.0)
        float2, count2 = self.parseToFloat.parseToFloat('19a.000', 0)
        self.assertEquals(count2, 0)
        self.assertEquals(float2, 0.0)
        float2, count2 = self.parseToFloat.parseToFloat('1911111111111111111111111111111111111111111111111111111.000', 0)
        self.assertEquals(count2, 1)
        self.assertEquals(float2, 1.911111111111111e+54)

if __name__ == "__main__":
    unittest.main()