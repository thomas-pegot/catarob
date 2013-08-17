# -*- coding: iso8859-1 -*- 
'''
Created on 17 août 2013

@author: thomas
'''

import pyexiv2
import numpy as np
import cv2.cv as cv

class Preprocessing(object):
    '''

    classdocs
    '''


    def __init__(self, path):
        '''
        Constructor
        '''
        self.path = path
        
    def load_image(self):
        self.current_image = cv.LoadImage(self.path)

    def read_metadata(self):
        ''' Lecture metadonnees de l'image '''
        metadata = pyexiv2.ImageMetadata(self.path); metadata.read()
        
        model = metadata['Exif.Image.Model'].value
        focal = np.float(metadata['Exif.Photo.FocalLength'].value)
        zoom = np.float(metadata['Exif.Photo.DigitalZoomRatio'].value)
        focal_apparent = focal*zoom
        
        return model, focal_apparent, zoom     
    
    def resize(self, size_choice):
        In_Resize = cv.CloneImage(self.current_image)
        if size_choice=="694 x 462":
            In_Resize = cv.CreateImage((696,462),cv.IPL_DEPTH_8U, 3)
        elif size_choice=="1392 x 924":
            In_Resize = cv.CreateImage((1392,924),cv.IPL_DEPTH_8U, 3)        
        cv.Resize(self.current_image, In_Resize)
        return In_Resize