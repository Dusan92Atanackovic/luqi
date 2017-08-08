# -*- coding: utf-8 -*-

from PyQt4 import QtCore, QtGui
from PIL import ImageTk, Image
from shutil import copyfile
import sqlite
import time
import hashlib
import sys, os

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
ui = None
style_lg_w = (_fromUtf8("background-color: qlineargradient(spread:pad,x1:0.1, y1:0.3, x2:0.7, y2:0.1, stop:0 lightgreen, stop:1 white);"))
style_lg_w_b = (_fromUtf8("background-color: qlineargradient(spread:pad,x1:0.1, y1:0.3, x2:0.7, y2:0.1, stop:0 lightgreen, stop:1 white); border:1px solid darkgreen;"))


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


class fileDialogDemo(QtGui.QWidget):

    def __init__(self, parent=None):
        super(fileDialogDemo, self).__init__(parent)
        self.fname = QtGui.QFileDialog.getOpenFileName(self, 'Open file', 'c:\\', "Image files(*.jpg *.gif *.png)")
        self.setWindowModality(QtCore.Qt.ApplicationModal)


    def getPath(self):
        return self.fname


class uiMainWindow(object):


    def setupUi(self, MainWindow):
        self.MainWindow = MainWindow
        self.MainWindow.setObjectName(_fromUtf8("LUQI"))
        self.MainWindow.resize(1366, 768)

        # self.mdi = QtGui.QMdiArea(MainWindow)

        self.centralwidget = QtGui.QWidget(self.MainWindow)
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


        self.MainWindow.setCentralWidget(self.centralwidget)

        self.menubar = QtGui.QMenuBar(self.MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1246, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))

        self.menuOptions = QtGui.QMenu(self.menubar)
        self.menuOptions.setObjectName(_fromUtf8("menuOptions"))

        self.menuGit = QtGui.QMenu(self.menubar)
        self.menuGit.setObjectName(_fromUtf8("menuGit"))

        self.menuInstalations = QtGui.QMenu(self.menubar)
        self.menuInstalations.setObjectName(_fromUtf8("menuInstalations"))

        self.MainWindow.setMenuBar(self.menubar)


        self.actionAdd_category = QtGui.QAction(self.MainWindow)
        self.actionAdd_category.setObjectName(_fromUtf8("actionAdd_category"))
        self.actionAdd_category.setShortcut('Ctrl+Shift+c')

        self.actionAdd_programs = QtGui.QAction(self.MainWindow)
        self.actionAdd_programs.setObjectName(_fromUtf8("actionAdd_programs"))
        self.actionAdd_programs.setShortcut('Ctrl+Shift+p')

        self.actionQuit = QtGui.QAction(self.MainWindow)
        self.actionQuit.setObjectName(_fromUtf8("actionQuit"))
        self.actionQuit.setShortcut('Ctrl+Shift+q')

        self.menuOptions.addAction(self.actionAdd_category)
        self.menuOptions.addAction(self.actionAdd_programs)

        self.menuOptions.addSeparator()
        self.menuOptions.addAction(self.actionQuit)

        self.menubar.addAction(self.menuOptions.menuAction())
        self.menubar.addAction(self.menuInstalations.menuAction())
        self.menubar.addAction(self.menuGit.menuAction())

        self.menubar.triggered[QtGui.QAction].connect(self.showdialog)


        self.statusbar = QtGui.QStatusBar(self.MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        self.MainWindow.setStatusBar(self.statusbar)


        self.retranslateUi(self.MainWindow)
        QtCore.QMetaObject.connectSlotsByName(self.MainWindow)

    # ************************ CATEGORIES BLOCK **********************

    # function to define structure for categories
    def build_categories(self):
        # structure :
        # Frame                                         self.categories
        #   > ScrollArea                                self.scrollArea
        #       > Widget (ScrollAreaContent)            self.scrollAreaWidgetContent
        #           > Frame                             self.catContainer
        #               > category objects (Buttons)    function

        self.cateogries = QtGui.QFrame(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cateogries.sizePolicy().hasHeightForWidth())
        self.cateogries.setMinimumSize(QtCore.QSize(220, 0))
        self.cateogries.setFrameShape(QtGui.QFrame.StyledPanel)
        self.cateogries.setFrameShadow(QtGui.QFrame.Raised)
        self.cateogries.setObjectName(_fromUtf8("cateogries"))
        self.cateogries.setStyleSheet(style_lg_w)

        self.verticalLayout = QtGui.QVBoxLayout(self.cateogries)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))

        # ---------------------------    block --------------------------------------------------- #

        self.scrollArea = QtGui.QScrollArea(self.cateogries)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollArea.sizePolicy().hasHeightForWidth())
        self.scrollArea.setSizePolicy(sizePolicy)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName(_fromUtf8("scrollArea"))
        self.scrollArea.setStyleSheet('border:0px;')

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

        # ---------------------------    block --------------------------------------------------- #

        self.catContainer = QtGui.QFrame(self.scrollAreaWidgetContents)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.catContainer.sizePolicy().hasHeightForWidth())
        self.catContainer.setSizePolicy(sizePolicy)
        self.catContainer.setFrameShape(QtGui.QFrame.StyledPanel)
        self.catContainer.setFrameShadow(QtGui.QFrame.Raised)
        self.catContainer.setObjectName(_fromUtf8("frame"))
        self.catContainer.setStyleSheet('border:0px;')

        self.gridLayout_4 = QtGui.QGridLayout(self.catContainer)
        self.gridLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))

        # ---------------------------    block --------------------------------------------------- #

        # get categories from db and fill scrollbar with them
        self.reBuildCategories()

        # ---------------------------    block --------------------------------------------------- #

        self.verticalLayout_3.addWidget(self.catContainer)
        spacerItem = QtGui.QSpacerItem(20, 570, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem)

        # ---------------------------    block --------------------------------------------------- #

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout.addWidget(self.scrollArea)
        self.horizontalLayout.addWidget(self.cateogries)


    def reBuildCategories(self):

        childs = self.catContainer.findChildren(QtGui.QPushButton)

        for child in childs:
            child.setParent(None)

        cat_list = sqlite.get_categories(db)

        cr = 0
        for item in cat_list:
            self.category_object(item, cr)
            cr += 1


    # function do define look of  cateogry btn
    def category_object(self, item, cr):

        self.item = item
        im_path = item[2]

        # categoryFilter(item)
        btn = QtGui.QPushButton(self.catContainer)
        btn.setMinimumSize(QtCore.QSize(200, 0))
        btn.setObjectName('cat_btn')
        btn.setText(_fromUtf8(item[1]))
        btn.setStyleSheet(_fromUtf8("background-color: qlineargradient(spread:pad, x1:0.3, y1:0, x2:1, y2:0, stop:0 white , stop:1 lightgreen); text-align: left; padding-left:10px; font-weight:bold;"
                                    "padding-top:2px; padding-bottom:2px;  border:1px solid green; "))
        btn.setIcon(QtGui.QIcon(im_path))
        btn.setIconSize(QtCore.QSize(40, 30))
        btn.clicked.connect(lambda event, item=self.item: self.categoryFilter(item))

        self.gridLayout_4.addWidget(btn, cr, 0)


    # filter programms by categories
    def categoryFilter(self, param):
        tlist = []

        if param is None:
            prog_list = sqlite.get_programs_data(db, param)
        else:
            prog_list = sqlite.get_programs_data(db, param[0])

        for j in prog_list:
            obj = Object(j[0], j[1], j[2], j[3], j[4], j[5], j[6], j[7])
            tlist.append(obj)

        self.program_object(tlist)


    # ************************ PROGRAMS BLOCK ************************

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

    # ************************ TERMINAL BLOCK *************************

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

    # ****************************************************************

    # makes popup forms
    def showdialog(self, a):

        command = a.text()
        print(command)
        if(command == 'add category'):
            # try:
                acf = addCategoryForm()
                acf.setupUi()
                acf.Form.show()
                acf.Form.exec_()
            # except:
            #     pass

        elif(command == 'add programs'):

            d = QtGui.QDialog()
            b1 = QtGui.QPushButton("programs", d)
            b1.move(50, 50)
            d.setWindowTitle("Dialog")
            d.setWindowModality(QtCore.Qt.ApplicationModal)
            d.exec_()


        elif(command == 'Quit'):
            sys.exit(0)


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
        self.menuOptions.setTitle(_translate("MainWindow", "options", None))
        self.menuGit.setTitle(_translate("MainWindow", "git", None))
        self.menuInstalations.setTitle(_translate("MainWindow", "instalations", None))
        self.actionAdd_category.setText(_translate("MainWindow", "add category", None))
        self.actionAdd_programs.setText(_translate("MainWindow", "add programs", None))
        self.actionQuit.setText(_translate("MainWindow", "Quit", None))


class addCategoryForm(object):


    def setupUi(self):
        # structure:
        #   Dialog                                      self.Form
        #       > ScrollArea                            self.scrollArea
        #           > ScrollareaContentWidget           self.scrollAreaContentWidget
        #               > Frame                         self.frame
        #                   > objects (entry and btn)
        #       > Frame                                 self.frame_2
        #           > objects (entry and 3 btns)        reBuildCAtegories function

        self.Form = QtGui.QDialog()
        Form = self.Form
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(504, 550)
        self.verticalLayout = QtGui.QVBoxLayout(Form)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))

        # ------------------------------------  block ------------------------------------------------- #

        self.scrollArea = QtGui.QScrollArea(self.Form)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollArea.sizePolicy().hasHeightForWidth())
        self.scrollArea.setSizePolicy(sizePolicy)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName(_fromUtf8("scrollArea"))
        self.scrollArea.setStyleSheet('border:0px;')

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

        # ------------------------------------  block ------------------------------------------------- #

        self.frame = QtGui.QFrame(self.scrollAreaWidgetContents)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setMinimumSize(QtCore.QSize(0, 50))
        self.frame.setStyleSheet(_fromUtf8("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0  lightgreen, stop:1 white);"))
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.frame.setStyleSheet(style_lg_w_b)

        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.frame)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))

        # ------------------------------------  block ------------------------------------------------- #
        # entry and btn for adding categories

        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))

        self.lineEdit = QtGui.QLineEdit(self.frame)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.lineEdit.setStyleSheet("background-color: white;")
        # self.lineEdit.keyReleaseEvent = self.handleKeyRelease
        self.horizontalLayout.addWidget(self.lineEdit)

        self.pushButton = QtGui.QPushButton(self.frame)
        self.pushButton.setMinimumSize(QtCore.QSize(50, 0))
        self.pushButton.setStyleSheet(_fromUtf8("border-image: url(imgs/required/btns/add.png);background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 white, stop:1 white);"))
        self.pushButton.setText(_fromUtf8(""))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.pushButton.clicked.connect(lambda event: self._insertIntoCategories(db, self.lineEdit))
        self.horizontalLayout.addWidget(self.pushButton)

        self.horizontalLayout_2.addLayout(self.horizontalLayout)

        # ------------------------------------  block ------------------------------------------------- #

        self.frame_2 = QtGui.QFrame(self.scrollAreaWidgetContents)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setStyleSheet(_fromUtf8("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 lightgreen, stop:1 white);"))
        self.frame_2.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_2.setObjectName(_fromUtf8("frame_2"))
        self.frame_2.setStyleSheet(style_lg_w_b)

        self.verticalLayout_2 = QtGui.QVBoxLayout(self.frame_2)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))

        self.reBuildCategories()

        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)


        # ------------------------------------  block ------------------------------------------------- #

        self.verticalLayout_3.addWidget(self.frame)
        self.verticalLayout_3.addWidget(self.frame_2)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout.addWidget(self.scrollArea)

         # ------------------------------------  block ------------------------------------------------- #

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        Form.setWindowModality(QtCore.Qt.ApplicationModal)


    def single_category_object(self, item):

        self.frame_3 = QtGui.QFrame(self.frame_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy)
        self.frame_3.setStyleSheet(_fromUtf8("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 lightgreen, stop:1 white);"))
        self.frame_3.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_3.setObjectName(_fromUtf8("frame_3"))
        self.frame_3.setStyleSheet('border:1px solid darkgreen;')

        self.horizontalLayout_3 = QtGui.QHBoxLayout(self.frame_3)
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))

        # ------------------------------------  block ------------------------------------------------- #

        self.lineEdit_2 = QtGui.QLineEdit(self.frame_3)
        self.lineEdit_2.setText(item[1])

        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_2.sizePolicy().hasHeightForWidth())
        self.lineEdit_2.setSizePolicy(sizePolicy)
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.lineEdit_2.setStyleSheet('background-color:white;')

        self.horizontalLayout_3.addWidget(self.lineEdit_2)

        # ------------------------------------  block ------------------------------------------------- #

        self.pushButton_4 = QtGui.QPushButton(self.frame_3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_4.sizePolicy().hasHeightForWidth())
        self.pushButton_4.setSizePolicy(sizePolicy)
        self.pushButton_4.setStyleSheet(_fromUtf8("border-image: url(imgs/required/btns/edit.jpg);background-color: transparent;"))
        self.pushButton_4.setText(_fromUtf8(""))
        self.pushButton_4.setObjectName(_fromUtf8("pushButton_4"))
        self.pushButton_4.clicked.connect(lambda event, id=item[0], le=self.lineEdit_2: self.modal('edit', 'Are you sure you want to rename this category ?', id, le))

        # ------------------------------------  block ------------------------------------------------- #

        self.horizontalLayout_3.addWidget(self.pushButton_4)
        self.pushButton_3 = QtGui.QPushButton(self.frame_3)
        self.pushButton_3.setStyleSheet(_fromUtf8("border-image: url(imgs/required/btns/ch_pic.png); background-color: transparent;"))
        self.pushButton_3.setText(_fromUtf8(""))
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.pushButton_3.clicked.connect(lambda event, id=item[0]: self.__chIcon(id))
        self.horizontalLayout_3.addWidget(self.pushButton_3)

        # ------------------------------------  block ------------------------------------------------- #

        self.pushButton_2 = QtGui.QPushButton(self.frame_3)
        self.pushButton_2.setStyleSheet(_fromUtf8("border-image: url(imgs/required/btns/cancel.png);background-color: transparent;"))
        self.pushButton_2.setText(_fromUtf8(""))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.pushButton_2.clicked.connect(lambda event, id=item[0], le=self.lineEdit_2: self.modal('delete', 'Are you sure you want to delete this category ?', id, le))
        self.horizontalLayout_3.addWidget(self.pushButton_2)

        self.verticalLayout_2.addWidget(self.frame_3)


    def modal(self, switch, message, category_id, entry):

        confirm = QtGui.QMessageBox()
        confirm.setWindowTitle("Confirm action")
        confirm.setText(message)

        btnYes = confirm.addButton("Yes", QtGui.QMessageBox.YesRole)
        btnYes.clicked.connect(lambda event: self.__getAns(True))

        btnNo = confirm.addButton("No", QtGui.QMessageBox.NoRole)
        btnNo.clicked.connect(lambda event: self.__getAns(False))

        confirm.setDefaultButton(btnYes)
        confirm = confirm.exec_()

        if self.ans is True:
            if switch == 'edit':
                self.__editCategory(category_id, entry)

            if switch == 'delete':
                self.__delCategory(category_id)


    def reBuildCategories(self):

        global ui

        childs = self.frame_2.findChildren(QtGui.QFrame)

        for child in childs:
            child.setParent(None)

        cat_list = sqlite.get_categories(db)

        for item in cat_list:
            self.single_category_object(item)

        ui.reBuildCategories()

    # ------------------------------- db actions -----------------------------------------

    def _insertIntoCategories(self, db, le):

        var = le.text()
        var2 = var.title()
        ans = False

        if len(var2) > 0:
            ans = sqlite.insert_into_categories(db, var2)
            le.setText('')

        if ans is True:
            self.reBuildCategories()
            print( 'neki toaster ovde')
        else:
            print("insertInto cateogires error" , ans)


    def __getAns(self, param):
        self.ans =  param


    def __editCategory(self, category_id, entry):
        response = sqlite.update_category_name(db, category_id, entry)

        if response is True:
            self.reBuildCategories()
            print(' neki toaster ako bi mogao')
        else:
            print( 'ima greska, error', response)


    def __delCategory(self, category_id):

        response = sqlite.remove_category(db, category_id)
        if response is True:
            self.reBuildCategories()
            print(' neki toaster ako bi mogao')
        else:
            print( 'ima greska, error', response)


    def __chIcon(self, id):
        '''
        1 - file chooser
        2 - proveriti da li je fajl u luqi/imgs folderu
        3 - ako nije modal - da li da napravi kopiju tamo
        4 - ako jeste ,sqlite fja
        '''
        # fp = '/home/atana/Documents/python projects/luqi/luqi/imgs/audacious.jpg'
        # fp = '/home/atana/Pictures/download.jpg'

        file_path = fileDialogDemo()
        fp = file_path.getPath()
        # print( 'fp', type(fp))

        # check if correct path is  chosen
        if_exist = os.path.isfile(fp)
        # print('if exist', if_exist)

        if if_exist == True:
            cwd = os.getcwd() + '/imgs/required'
            img_dir, fileName = os.path.split(fp)

            if cwd == img_dir:
                # print('1')
                sqlite.update_category(db, id, fp)

            else:
                # print('2')
                dst = cwd + '/' + fileName
                if_exist = os.path.isfile(dst)

                if if_exist == True:
                    # print('3')
                    # if file alredy exists
                    # split it in name and extension
                    index = fileName.index('.')
                    name = fileName[:index]
                    extension = fileName[index:]

                    # make time variable
                    timeMaked = time.strftime("%c")
                    # hash the time
                    hash = hashlib.md5(timeMaked.encode()).hexdigest()

                    # add hash to file name to avoid overwriting the file
                    new_dst = cwd + '/' + name + '.' + hash + '.' + extension
                    copyfile(fp, new_dst)

                else:
                    # print('4')
                    copyfile(fp, dst)

                sqlite.update_category(db, id, dst)


            self.reBuildCategories()

    # --------------------------------  block  -------------------------------------


    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.pushButton_4.setToolTip(_translate("Form", "<html><head/><body><p>rename</p></body></html>", None))
        self.pushButton_3.setToolTip(_translate("Form", "<html><head/><body><p>picture</p></body></html>", None))
        self.pushButton_2.setToolTip(_translate("Form", "<html><head/><body><p>delete</p></body></html>", None))
        self.pushButton_2.setWhatsThis(_translate("Form", "<html><head/><body><p>delete</p></body></html>", None))


def main():
    try:
        global ui

        app = QtGui.QApplication(sys.argv)
        MainWindow = QtGui.QMainWindow()
        ui = uiMainWindow()
        ui.setupUi(MainWindow)
        MainWindow.show()

        sys.exit(app.exec_())
    except Exception as e:
        print('exception in main' , e)

if __name__ == "__main__":
    main()
