#!/usr/bin/python
# use a progress dialog from a thread
 
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import time,sys
 
STEPS=5
 
class MyThread(QThread):
   def __init__(self,parent):
      super(MyThread,self).__init__(parent)
      self.cancel = False
 
   def run (self):
      for i in range(STEPS):
         if self.cancel: break
         time.sleep(1)
         self.emit(SIGNAL("increment"))
         print "%d "%(i),
 
   @pyqtSignature("")
   def cancel(self):
      """SLOT to cancel treatment"""
      self.cancel = True
 
class MyAppli(QWidget):
   def __init__(self,parent=None):
      QWidget.__init__(self, parent)
      # create button to start the thread
      self.btnStart = QPushButton("Start",self)
      self.connect(self.btnStart, SIGNAL("clicked()"),
                   self,          SLOT("on_btnStart_clicked()"))
 
   @pyqtSignature("")
   def on_btnStart_clicked(self):
      """Start the treatment in the thread"""
      self.p = QProgressDialog("Running...","Stop",0,STEPS-1,self)
      self.th = MyThread(self)
      self.th.connect(self.th,SIGNAL("increment"),
                              self.incProgress)
      self.p.connect (self.p, SIGNAL("canceled()"),
                      self.th,SLOT("cancel()"))
      self.p.show()
      self.th.start()
 
   def incProgress(self):
      """Increment the progress dialog"""
      self.p.setValue(self.p.value()+1)
 
if __name__ == "__main__":
   app = QApplication(sys.argv)
   widget = MyAppli()
   widget.show()
   sys.exit(app.exec_())
