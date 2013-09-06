# -*- coding: iso8859-1 -*- 


from PyQt4 import QtGui
from catarob.gui.mainwindow import MainWindow
import sys

app = QtGui.QApplication.instance()
if not app:
	app = QtGui.QApplication(sys.argv)
menu = MainWindow()
menu.show()
try:
	sys.exit(app.exec_())
except SystemExit:
	print SystemExit
