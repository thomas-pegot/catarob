# -*- coding: iso8859-1 -*- 
'''
Created on 18 août 2013

@author: thomas
'''
import numpy as np

from cv2 import cv


class Image(object):
    '''
    classdocs
    '''


    def __init__(self, path):
        '''
        Constructor
        '''
        self.path = path
        self.current_image = None
        self.prev_image = None
    
    def cv_load(self):
        self.current_image = cv.LoadImage(self.path)       

    def cv_resize(self, size_choice = None):
        self.prev_image = cv.CloneImage(self.current_image)
        if size_choice=="694 x 462":
            self.current_image = cv.CreateImage((696,462),cv.IPL_DEPTH_8U, 3)
        elif size_choice=="1392 x 924":
            self.current_image = cv.CreateImage((1392,924),cv.IPL_DEPTH_8U, 3)        
        cv.Resize(self.prev_image, self.current_image)
               