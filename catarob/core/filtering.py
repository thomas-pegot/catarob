#!/usr/bin/env python
# encoding: utf-8
'''
.. module:: filtering.py
    ::synopsis:
.. moduleauthor:: Thomas Pegot <thomas.pegot@gmail.com>
 Last Modified: septembre 23, 2013
'''
import gpumeanshift as _pymeanshift

class Filtering(object):
    '''
    Segmenter class using the mean shift GPU OpenCV to segment image
    Example::
        import cv2
        from gpumeanshift import filter
        I = cv2.imread("path/to/image", cv2.CV_IMREAD_COLOR)
        A = filter(I, 12, 12, 1)
    '''
    def __init__(self, spatial_radius=None, range_radius=None):
        """Initialisation:

        :param spatial_radius: Spatial radius in pixel
        :param range_radius: Range radius in pixel
        :type spatial_radius: int
        :type range_radius: int

        """
        self._spatial_radius = spatial_radius
        self._range_radius = range_radius

    def __call__(self, image):
        '''Call:.

        :param image: image color with alpha channel
        :type image: ndarray 4 channels
        :returns: filtered image (ndarray 3 channels)

        '''
        if self._spatial_radius is None:
            raise ValueError("Spatial radius has not been set")
        if self._range_radius is None:
            raise ValueError("Range radius has not been set")

        return _pymeanshift.filter(image, self._spatial_radius,
                                   self._range_radius)

    def __str__(self):
        return "<Segmenter: spatial_radius={}, range_radius={}>".format(
            self._spatial_radius,
            self._range_radius)

    def __repr__(self):
        return "Segmenter(spatial_radius={}, range_radius={})".format(
            self._spatial_radius,
            self._range_radius)

    @property
    def spatial_radius(self):
        '''
        Spatial radius of the search window
        '''
        return self._spatial_radius

    @spatial_radius.setter
    def spatial_radius(self, value):
        if value < 0:
            raise AttributeError("Spatial radius must be greater or equal to zero")
        self._spatial_radius = value

    @property
    def range_radius(self):
        '''
        Range radius of the search window
        '''
        return self._range_radius

    @range_radius.setter
    def range_radius(self, value):
        if value < 0:
            raise AttributeError(
                "Range radius must be greater or equal to zero")
        self._range_radius = value
