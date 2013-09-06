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





class MainWindow(QMainWindow, Ui_MainWindow):
	"""
	Class documentation goes here.
	"""
	def __init__(self, parent = None):
		"""
		Constructor
		"""
		super(MainWindow,self).__init__(parent)
		self.setupUi(self)


import sys
app = QtGui.QApplication(sys.argv)
menu = MainWindow()
menu.show()
try:
	sys.exit(app.exec_())
except SystemExit:
	pass
