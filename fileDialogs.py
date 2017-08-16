__author__ = 'atana'

from PyQt4 import QtCore, QtGui

class fileDialog(QtGui.QWidget):

    def __init__(self, parent=None):
        super(fileDialog, self).__init__(parent)
        self.fname = QtGui.QFileDialog.getOpenFileName(self, 'Open file', 'c:\\', "Image files(*.jpg *.gif *.png)")
        self.setWindowModality(QtCore.Qt.ApplicationModal)


    def getPath(self):
        return self.fname