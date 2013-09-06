


import sys

from PyQt4.QtCore import QObject,\
                         pyqtSignal

from PyQt4.QtGui import QDialog, \
                        QVBoxLayout, \
                        QPushButton, \
                        QTextBrowser,\
                        QApplication


class TermStream(QObject):
    _stdout = None
    _stderr = None

    messageWritten = pyqtSignal(str)

    def flush( self ):
        pass

    def fileno( self ):
        return -1

    def write( self, msg ):
        if ( not self.signalsBlocked() ):
            self.messageWritten.emit(unicode(msg))

    @staticmethod
    def stdout():
        if ( not TermStream._stdout ):
            TermStream._stdout = TermStream()
            sys.stdout = TermStream._stdout
        return TermStream._stdout

    @staticmethod
    def stderr():
        if ( not TermStream._stderr ):
            TermStream._stderr = TermStream()
            sys.stderr = TermStream._stderr
        return TermStream._stderr

