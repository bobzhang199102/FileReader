import unittest
from FileProcess import FileProcess

# This is used to test functions in class FileProcess
class FileProcessTestCase(unittest.TestCase):
    def setUp(self):
        self.fileProcess = FileProcess()

    # This is used to test function processFile
    def test_processFile(self):
        x, count = self.fileProcess.processFile("./TestData1")
        self.assertEqual(x, 8.888888888888889e+35)
        self.assertEquals(count, 42)
        x, count = self.fileProcess.processFile("./TestData2")
        self.assertEqual(x, 933.0 )
        self.assertEquals(count, 83)



if __name__ == "__main__":
    unittest.main()