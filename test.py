# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'trying.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from PIL import ImageTk, Image
import sqlite
import sys

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

db = 'programs.db'

class Object():

    def __init__(self, id , name, vers, cmnd, updt, delt, imag, cat):
        self.id = id
        self.name = name
        self.version = vers
        self.img = imag
        self.command = cmnd
        self.delete = delt
        self.update = updt
        self.category = cat

class Ui_MainWindow(object):


    def setupUi(self, MainWindow):

        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(1366, 768)

        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))

        self.horizontalLayout = QtGui.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))

        # building categories section
        self.build_categories()

        # building programs section
        self.build_programs()

        # initial fill with programs
        self.categoryFilter(None)

        # buildint terminal section
        self.terminal_build()

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1366, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    # function to define structure for categories
    def build_categories(self):

        self.cateogries = QtGui.QFrame(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cateogries.sizePolicy().hasHeightForWidth())
        self.cateogries.setMinimumSize(QtCore.QSize(220, 0))
        self.cateogries.setFrameShape(QtGui.QFrame.StyledPanel)
        self.cateogries.setFrameShadow(QtGui.QFrame.Raised)
        self.cateogries.setObjectName(_fromUtf8("cateogries"))
        self.cateogries.setStyleSheet(_fromUtf8("background-color: qlineargradient(\n"
                                                "spread:pad, \n"
                                                "x1:0.1, y1:0.3, \n"
                                                "x2:0.7, y2:0.1, \n"
                                                "stop:0 lightgreen, stop:1 white);"))

        self.verticalLayout = QtGui.QVBoxLayout(self.cateogries)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))

        self.scrollArea = QtGui.QScrollArea(self.cateogries)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollArea.sizePolicy().hasHeightForWidth())
        self.scrollArea.setSizePolicy(sizePolicy)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName(_fromUtf8("scrollArea"))

        self.scrollAreaWidgetContents = QtGui.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 218, 657))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollAreaWidgetContents.sizePolicy().hasHeightForWidth())


        self.scrollAreaWidgetContents.setSizePolicy(sizePolicy)
        self.scrollAreaWidgetContents.setObjectName(_fromUtf8("scrollAreaWidgetContents"))

        self.verticalLayout_3 = QtGui.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))

        # get data from db and fill scrollbar with them
        self.category_object()

        spacerItem = QtGui.QSpacerItem(20, 570, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout.addWidget(self.scrollArea)
        self.horizontalLayout.addWidget(self.cateogries)

    # function do define look of a cateogry btn
    def category_object(self):
        # for child in ):
        #     print(child, 'child')

        cat_list = sqlite.get_categories(db)
        # for i in range(0,5):
        for item in cat_list:
            self.item = item
            im_path = item[2]

            # categoryFilter(item)
            btn = QtGui.QPushButton(self.scrollAreaWidgetContents)
            btn.setMinimumSize(QtCore.QSize(200, 0))
            btn.setObjectName('cat_btn')
            btn.setText(_fromUtf8(item[1]))
            btn.setStyleSheet(_fromUtf8("background-color: qlineargradient(spread:pad, x1:0.3, y1:0, x2:1, y2:0, stop:0 white , stop:1 lightgreen); text-align: left; padding-left:10px; font-weight:bold;"
                                        "padding-top:2px; padding-bottom:2px; border-radius:5px; border:1px solid green; "))
            btn.setIcon(QtGui.QIcon(im_path))
            btn.setIconSize(QtCore.QSize(40, 30))
            btn.clicked.connect(lambda event, item=self.item: self.categoryFilter(item))

            self.verticalLayout_3.addWidget(btn)

    # filter programms by categories
    def categoryFilter(self, param):
        tlist = []

        if param is None:
            prog_list = sqlite.get_programs_data(db, param)
        else:
            prog_list = sqlite.get_programs_data(db, param[0])

        # print('pl', prog_list)

        for j in prog_list:
            obj = Object(j[0], j[1], j[2], j[3], j[4], j[5], j[6], j[7])
            tlist.append(obj)

        self.program_object(tlist)

    # makes programm buttons on layout
    def build_programs(self):

        self.programs = QtGui.QFrame(self.centralwidget)
        self.programs.setStyleSheet(_fromUtf8("background-color: qlineargradient(\n"
                                                "spread:pad, \n"
                                                "x1:0.1, y1:0.3, \n"
                                                "x2:0.7, y2:0.1, \n"
                                                "stop:0 lightgreen, stop:1 white);"))

        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.programs.sizePolicy().hasHeightForWidth())

        self.programs.setSizePolicy(sizePolicy)
        self.programs.setMinimumSize(QtCore.QSize(0, 0))
        self.programs.setFrameShape(QtGui.QFrame.StyledPanel)
        self.programs.setFrameShadow(QtGui.QFrame.Raised)
        self.programs.setObjectName(_fromUtf8("programs"))
        self.gridLayout = QtGui.QGridLayout(self.programs)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.scrollArea_2 = QtGui.QScrollArea(self.programs)

        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)

        sizePolicy.setHeightForWidth(self.scrollArea_2.sizePolicy().hasHeightForWidth())
        self.scrollArea_2.setSizePolicy(sizePolicy)
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollArea_2.setObjectName(_fromUtf8("scrollArea_2"))

        self.scrollAreaWidgetContents_2 = QtGui.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 661, 657))
        self.scrollAreaWidgetContents_2.setObjectName(_fromUtf8("scrollAreaWidgetContents_2"))

        self.gridLayout_2 = QtGui.QGridLayout(self.scrollAreaWidgetContents_2)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))

        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem1, 3, 2, 1, 1)
        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)
        self.gridLayout.addWidget(self.scrollArea_2, 2, 3, 1, 2)
        self.horizontalLayout.addWidget(self.programs)

    # defines look of program button
    def program_object(self, objects):


        childs = self.scrollAreaWidgetContents_2.findChildren(QtGui.QPushButton)
        for child in childs:
            child.setParent(None)

        cc = 0
        cr = 0
        for object in objects:
            program = QtGui.QPushButton(self.scrollAreaWidgetContents_2)
            sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Minimum)
            sizePolicy.setHorizontalStretch(0)
            sizePolicy.setVerticalStretch(0)
            sizePolicy.setHeightForWidth(program.sizePolicy().hasHeightForWidth())
            program.setSizePolicy(sizePolicy)
            program.setMinimumSize(QtCore.QSize(80, 80))

            stil = "border-image:url(%s); background-repeat: no-repeat;" % (object.img)
            program.setStyleSheet(_fromUtf8(stil))
            program.setText(_fromUtf8(""))
            program.setObjectName(_fromUtf8("pushButton_6"))
            self.gridLayout_2.addWidget(program, cr, cc, 1, 1)
            cc += 1
            if cc == 6:
                cc = 0
                cr += 1

    #function to define terminal output
    def terminal_build(self):

        self.terminal = QtGui.QFrame(self.centralwidget)

        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.terminal.sizePolicy().hasHeightForWidth())

        self.terminal.setSizePolicy(sizePolicy)
        self.terminal.setMinimumSize(QtCore.QSize(300, 0))
        self.terminal.setMaximumSize(QtCore.QSize(400, 16777215))
        self.terminal.setFrameShape(QtGui.QFrame.StyledPanel)
        self.terminal.setFrameShadow(QtGui.QFrame.Raised)
        self.terminal.setObjectName(_fromUtf8("terminal"))

        self.verticalLayout_2 = QtGui.QVBoxLayout(self.terminal)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))

        self.textEdit = QtGui.QTextEdit(self.terminal)

        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textEdit.sizePolicy().hasHeightForWidth())

        self.textEdit.setSizePolicy(sizePolicy)
        self.textEdit.setStyleSheet(_fromUtf8("background-color: rgb(85, 0, 127); color: rgb(255, 255, 255);"))
        self.textEdit.setObjectName(_fromUtf8("textEdit"))

        self.verticalLayout_2.addWidget(self.textEdit)
        self.horizontalLayout.addWidget(self.terminal)


    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        # self.pushButton_2.setText(_translate("MainWindow", "PushButton", None))
        # self.pushButton_3.setText(_translate("MainWindow", "PushButton", None))
        # self.pushButton.setText(_translate("MainWindow", "PushButton", None))
        self.textEdit.setToolTip(_translate("MainWindow", "Terminal output", None))
        self.textEdit.setWhatsThis(_translate("MainWindow", "Terminal otuput", None))
        self.textEdit.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">rewrwerew</p></body></html>", None))


    # def pil_image(self, path, x, y):
    # # return image object with custom size, mainly for buttons
    #     try:
    #         imagen = Image.open(path)
    #         imagen = imagen.resize((x, y), Image.ANTIALIAS)
    #         img = ImageTk.PhotoImage(imagen)
    #         return img
    #     except:
    #         imagen = Image.open('imgs/required/default.jpg')
    #         imagen = imagen.resize((x, y), Image.ANTIALIAS)
    #         img = ImageTk.PhotoImage(imagen)
    #         return img



if __name__ == "__main__":

    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
