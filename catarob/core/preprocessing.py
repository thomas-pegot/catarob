# -*- coding: iso8859-1 -*-
'''

.. module:: preprocessing
    :platform: Unix
    :synopsis: Module working on image with EXIF data.

.. moduleauthor: Thomas Pegot <thomas.pegot@gmail.com>

Created on 17 août 2013
'''

import pyexiv2
from catarob.core.base import *
import pylab as pl
import numpy as np
import cv2.cv as cv
import scipy.ndimage as ndimage
from catarob.lib import cvnumpy

#@singleton
class Preprocessing(object):
    @staticmethod
    def read_metadata(path):
        ''' Pick model, focal and zoom data from Exif data of picture.

        :param path: full picture path
        :type path: str
        :return: model, focal, zoom
        :rtype: tuple'''
        metadata = pyexiv2.ImageMetadata(str(path))
        metadata.read()
        model = metadata['Exif.Image.Model'].value
        focal = float(metadata['Exif.Photo.FocalLength'].value)
        zoom = float(metadata['Exif.Photo.DigitalZoomRatio'].value)
        focal_apparent = focal*zoom
        return model, focal_apparent, zoom

    @staticmethod
    def cv_resize(image, size_choice=None):
        """Resize an iplimage

        :param size_choice: "694x462" or "1392x924" or None
        :returns: image resizei
        :type size_choice: iplimage CV_8UC3
        :rtype: same as size_choice
        """
        prev_image = cv.CloneImage(image)
        if size_choice == "694x462":
            image = cv.CreateImage((696, 462), cv.IPL_DEPTH_8U, 3)
        elif size_choice == "1392x924":
            image = cv.CreateImage((1392, 924), cv.IPL_DEPTH_8U, 3)
        elif size_choice is None:
            return image
        else:
            print "Bad size_choice arguments: 694 x 462 or 1392 x 924 or None"
            return 0
        cv.Resize(prev_image, image)
        return image

    @typedef_control(np.ndarray, np.ndarray, float, float)
    def find_height(self, coord_laser, dim_image, focale, zoom):
        """Seek out distance between  camera<->objet

            This find distance between object and camera with laser spacing

            :param coord_laser: Coordinate of four laser
            :param dim_image: Dimension of image
            :param focale: Focale of camera in mm
            :param zoom: Zoom ratio
            :type coord_laser: (2,2) nd.array or list
            :type dim_image: ndarray (1,2)
            :type focale: float
            :type zoom: float
            :return: distance and pixel size
            :rtype: int, int
        """
        pts1 = np.array([coord_laser[:, 0].min(), coord_laser[:, 1].min()])
        pts2 = np.array([coord_laser[:, 0].max(), coord_laser[:, 1].max()])
        diag_laser_px = pl.dist(pts1, pts2)
        # Diagonale laser a 2m07 comme reference avec mesure de 109mm
        s = 43.0/np.sqrt(np.sum(dim_image**2))
        diag_laser_a_2m07 = 109
        ecart_angulaire_depuis_2m07 = 6.5/100
        hauteur_estimee = (focale*diag_laser_a_2m07/(s*diag_laser_px))
        ecart = (2068 - hauteur_estimee)*ecart_angulaire_depuis_2m07
        hauteur = hauteur_estimee-ecart


        # Dimension laser metrologie avec ajustement de non parallelisme
        taille_pixel = (hauteur/focale)*(np.array([24.0/dim_image[0], 36.0/dim_image[1]]))


        return hauteur, taille_pixel
    @staticmethod
    def extraction_laser(image, disp=False):
        """ Extraction des laser en image de label
        """
        ## Conversion vers Lab recuperation a
        Lab = cv.CloneImage(image); cv.Zero(Lab)
        a = cv.CreateImage(cv.GetSize(image), cv.IPL_DEPTH_8U, 1)
        cv.CvtColor(image, Lab, cv.CV_BGR2Lab)
        cv.SetImageCOI(Lab,2)
        cv.Copy(Lab,a)

        ## Seuillage a au niveau laser
        BW = cv.CloneImage(a); cv.Zero(BW)
        T  = 0+128  #    Seuillage a 0+delta avec delta 128
        Nb_lbl = 0
        while Nb_lbl<4:
            cv.Threshold(a, BW, T, 255, cv.CV_THRESH_BINARY )
            A_BW = cvnumpy.cv2array(BW)[:,:,0]
            A_lbl, Nb_lbl = ndimage.label(A_BW)
            T-=1

        ## Correspondre bon label au laser
        center = np.floor(np.array(A_BW.shape)/2)
        # Contrainte de proximite au centre de l image considération d une photo prise distante de plus de 37cm
        # -> corresond proportion diagonale laser sur diagonale image de 17%
        proportion = 0.2
        diag_constraint = proportion*(np.sqrt(np.sum(np.array(A_BW.shape)**2)))
        # Verification contrainte
        new_lbl = 1
        A_center_lbl = A_lbl*0
        while new_lbl < Nb_lbl:
            for lbl in xrange(1,Nb_lbl+1):
                coord_current_lbl = np.unravel_index(pl.find(A_lbl==lbl),A_lbl.shape)
                coord_center = np.sum(coord_current_lbl, 1)/len(coord_current_lbl[0])
                diag_current_lbl = 2*np.sqrt(np.sum((coord_center-center)**2))
                if diag_current_lbl < diag_constraint:
                    A_center_lbl[coord_center[0],coord_center[1]] = new_lbl
                    A_lbl[A_lbl==lbl] = new_lbl
                    new_lbl+=1
                else:
                    A_lbl[A_lbl==lbl] = 0
            proportion -= 0.5


        if disp:
            #A_a = self.cv2array(a)[:,:,0]

            #fig1 = pl.figure()
            #pl.imshow(A_a, cmap = pl.cm.gray)
            #pl.title('Composante a de Lab')
            #fig1.show()

            fig2 = pl.figure()
            #pl.imshow(A_lbl)
            pl.title('Image label:Seuillage a '+repr(T))
            fig2.show()
        return np.transpose(np.unravel_index(pl.find(A_center_lbl>0), A_lbl.shape))


        def rectif(self,image, cadreIn, cadreOut):
            prev_image = cv.CloneImage(image); cv.Zero(image)
            mmat = cv.CreateMat(3,3, cv.CV_32FC1)
            print ("mmat= %s"%repr(mmat))
            cv.GetPerspectiveTransform(cadreIn , cadreOut, mmat)
            cv.WarpPerspective(prev_image, image, mmat)#, flags=cv.CV_WARP_INVERSE_MAP )






if __name__ == "__main__":
    #import sys, tkFileDialog

    path = "/home/thomas/Bureau/WatershedCV/fond_titre.jpg"
    #if len(sys.argv) > 1:
    #    path = sys.argv[1]
    #else:
    #    path = tkFileDialog.askopenfilename()

    Proc = Preprocessing(path)
    Proc.cv_load()
    coord_laser=Proc.extraction_laser()
    print type(np.array([]))
    model, focal_apparent, zoom = Proc.read_metadata()
    hauteur, taille_pixel = Proc.find_height(coord_laser, np.array([Proc.current_image.height, Proc.current_image.width]), focal_apparent, zoom)

    print "Model: %s    \nfocal: %i, zoom: %i"%(model, focal_apparent, zoom)
    print "hauteur: %i \ndimension pixel: %s"%(hauteur, taille_pixel.__repr__())



