# -*- coding: iso8859-1 -*- 
'''
Created on 20 août 2013

@author: thomas
'''
import unittest
from catarob.core.preprocessing import Image

class ImageTestPath(unittest.TestCase):
    def setUp(self):
        self.path = ["eazere", 1, 254, 10.0, "/usr", "/home/test.jpg", "data/image_test.jpg"]
            
    def testPathError(self):
        self.failUnlessRaises(TypeError, Image, self.path)
        

class ImageTestMethod(ImageTestPath, unittest.TestCase):
    def testWrongTypeImage(self):  
        #self.path = ["eazere", 1, 254, 10.0, "/usr", "/home/test.jpg", "data/image_test.jpg"]
        self.image = Image(self.path)    
        self.assertRaises(TypeError, self.image.cv_load, "data/image_test.jpg")

class PreprocessingTest(ImageTestPath, unittest.TestCase):

    def test_unexpected_value(self):
        pass

def suite():
    tests = ['testPathError', 'testWrongTypeImage']
    return unittest.TestSuite(map(ImageTestMethod, tests))

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    #unittest.main()
    #suite = unittest.TestLoader().loadTestsFromTestCase(ImageTest)
    #unittest.TextTestRunner(verbosity=3).run(suite)    
    unittest.TextTestRunner(verbosity=2).run(suite()) # Ran 3 tests in 0.000s, OK
