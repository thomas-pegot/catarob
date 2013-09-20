# -*- coding: utf-8 -*-

"""
Module implementing MainWindow.
"""

from PyQt4.QtGui import QMainWindow
from PyQt4.QtCore import pyqtSignature
from PyQt4 import QtGui, Qt
from menumanager import MenuManager, OpenCVQImage
from Ui_mainwindow import Ui_MainWindow
from termstream import TermStream
from cv2 import cv

from catarob.core.preprocessing import Preprocessing
from catarob.core.segmentation import Segmentation
from catarob.core.filtering import Filtering

from catarob.lib.cvnumpy import cv2array

WINDOW_SIZE = [840, 680]
IMAGE_SIZE = [400, 300]


class MainWindow(QMainWindow, Ui_MainWindow, Preprocessing):
    """
    Class documentation goes here.
    """
    def __init__(self, parent=None):
        """
        Constructor
        """
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.menumanager = MenuManager()
        self.setFixedSize(*WINDOW_SIZE)
        self.ImageFrame.setFixedSize(*IMAGE_SIZE)
        TermStream.stdout().messageWritten.\
            connect(self.textBrowser.insertPlainText)
        TermStream.stderr().messageWritten.\
            connect(self.textBrowser.insertPlainText)
        self.alloc_attr()
        self.dict_step = {0: Preprocessing, 1: Filtering, 2: "Correction",
                          3: Segmentation, 4: "fitting"}

    def alloc_attr(self):
        self.current_image = None

    def update(self):
        """Call class and 4update image, and window """
        self.show_curr_image()

    def show_curr_image(self):
        curr_qimage = OpenCVQImage(self.current_image)
        displayed_image = curr_qimage.scaled(*IMAGE_SIZE)
        pixmap = QtGui.QPixmap.fromImage(displayed_image)
        self.ImageFrame.setPixmap(pixmap)

    def show_curr_metadata(self):
        meta = self.read_metadata(self.path)
        meta_str = "model : {}\n\
                focal : {}mm\n\
                zoom : {}".format(*meta)
        self.HelpLabel.setText(Qt.QString(meta_str))

    @pyqtSignature("")
    def on_OpenButton_clicked(self):
        """
        Slot documentation goes here.
        """
        try:
            self.path = Qt.QFileDialog.getOpenFileName(None,
                Qt.QString("Open Image"), Qt.QString("."),
                Qt.QString("Image Files (*.png *.jpg *.bmp"));
        except ValueError:
            print("Erreur chargement:%s" % ValueError)
        try:
            self.current_image = cv.LoadImage(str(self.path))
        except IOError:
            print IOError
        self.show_curr_metadata()
        self.show_curr_image()

    def on_RegisterButton_clicked(self):
        self.current_image = self.cv_resize(self.current_image, str(self.SizeBox.currentText()))
        self.HelpLabel.setText(Qt.QString("Resize done:{}".format(cv.GetSize(self.current_image))))

    @pyqtSignature("")
    def on_actionSave_current_image_triggered(self):
        """
        Slot documentation goes here.
        """
        save_path = Qt.QFileDialog.getSaveFileName(None, Qt.QString("Save Image"), Qt.QString("."), Qt.QString("Image Files (*.png *.jpg *.bmp"));

        try:
            cv.SaveImage(str(save_path), self.current_image)
        except ValueError:
            print ValueError

    def on_actionSave_current_image_2_triggered(self):
        self.on_actionSave_current_image_triggered()

    @pyqtSignature("")
    def on_actionRun_all_triggered(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        raise NotImplemented

    @pyqtSignature("")
    def on_actionRun_all_2_triggered(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        raise NotImplementedError

    @pyqtSignature("")
    def on_actionStop_triggered(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        raise NotImplementedError

    @pyqtSignature("")
    def on_actionView_statistics_triggered(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        raise NotImplementedError

    @pyqtSignature("")
    def on_actionHelp_2_triggered(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        raise NotImplementedError

    @pyqtSignature("")
    def on_actionQuit_triggered(self):
        """
        Slot documentation goes here.
        """
        # Destroy MainWindow object
        self.close()

    @pyqtSignature("")
    def on_FilterButton_clicked(self):
        filt = Filtering(int(self.RangeLCD.value()), int(self.SpaceLCD.value()))
        arr_image = cv2array(self.current_image)
        self.current_image = filt(arr_image)
        self.update()

