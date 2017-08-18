#!/usr/bin/env python3
from PyQt4 import QtGui
from PyQt4 import QtCore
import sys
import CPUsUI
import psutil



s = None
class Window(QtGui.QMainWindow,CPUsUI.Ui_MainWindow ):
    def __init__(self,parent=None):
        super(Window, self).__init__(parent)
        self.setupUi(self)

        self.thrClass = ThrClass()
        self.thrClass.start()
        #self.connect(self.thrClass, QtCore.SIGNAL('CPU'), self.updateProgressBar)
        self.connect(self.thrClass, QtCore.SIGNAL('CPU'), self.updateCPU)
        #self.connect(self.thrClass, QtCore.SIGNAL('HUM'), self.updateHUM)

    def updateCPU(self, ans):

	    for i in range(len(ans)):
                if i == 0:
                    val = str(ans[i])+"%"
                    #self.setFormat('%.02f%%' % (self.prefixFloat))
                    self.c1.setFormat('%.02f%%' % (ans[i]))
                    self.c1.setValue(ans[i])
                elif i == 1:
                    #val = str(ans[i]) + "%"
                    #self.c1.setFormat(val)
                    self.c2.setFormat('%.02f%%' % (ans[i]))
                    self.c2.setValue(ans[i])
                elif i == 2:
                    #val = str(ans[i]) + "%"
                    #self.c1.setFormat(val)
                    self.c3.setFormat('%.02f%%' % (ans[i]))
                    self.c3.setValue(ans[i])
                elif i == 3:
                    #val = str(ans[i]) + "%"
                    #self.c1.setFormat(val)
                    self.c4.setFormat('%.02f%%' % (ans[i]))
                    self.c4.setValue(ans[i])
                elif i == 4:
                    self.RAM.setFormat('%.02f%%'%(ans[i]))
                    self.RAM.setValue(ans[i])
                else:
                    print ('nothing')

    

class ThrClass(QtCore.QThread):
   


    def __init__(self, parent=None):
        super(ThrClass,self).__init__(parent)
   


    def run(self):
        last = 0
        lasthum = 0
        while True:
            ans = psutil.cpu_percent(interval=1, percpu=True)
            ans.append(psutil.virtual_memory()[2])
            print (ans)
            self.emit(QtCore.SIGNAL('CPU'), ans)


	    	
           
app = QtGui.QApplication(sys.argv)
gui = Window()
gui.show()
sys.exit(app.exec())
