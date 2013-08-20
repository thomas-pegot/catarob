# -*- coding: iso8859-1 -*- 
'''
Created on 18 août 2013

@author: thomas
'''
#import numpy as np

from cv2 import cv
import os

class Image(object):
    '''
    classdocs
    '''


    def __init__(self, path):
        '''
        Constructor
        '''
        self.path = None
        self.current_image = None
        self.prev_image = None    
        self.img_loaded = 0   
        
        if(type(path) != str):
            raise TypeError
        elif(not(os.path.exists(path) or os.path.isfile(path))):
            raise NameError
        else:
            self.path = path

    def cv_load(self):
        try:
            self.current_image = cv.LoadImage(self.path)       
        except ValueError:
            print ValueError

    def cv_resize(self, size_choice = None):
        if (not self.img_loaded):
            print "image not loaded; \n\
            You might use cv_load method before cv_resize."
            return 0
        self.prev_image = cv.CloneImage(self.current_image)
        if size_choice=="694 x 462":
            self.current_image = cv.CreateImage((696,462),cv.IPL_DEPTH_8U, 3)
        elif size_choice=="1392 x 924":
            self.current_image = cv.CreateImage((1392,924),cv.IPL_DEPTH_8U, 3)
        elif size_choice == None:
            return 1
        else:
            print "Bad size_choice arguments: 694 x 462 or 1392 x 924 or None"
            return 0
        cv.Resize(self.prev_image, self.current_image)
        return 1