'''
Created on Mar 28, 2013

@author: sob016

'''
from PyQt4 import  QtGui
#from PyQt4 import QtCore, QtGui
#from DataAccess.PCA import PCA
import Interface
#from Interface.MyMainGUI import MyMainWindow, getMainPage
from Interface.MyMainGUI import getMainPage
import sys

if __name__ == "__main__":
 
    
    app = QtGui.QApplication(sys.argv)
    Interface.MyMainGUI.getMainPage().show()
    sys.exit(app.exec_())

