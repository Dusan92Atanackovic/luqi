# -*- coding: utf-8 -*-

from PyQt4 import QtCore, QtGui
from categoryForm import addCategoryForm
from programsForm import programsFormClass
import sqlite
import fileDialogs as fd
import sys, os
import globalVars

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


ui = None


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
        self.cateogries.setStyleSheet(globalVars.style_lg_w)

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

        cat_list = sqlite.get_categories(globalVars.db)

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
        if param is None or param[1] == 'All':
            prog_list = sqlite.get_programs_data(globalVars.db, None)
        else:
            prog_list = sqlite.get_programs_data(globalVars.db, param[0])

        for j in prog_list:
            obj = Object(j[0], j[1], j[2], j[3], j[4], j[5], j[6], j[7])
            tlist.append(obj)

        self.program_object(tlist)


    # ************************ PROGRAMS BLOCK ************************

    # makes program buttons on layout
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
            program.clicked.connect(lambda event, obj=object: self.showProgramPopUp(obj))
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
        global ui
        command = a.text()

        if(command == 'add category'):
            acf = addCategoryForm(ui)
            acf.setupUi()
            acf.Form.show()

        elif(command == 'add programs'):

            d = QtGui.QDialog()
            b1 = QtGui.QPushButton("programs", d)
            b1.move(50, 50)
            d.setWindowTitle("Dialog")
            d.setWindowModality(QtCore.Qt.ApplicationModal)
            d.exec_()

        elif(command == 'Quit'):
            sys.exit(0)


    def showProgramPopUp(self, program):

        try:
            self.pform = programsFormClass(ui, program)
            self.pform.setupUi()
            self.pform.Form.show()

        except Exception as e:
            print (e, ' error in showProgramPopUp')


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
        print('exception in function main(), luqi.py' , e)

if __name__ == "__main__":
    main()
