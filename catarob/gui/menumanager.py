from PyQt4 import Qt,  QtCore,  QtGui
from cv2 import cv
from Ui_mainwindow import Ui_MainWindow
from PyQt4.QtGui import QMainWindow

class MenuManager(QMainWindow):
    def __init__(self,  parent=None):
        QMainWindow.__init__(self, parent)
    def  load_file(self, path = None):
		    
	if path == None:
		self.path = Qt.QFileDialog.getOpenFileName(None, Qt.QString("Open Image"),Qt.QString("."), Qt.QString("Image Files (*.png *.jpg *.bmp"))
	else:
		self.path = path
	self.current_image = cv.LoadImage(str(self.path))    
        self.current_image = OpenCVQImage(self.current_image)
        return QtGui.QImage(self.current_image)
        
 
class OpenCVQImage(QtGui.QImage):
    def __init__(self, opencvBgrImg):
        depth, nChannels = opencvBgrImg.depth, opencvBgrImg.nChannels
        if depth != cv.IPL_DEPTH_8U or nChannels != 3:
            raise ValueError("the input image must be 8-bit, 3-channel")
        w, h = cv.GetSize(opencvBgrImg)
        opencvRgbImg = cv.CreateImage((w, h), depth, nChannels)
        # it's assumed the image is in BGR format
        cv.CvtColor(opencvBgrImg, opencvRgbImg, cv.CV_BGR2RGB)
        self._imgData = opencvRgbImg.tostring()
        super(OpenCVQImage, self).__init__(self._imgData, w, h, 
            QtGui.QImage.Format_RGB888)
