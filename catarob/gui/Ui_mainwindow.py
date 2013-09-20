# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created: Thu Sep 19 15:49:52 2013
#      by: PyQt4 UI code generator 4.10
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(703, 523)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("../../../../Bureau/KTROB/catarob.ico")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setWindowOpacity(1.0)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet(_fromUtf8("     background-color: rgba(40,40,40,255);\n"
"     border-style: outset;\n"
"     border-width: 1px;\n"
"     border-radius: 6px;\n"
"     border-color: beige;\n"
"     font: 12px;\n"
"     min-width: 6em;\n"
"     padding: 4px;\n"
""))
        self.centralWidget = QtGui.QWidget(MainWindow)
        self.centralWidget.setStyleSheet(_fromUtf8(""))
        self.centralWidget.setObjectName(_fromUtf8("centralWidget"))
        self.gridLayout = QtGui.QGridLayout(self.centralWidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.ParamStack = QtGui.QToolBox(self.centralWidget)
        self.ParamStack.setMinimumSize(QtCore.QSize(56, 0))
        self.ParamStack.setAutoFillBackground(False)
        self.ParamStack.setStyleSheet(_fromUtf8("     background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                 stop: 0 #E1E1E1, stop: 0.4 #DDDDDD,\n"
"                                 stop: 0.5 #D8D8D8, stop: 1.0 #D3D3D3);\n"
"     border: 2px solid #C4C4C3;\n"
"     border-bottom-color: #C2C7CB; /* same as the pane color */\n"
"     border-top-left-radius: 4px;\n"
"     border-top-right-radius: 4px;\n"
"     min-width: 8ex;\n"
"     padding: 2px;\n"
""))
        self.ParamStack.setFrameShape(QtGui.QFrame.Panel)
        self.ParamStack.setFrameShadow(QtGui.QFrame.Sunken)
        self.ParamStack.setMidLineWidth(0)
        self.ParamStack.setObjectName(_fromUtf8("ParamStack"))
        self.RegistWidget = QtGui.QWidget()
        self.RegistWidget.setGeometry(QtCore.QRect(0, 0, 324, 75))
        self.RegistWidget.setToolTip(_fromUtf8("<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-style:italic;\">-Change size</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-style:italic;\">-Registering if necessary</span></p></body></html>"))
        self.RegistWidget.setStatusTip(_fromUtf8(""))
        self.RegistWidget.setWhatsThis(_fromUtf8("<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-style:italic;\">-Change size</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-style:italic;\">-Registering if necessary</span></p></body></html>"))
        self.RegistWidget.setAccessibleName(_fromUtf8(""))
        self.RegistWidget.setObjectName(_fromUtf8("RegistWidget"))
        self.RegisterButton = QtGui.QPushButton(self.RegistWidget)
        self.RegisterButton.setGeometry(QtCore.QRect(110, 40, 99, 27))
        self.RegisterButton.setObjectName(_fromUtf8("RegisterButton"))
        self.OpenButton = QtGui.QToolButton(self.RegistWidget)
        self.OpenButton.setEnabled(True)
        self.OpenButton.setGeometry(QtCore.QRect(40, 40, 72, 25))
        self.OpenButton.setObjectName(_fromUtf8("OpenButton"))
        self.SizeBox = QtGui.QComboBox(self.RegistWidget)
        self.SizeBox.setGeometry(QtCore.QRect(40, 10, 171, 27))
        self.SizeBox.setObjectName(_fromUtf8("SizeBox"))
        self.SizeBox.addItem(_fromUtf8(""))
        self.SizeBox.addItem(_fromUtf8(""))
        self.SizeBox.addItem(_fromUtf8(""))
        self.ParamStack.addItem(self.RegistWidget, _fromUtf8(""))
        self.FilterWidget = QtGui.QWidget()
        self.FilterWidget.setGeometry(QtCore.QRect(0, 0, 324, 75))
        self.FilterWidget.setObjectName(_fromUtf8("FilterWidget"))
        self.widget = QtGui.QWidget(self.FilterWidget)
        self.widget.setGeometry(QtCore.QRect(20, 0, 246, 72))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.widget)
        self.horizontalLayout_2.setMargin(0)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.gridLayout_2 = QtGui.QGridLayout()
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.RangeSlider = QtGui.QSlider(self.widget)
        self.RangeSlider.setMinimum(5)
        self.RangeSlider.setMaximum(20)
        self.RangeSlider.setOrientation(QtCore.Qt.Horizontal)
        self.RangeSlider.setObjectName(_fromUtf8("RangeSlider"))
        self.gridLayout_2.addWidget(self.RangeSlider, 0, 0, 1, 1)
        self.RangeLCD = QtGui.QLCDNumber(self.widget)
        self.RangeLCD.setFrameShape(QtGui.QFrame.Box)
        self.RangeLCD.setFrameShadow(QtGui.QFrame.Raised)
        self.RangeLCD.setObjectName(_fromUtf8("RangeLCD"))
        self.gridLayout_2.addWidget(self.RangeLCD, 0, 1, 1, 1)
        self.SpaceSlider = QtGui.QSlider(self.widget)
        palette = QtGui.QPalette()
        gradient = QtGui.QLinearGradient(0.0, 0.0, 0.0, 1.0)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(225, 225, 225))
        gradient.setColorAt(0.4, QtGui.QColor(221, 221, 221))
        gradient.setColorAt(0.5, QtGui.QColor(216, 216, 216))
        gradient.setColorAt(1.0, QtGui.QColor(211, 211, 211))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        gradient = QtGui.QLinearGradient(0.0, 0.0, 0.0, 1.0)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(225, 225, 225))
        gradient.setColorAt(0.4, QtGui.QColor(221, 221, 221))
        gradient.setColorAt(0.5, QtGui.QColor(216, 216, 216))
        gradient.setColorAt(1.0, QtGui.QColor(211, 211, 211))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        gradient = QtGui.QLinearGradient(0.0, 0.0, 0.0, 1.0)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(225, 225, 225))
        gradient.setColorAt(0.4, QtGui.QColor(221, 221, 221))
        gradient.setColorAt(0.5, QtGui.QColor(216, 216, 216))
        gradient.setColorAt(1.0, QtGui.QColor(211, 211, 211))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(79, 79, 59))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Highlight, brush)
        gradient = QtGui.QLinearGradient(0.0, 0.0, 0.0, 1.0)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(225, 225, 225))
        gradient.setColorAt(0.4, QtGui.QColor(221, 221, 221))
        gradient.setColorAt(0.5, QtGui.QColor(216, 216, 216))
        gradient.setColorAt(1.0, QtGui.QColor(211, 211, 211))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        gradient = QtGui.QLinearGradient(0.0, 0.0, 0.0, 1.0)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(225, 225, 225))
        gradient.setColorAt(0.4, QtGui.QColor(221, 221, 221))
        gradient.setColorAt(0.5, QtGui.QColor(216, 216, 216))
        gradient.setColorAt(1.0, QtGui.QColor(211, 211, 211))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        gradient = QtGui.QLinearGradient(0.0, 0.0, 0.0, 1.0)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(225, 225, 225))
        gradient.setColorAt(0.4, QtGui.QColor(221, 221, 221))
        gradient.setColorAt(0.5, QtGui.QColor(216, 216, 216))
        gradient.setColorAt(1.0, QtGui.QColor(211, 211, 211))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(79, 79, 59))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Highlight, brush)
        gradient = QtGui.QLinearGradient(0.0, 0.0, 0.0, 1.0)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(225, 225, 225))
        gradient.setColorAt(0.4, QtGui.QColor(221, 221, 221))
        gradient.setColorAt(0.5, QtGui.QColor(216, 216, 216))
        gradient.setColorAt(1.0, QtGui.QColor(211, 211, 211))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        gradient = QtGui.QLinearGradient(0.0, 0.0, 0.0, 1.0)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(225, 225, 225))
        gradient.setColorAt(0.4, QtGui.QColor(221, 221, 221))
        gradient.setColorAt(0.5, QtGui.QColor(216, 216, 216))
        gradient.setColorAt(1.0, QtGui.QColor(211, 211, 211))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        gradient = QtGui.QLinearGradient(0.0, 0.0, 0.0, 1.0)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(225, 225, 225))
        gradient.setColorAt(0.4, QtGui.QColor(221, 221, 221))
        gradient.setColorAt(0.5, QtGui.QColor(216, 216, 216))
        gradient.setColorAt(1.0, QtGui.QColor(211, 211, 211))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Highlight, brush)
        self.SpaceSlider.setPalette(palette)
        self.SpaceSlider.setMinimum(5)
        self.SpaceSlider.setMaximum(20)
        self.SpaceSlider.setOrientation(QtCore.Qt.Horizontal)
        self.SpaceSlider.setObjectName(_fromUtf8("SpaceSlider"))
        self.gridLayout_2.addWidget(self.SpaceSlider, 1, 0, 1, 1)
        self.SpaceLCD = QtGui.QLCDNumber(self.widget)
        self.SpaceLCD.setObjectName(_fromUtf8("SpaceLCD"))
        self.gridLayout_2.addWidget(self.SpaceLCD, 1, 1, 1, 1)
        self.horizontalLayout_2.addLayout(self.gridLayout_2)
        self.FilterButton = QtGui.QPushButton(self.widget)
        self.FilterButton.setObjectName(_fromUtf8("FilterButton"))
        self.horizontalLayout_2.addWidget(self.FilterButton)
        self.ParamStack.addItem(self.FilterWidget, _fromUtf8(""))
        self.LightWidget = QtGui.QWidget()
        self.LightWidget.setGeometry(QtCore.QRect(0, 0, 324, 75))
        self.LightWidget.setObjectName(_fromUtf8("LightWidget"))
        self.widget1 = QtGui.QWidget(self.LightWidget)
        self.widget1.setGeometry(QtCore.QRect(60, 10, 186, 100))
        self.widget1.setObjectName(_fromUtf8("widget1"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout(self.widget1)
        self.horizontalLayout_3.setMargin(0)
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.formLayout = QtGui.QFormLayout()
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.PolRButton = QtGui.QRadioButton(self.widget1)
        self.PolRButton.setObjectName(_fromUtf8("PolRButton"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.PolRButton)
        self.FreqRButton = QtGui.QRadioButton(self.widget1)
        self.FreqRButton.setObjectName(_fromUtf8("FreqRButton"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.FreqRButton)
        self.NoneRButton = QtGui.QRadioButton(self.widget1)
        self.NoneRButton.setObjectName(_fromUtf8("NoneRButton"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.NoneRButton)
        self.horizontalLayout_3.addLayout(self.formLayout)
        self.CorrectButton = QtGui.QPushButton(self.widget1)
        self.CorrectButton.setObjectName(_fromUtf8("CorrectButton"))
        self.horizontalLayout_3.addWidget(self.CorrectButton)
        self.ParamStack.addItem(self.LightWidget, _fromUtf8(""))
        self.SegmentWidget = QtGui.QWidget()
        self.SegmentWidget.setGeometry(QtCore.QRect(0, 0, 324, 75))
        self.SegmentWidget.setObjectName(_fromUtf8("SegmentWidget"))
        self.widget2 = QtGui.QWidget(self.SegmentWidget)
        self.widget2.setGeometry(QtCore.QRect(40, 10, 162, 56))
        self.widget2.setObjectName(_fromUtf8("widget2"))
        self.verticalLayout = QtGui.QVBoxLayout(self.widget2)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.comboBox = QtGui.QComboBox(self.widget2)
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.verticalLayout.addWidget(self.comboBox)
        self.SegementButton = QtGui.QPushButton(self.widget2)
        self.SegementButton.setObjectName(_fromUtf8("SegementButton"))
        self.verticalLayout.addWidget(self.SegementButton)
        self.ParamStack.addItem(self.SegmentWidget, _fromUtf8(""))
        self.FitWidget = QtGui.QWidget()
        self.FitWidget.setGeometry(QtCore.QRect(0, 0, 324, 75))
        self.FitWidget.setToolTip(_fromUtf8(""))
        self.FitWidget.setStyleSheet(_fromUtf8(""))
        self.FitWidget.setObjectName(_fromUtf8("FitWidget"))
        self.widget3 = QtGui.QWidget(self.FitWidget)
        self.widget3.setGeometry(QtCore.QRect(60, 10, 107, 56))
        self.widget3.setObjectName(_fromUtf8("widget3"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.widget3)
        self.verticalLayout_2.setMargin(0)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.comboBox_2 = QtGui.QComboBox(self.widget3)
        self.comboBox_2.setObjectName(_fromUtf8("comboBox_2"))
        self.comboBox_2.addItem(_fromUtf8(""))
        self.comboBox_2.addItem(_fromUtf8(""))
        self.verticalLayout_2.addWidget(self.comboBox_2)
        self.FitButton = QtGui.QPushButton(self.widget3)
        self.FitButton.setObjectName(_fromUtf8("FitButton"))
        self.verticalLayout_2.addWidget(self.FitButton)
        self.ParamStack.addItem(self.FitWidget, _fromUtf8(""))
        self.gridLayout.addWidget(self.ParamStack, 0, 0, 1, 1)
        self.HelpLabel = QtGui.QLabel(self.centralWidget)
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.HelpLabel.setFont(font)
        self.HelpLabel.setTextFormat(QtCore.Qt.PlainText)
        self.HelpLabel.setScaledContents(True)
        self.HelpLabel.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.HelpLabel.setIndent(1)
        self.HelpLabel.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.HelpLabel.setObjectName(_fromUtf8("HelpLabel"))
        self.gridLayout.addWidget(self.HelpLabel, 0, 1, 1, 1)
        self.ImageFrame = QtGui.QLabel(self.centralWidget)
        self.ImageFrame.setObjectName(_fromUtf8("ImageFrame"))
        self.gridLayout.addWidget(self.ImageFrame, 3, 0, 1, 1)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.textBrowser = QtGui.QTextBrowser(self.centralWidget)
        self.textBrowser.setEnabled(True)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 128, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 128, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 128, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 128, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 128, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 128, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 128, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 128, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 128, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.textBrowser.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.textBrowser.setFont(font)
        self.textBrowser.setStyleSheet(_fromUtf8("     background-color : black;\n"
"     color: green;\n"
"     border-style: outset;\n"
"     border-width: 1px;\n"
"     border-radius: 0px;\n"
"     font: bold 9px;\n"
"     min-width: 1em;\n"
"     padding: 0px;"))
        self.textBrowser.setFrameShape(QtGui.QFrame.VLine)
        self.textBrowser.setFrameShadow(QtGui.QFrame.Plain)
        self.textBrowser.setLineWidth(1)
        self.textBrowser.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.textBrowser.setTabStopWidth(80)
        self.textBrowser.setObjectName(_fromUtf8("textBrowser"))
        self.horizontalLayout.addWidget(self.textBrowser)
        self.gridLayout.addLayout(self.horizontalLayout, 3, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QtGui.QMenuBar(MainWindow)
        self.menuBar.setEnabled(True)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 703, 31))
        self.menuBar.setMaximumSize(QtCore.QSize(17000, 170))
        self.menuBar.setNativeMenuBar(False)
        self.menuBar.setObjectName(_fromUtf8("menuBar"))
        self.menuFile = QtGui.QMenu(self.menuBar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        self.menuOptions = QtGui.QMenu(self.menuBar)
        self.menuOptions.setObjectName(_fromUtf8("menuOptions"))
        self.menuParameters = QtGui.QMenu(self.menuOptions)
        self.menuParameters.setObjectName(_fromUtf8("menuParameters"))
        self.menuHelp = QtGui.QMenu(self.menuBar)
        self.menuHelp.setObjectName(_fromUtf8("menuHelp"))
        self.menuRun = QtGui.QMenu(self.menuBar)
        self.menuRun.setObjectName(_fromUtf8("menuRun"))
        MainWindow.setMenuBar(self.menuBar)
        self.statusBar = QtGui.QStatusBar(MainWindow)
        self.statusBar.setObjectName(_fromUtf8("statusBar"))
        MainWindow.setStatusBar(self.statusBar)
        self.toolBar = QtGui.QToolBar(MainWindow)
        self.toolBar.setEnabled(True)
        self.toolBar.setMinimumSize(QtCore.QSize(34, 0))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(180, 180, 180, 100))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(180, 180, 180, 100))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(180, 180, 180, 100))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(180, 180, 180, 100))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(180, 180, 180, 100))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(180, 180, 180, 100))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(180, 180, 180, 100))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(180, 180, 180, 100))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(180, 180, 180, 100))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.toolBar.setPalette(palette)
        self.toolBar.setStyleSheet(_fromUtf8(" background-color: rgba(180,180,180,100);\n"
"     border-style: outset;\n"
"     border-width: 0px;\n"
"     border-radius: 0px;\n"
"     border-color: beige;\n"
"     font: 14px;\n"
"     min-width: 2em;\n"
"     padding: 1\n"
"px;\n"
""))
        self.toolBar.setAllowedAreas(QtCore.Qt.NoToolBarArea)
        self.toolBar.setIconSize(QtCore.QSize(20, 20))
        self.toolBar.setObjectName(_fromUtf8("toolBar"))
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.actionOpen = QtGui.QAction(MainWindow)
        self.actionOpen.setCheckable(False)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/icones/open")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionOpen.setIcon(icon1)
        self.actionOpen.setIconVisibleInMenu(True)
        self.actionOpen.setObjectName(_fromUtf8("actionOpen"))
        self.actionCreate_new_project = QtGui.QAction(MainWindow)
        self.actionCreate_new_project.setCheckable(True)
        self.actionCreate_new_project.setEnabled(True)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8(":/icones/proj")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionCreate_new_project.setIcon(icon2)
        self.actionCreate_new_project.setObjectName(_fromUtf8("actionCreate_new_project"))
        self.actionSave_current_image = QtGui.QAction(MainWindow)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8(":/icones/picme")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSave_current_image.setIcon(icon3)
        self.actionSave_current_image.setIconVisibleInMenu(True)
        self.actionSave_current_image.setObjectName(_fromUtf8("actionSave_current_image"))
        self.actionQuit = QtGui.QAction(MainWindow)
        self.actionQuit.setObjectName(_fromUtf8("actionQuit"))
        self.actionReset_parameters = QtGui.QAction(MainWindow)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(_fromUtf8(":/icones/zoom")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionReset_parameters.setIcon(icon4)
        self.actionReset_parameters.setObjectName(_fromUtf8("actionReset_parameters"))
        self.actionReset_parameters_2 = QtGui.QAction(MainWindow)
        self.actionReset_parameters_2.setObjectName(_fromUtf8("actionReset_parameters_2"))
        self.actionShow_doc = QtGui.QAction(MainWindow)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(_fromUtf8(":/icones/info")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionShow_doc.setIcon(icon5)
        self.actionShow_doc.setIconVisibleInMenu(True)
        self.actionShow_doc.setObjectName(_fromUtf8("actionShow_doc"))
        self.actionZoom = QtGui.QAction(MainWindow)
        self.actionZoom.setObjectName(_fromUtf8("actionZoom"))
        self.actionRun_all = QtGui.QAction(MainWindow)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(_fromUtf8(":/icones/play")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionRun_all.setIcon(icon6)
        self.actionRun_all.setIconVisibleInMenu(True)
        self.actionRun_all.setObjectName(_fromUtf8("actionRun_all"))
        self.actionOpen_2 = QtGui.QAction(MainWindow)
        self.actionOpen_2.setIcon(icon1)
        self.actionOpen_2.setIconVisibleInMenu(True)
        self.actionOpen_2.setObjectName(_fromUtf8("actionOpen_2"))
        self.actionRun_all_2 = QtGui.QAction(MainWindow)
        self.actionRun_all_2.setIcon(icon6)
        self.actionRun_all_2.setIconVisibleInMenu(True)
        self.actionRun_all_2.setObjectName(_fromUtf8("actionRun_all_2"))
        self.actionStop = QtGui.QAction(MainWindow)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(_fromUtf8(":/icones/stop")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionStop.setIcon(icon7)
        self.actionStop.setObjectName(_fromUtf8("actionStop"))
        self.actionSave_current_image_2 = QtGui.QAction(MainWindow)
        self.actionSave_current_image_2.setCheckable(False)
        self.actionSave_current_image_2.setEnabled(True)
        self.actionSave_current_image_2.setIcon(icon3)
        self.actionSave_current_image_2.setIconVisibleInMenu(True)
        self.actionSave_current_image_2.setObjectName(_fromUtf8("actionSave_current_image_2"))
        self.actionHelp = QtGui.QAction(MainWindow)
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(_fromUtf8(":/icones/help")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionHelp.setIcon(icon8)
        self.actionHelp.setObjectName(_fromUtf8("actionHelp"))
        self.actionView_statistics = QtGui.QAction(MainWindow)
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap(_fromUtf8(":/icones/stat")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionView_statistics.setIcon(icon9)
        self.actionView_statistics.setObjectName(_fromUtf8("actionView_statistics"))
        self.actionCreate_new_project_2 = QtGui.QAction(MainWindow)
        self.actionCreate_new_project_2.setIcon(icon2)
        self.actionCreate_new_project_2.setIconVisibleInMenu(True)
        self.actionCreate_new_project_2.setObjectName(_fromUtf8("actionCreate_new_project_2"))
        self.actionHelp_2 = QtGui.QAction(MainWindow)
        self.actionHelp_2.setIcon(icon8)
        self.actionHelp_2.setIconVisibleInMenu(True)
        self.actionHelp_2.setObjectName(_fromUtf8("actionHelp_2"))
        self.actionStop_2 = QtGui.QAction(MainWindow)
        self.actionStop_2.setIcon(icon7)
        self.actionStop_2.setIconVisibleInMenu(True)
        self.actionStop_2.setObjectName(_fromUtf8("actionStop_2"))
        self.actionView_stats = QtGui.QAction(MainWindow)
        self.actionView_stats.setIcon(icon9)
        self.actionView_stats.setIconVisibleInMenu(True)
        self.actionView_stats.setObjectName(_fromUtf8("actionView_stats"))
        self.menuFile.addAction(self.actionCreate_new_project_2)
        self.menuFile.addAction(self.actionOpen_2)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionSave_current_image)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionQuit)
        self.menuParameters.addAction(self.actionReset_parameters_2)
        self.menuOptions.addAction(self.menuParameters.menuAction())
        self.menuHelp.addAction(self.actionShow_doc)
        self.menuHelp.addAction(self.actionHelp_2)
        self.menuRun.addAction(self.actionRun_all_2)
        self.menuRun.addAction(self.actionStop_2)
        self.menuRun.addAction(self.actionView_stats)
        self.menuBar.addAction(self.menuFile.menuAction())
        self.menuBar.addAction(self.menuRun.menuAction())
        self.menuBar.addAction(self.menuOptions.menuAction())
        self.menuBar.addAction(self.menuHelp.menuAction())
        self.toolBar.addAction(self.actionCreate_new_project)
        self.toolBar.addAction(self.actionOpen)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionRun_all)
        self.toolBar.addAction(self.actionStop)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionView_statistics)
        self.toolBar.addAction(self.actionSave_current_image_2)
        self.toolBar.addAction(self.actionReset_parameters)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionHelp)

        self.retranslateUi(MainWindow)
        self.ParamStack.setCurrentIndex(4)
        self.ParamStack.layout().setSpacing(0)
        QtCore.QObject.connect(self.RangeSlider, QtCore.SIGNAL(_fromUtf8("sliderMoved(int)")), self.RangeLCD.display)
        QtCore.QObject.connect(self.SpaceSlider, QtCore.SIGNAL(_fromUtf8("sliderMoved(int)")), self.SpaceLCD.display)
        QtCore.QObject.connect(self.actionOpen, QtCore.SIGNAL(_fromUtf8("triggered()")), self.OpenButton.click)
        QtCore.QObject.connect(self.actionOpen_2, QtCore.SIGNAL(_fromUtf8("triggered()")), self.OpenButton.click)
        QtCore.QObject.connect(self.actionCreate_new_project_2, QtCore.SIGNAL(_fromUtf8("triggered()")), self.actionCreate_new_project.trigger)
        QtCore.QObject.connect(self.actionHelp, QtCore.SIGNAL(_fromUtf8("triggered()")), self.actionHelp_2.trigger)
        QtCore.QObject.connect(self.actionStop_2, QtCore.SIGNAL(_fromUtf8("triggered()")), self.actionStop.trigger)
        QtCore.QObject.connect(self.actionView_stats, QtCore.SIGNAL(_fromUtf8("triggered()")), self.actionView_statistics.trigger)
        QtCore.QObject.connect(self.actionSave_current_image_2, QtCore.SIGNAL(_fromUtf8("triggered()")), self.actionSave_current_image.trigger)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "KTAROB", None))
        self.RegisterButton.setText(_translate("MainWindow", "Registering", None))
        self.OpenButton.setText(_translate("MainWindow", "...", None))
        self.SizeBox.setItemText(0, _translate("MainWindow", "694x462", None))
        self.SizeBox.setItemText(1, _translate("MainWindow", "1392x924", None))
        self.SizeBox.setItemText(2, _translate("MainWindow", "None", None))
        self.ParamStack.setItemText(self.ParamStack.indexOf(self.RegistWidget), _translate("MainWindow", "Registration and Resize", None))
        self.FilterWidget.setToolTip(_translate("MainWindow", "<html><head/><body><p><span style=\" font-style:italic;\">Filtering parameters</span></p></body></html>", None))
        self.FilterWidget.setWhatsThis(_translate("MainWindow", "<html><head/><body><p><span style=\" font-style:italic;\">Filtering parameters</span></p></body></html>", None))
        self.FilterButton.setText(_translate("MainWindow", "filter", None))
        self.ParamStack.setItemText(self.ParamStack.indexOf(self.FilterWidget), _translate("MainWindow", "Filtering", None))
        self.LightWidget.setToolTip(_translate("MainWindow", "<html><head/><body><p><span style=\" font-style:italic;\">Light correction parameters</span></p></body></html>", None))
        self.PolRButton.setText(_translate("MainWindow", "Polynomial", None))
        self.FreqRButton.setText(_translate("MainWindow", "Frequency", None))
        self.NoneRButton.setText(_translate("MainWindow", "None", None))
        self.CorrectButton.setText(_translate("MainWindow", "correct", None))
        self.ParamStack.setItemText(self.ParamStack.indexOf(self.LightWidget), _translate("MainWindow", "Light derive correction", None))
        self.SegmentWidget.setToolTip(_translate("MainWindow", "<html><head/><body><p><span style=\" font-style:italic;\">Segmenation choice</span></p></body></html>", None))
        self.comboBox.setItemText(0, _translate("MainWindow", "Segmentation process 1", None))
        self.comboBox.setItemText(1, _translate("MainWindow", "Segmentation process 2", None))
        self.comboBox.setItemText(2, _translate("MainWindow", "Segmentation process 3", None))
        self.comboBox.setItemText(3, _translate("MainWindow", "Segmentation Mamba", None))
        self.comboBox.setItemText(4, _translate("MainWindow", "Manual", None))
        self.SegementButton.setText(_translate("MainWindow", "segment", None))
        self.ParamStack.setItemText(self.ParamStack.indexOf(self.SegmentWidget), _translate("MainWindow", "Segmentation", None))
        self.comboBox_2.setItemText(0, _translate("MainWindow", "Bounding Box", None))
        self.comboBox_2.setItemText(1, _translate("MainWindow", "Moment Box", None))
        self.FitButton.setText(_translate("MainWindow", "fit", None))
        self.ParamStack.setItemText(self.ParamStack.indexOf(self.FitWidget), _translate("MainWindow", "Ellipse fitting", None))
        self.HelpLabel.setText(_translate("MainWindow", "Tips", None))
        self.ImageFrame.setText(_translate("MainWindow", "ImageFrame", None))
        self.menuFile.setTitle(_translate("MainWindow", "File", None))
        self.menuOptions.setTitle(_translate("MainWindow", "Options", None))
        self.menuParameters.setTitle(_translate("MainWindow", "Parameters", None))
        self.menuHelp.setTitle(_translate("MainWindow", "Help", None))
        self.menuRun.setTitle(_translate("MainWindow", "Run", None))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar", None))
        self.actionOpen.setText(_translate("MainWindow", "Open", None))
        self.actionOpen.setShortcut(_translate("MainWindow", "Ctrl+O", None))
        self.actionCreate_new_project.setText(_translate("MainWindow", "Create new project...", None))
        self.actionSave_current_image.setText(_translate("MainWindow", "Save current image", None))
        self.actionSave_current_image.setShortcut(_translate("MainWindow", "Ctrl+S", None))
        self.actionQuit.setText(_translate("MainWindow", "Quit", None))
        self.actionReset_parameters.setText(_translate("MainWindow", "Zoom +", None))
        self.actionReset_parameters_2.setText(_translate("MainWindow", "Reset parameters", None))
        self.actionShow_doc.setText(_translate("MainWindow", "Show doc", None))
        self.actionZoom.setText(_translate("MainWindow", "Zoom -", None))
        self.actionRun_all.setText(_translate("MainWindow", "Run all", None))
        self.actionOpen_2.setText(_translate("MainWindow", "Open", None))
        self.actionRun_all_2.setText(_translate("MainWindow", "Run all", None))
        self.actionStop.setText(_translate("MainWindow", "Stop", None))
        self.actionSave_current_image_2.setText(_translate("MainWindow", "Save current image", None))
        self.actionHelp.setText(_translate("MainWindow", "help", None))
        self.actionView_statistics.setText(_translate("MainWindow", "View statistics", None))
        self.actionCreate_new_project_2.setText(_translate("MainWindow", "Create new project", None))
        self.actionHelp_2.setText(_translate("MainWindow", "Help", None))
        self.actionStop_2.setText(_translate("MainWindow", "Stop", None))
        self.actionView_stats.setText(_translate("MainWindow", "View stats", None))

import icones_rc
