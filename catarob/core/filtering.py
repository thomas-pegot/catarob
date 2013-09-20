# -*- coding: iso8859-1 -*-
'''
Created on 31 août 2013

@author: thomas
'''
import gpumeanshift as _pymeanshift


class Filtering(object):
    '''
    Segmenter class using the mean shift algorithm to segment image
    '''

    def __init__(self, spatial_radius=None, range_radius=None):
        '''
        Segmenter init function. See function segment for keywords description.
        '''
        self._spatial_radius = None
        self._range_radius = None
        self._min_density = None

        if spatial_radius is not None:
            self.spatial_radius = spatial_radius
        if range_radius is not None:
            self.range_radius = range_radius

    def __call__(self, image):
        '''
        Segment the input image (color or grayscale).

        Keyword arguments:
            image -- Input image (2-D or 3-D numpy array or compatible).

        Return value: tuple (segmented, labels, nb_regions)
        segmented -- Image (Numpy array) where the color (or grayscale) of the
                     regions is the mean value of the pixels belonging to a region.
        labels -- Image (2-D Numpy array, 32 unsigned bits per element) where a
                  pixel value correspond to the region number the pixel belongs to.
        nb_regions -- The number of regions found by the mean shift algorithm.

        NOTES: To avoid unnecessary image conversions when the function is called,
        make sure the input image array is 8 unsigned bits per pixel and is
        contiguous in memory.

        '''
        if self._spatial_radius is None:
            raise ValueError("Spatial radius has not been set")
        if self._range_radius is None:
            raise ValueError("Range radius has not been set")

        return _pymeanshift.filter(image, self._spatial_radius,
                                   self._range_radius)

    def __str__(self):
        return "<Segmenter: spatial_radius={}, range_radius={},\
    >".format(
            self._spatial_radius,
            self._range_radiu)

    def __repr__(self):
        return "Segmenter(spatial_radius={}, range_radius={},\
                )".format(
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
