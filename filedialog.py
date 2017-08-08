__author__ = 'atana'


import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *

class filedialogdemo(QWidget):

    def __init__(self, parent=None):
        super(filedialogdemo, self).__init__(parent)

        fname = QFileDialog.getOpenFileName(self, 'Open file', 'c:\\', "Image files(*.jpg *.gif *.png)")
        return fname




def main():
    app = QApplication(sys.argv)
    ex = filedialogdemo()
    ex.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()