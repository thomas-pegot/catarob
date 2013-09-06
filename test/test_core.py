# -*- coding: iso8859-1 -*- 
'''
Created on 20 août 2013

@author: thomas
'''
import unittest
from cv2 import cv
from catarob.core.preprocessing import Image, Preprocessing
import numpy as np

class ImageTestPath(unittest.TestCase):
    def setUp(self):
        print "Setup.."
        self.path = ["eazere", 1, 254, 10.0, "/usr", "/home/test.jpg", "data/image_test.jpg", "data/fake_type.jpg"]

            
    def testPathError(self):
        self.failUnlessRaises(TypeError, Image, self.path)
        
    def tearDown(self):
        print "tearDown.."
        del self.path

class ImageTestMethod(ImageTestPath, unittest.TestCase):
    def testCVWrongPathImage(self):  
        #test image non existante
        self.assertRaises(IOError, cv.LoadImage, "data/image_.jpg")
    def testCVFakeTypeImage(self):  
        #Test extension d'image fausse 
        self.assertRaises(IOError, cv.LoadImage, "data/fake_type.jpg")

class PreprocessingTest(ImageTestPath, unittest.TestCase):
    def test_find_height_divide_by_zero(self):
        Prep = Preprocessing("data/fake_type.jpg")   
        coord_laser = np.array([ [1,1] , [1,1], [1,1], [1,1] ])
        dim_image = np.array([1, 1])
        self.assertRaises(RuntimeWarning, Prep.find_height, coord_laser, np.array([0, 0]),1.,1. )
        self.assertRaises(ZeroDivisionError, Prep.find_height, coord_laser, dim_image,1,1 )



def suite():
    suite = unittest.TestSuite()
    suite.addTest(ImageTestPath('testPathError'))
    suite.addTest(ImageTestMethod('testPathError'))    
    suite.addTest(ImageTestMethod('testCVWrongPathImage'))
    suite.addTest(ImageTestMethod('testCVFakeTypeImage'))
    suite.addTest(PreprocessingTest('test_find_height_divide_by_zero'))
    return suite

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    #unittest.main()
    #suite = unittest.TestLoader().loadTestsFromTestCase(ImageTest)
    #unittest.TextTestRunner(verbosity=3).run(suite)    
    unittest.TextTestRunner(verbosity=2).run(suite()) # Ran 3 tests in 0.000s, OK
