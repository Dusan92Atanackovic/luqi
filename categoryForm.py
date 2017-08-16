__author__ = 'atana'

from PyQt4 import QtCore, QtGui
import globalVars as gv
from shutil import copyfile
import sqlite
import time
import hashlib
import os
import fileDialogs as fd



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



class addCategoryForm(object):

    def __init__(self, ui):
        self.ui = ui


    def setupUi(self):
        # structure:
        #   Dialog                                      self.Form
        #       > ScrollArea                            self.scrollArea
        #           > ScrollareaContentWidget           self.scrollAreaContentWidget
        #               > Frame                         self.frame
        #                   > objects (entry and btn)
        #       > Frame                                 self.frame_2
        #           > objects (entry and 3 btns)        reBuildCAtegories function

        self.Form = QtGui.QWidget()
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
        self.frame.setStyleSheet(gv.style_lg_w_b)

        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.frame)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))

        # ------------------------------------  block ------------------------------------------------- #
        # entry and btn for adding categories

        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))

        self.lineEdit = QtGui.QLineEdit(self.frame)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.lineEdit.setStyleSheet("background-color: white;")
        self.lineEdit.keyReleaseEvent = self.handleKeyRelease
        self.horizontalLayout.addWidget(self.lineEdit)

        self.pushButton = QtGui.QPushButton(self.frame)
        self.pushButton.setMinimumSize(QtCore.QSize(50, 0))
        self.pushButton.setStyleSheet(_fromUtf8("border-image: url(%s);background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 white, stop:1 white);") % gv.add)
        self.pushButton.setText(_fromUtf8(""))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.pushButton.clicked.connect(lambda event: self._insertIntoCategories(gv.db, self.lineEdit))
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
        self.frame_2.setStyleSheet(gv.style_lg_w_b)

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
        self.pushButton_4.setStyleSheet(_fromUtf8("border-image: url(%s);background-color: transparent;") % gv.edit)
        self.pushButton_4.setText(_fromUtf8(""))
        self.pushButton_4.setObjectName(_fromUtf8("pushButton_4"))
        self.pushButton_4.clicked.connect(lambda event, id=item[0], le=self.lineEdit_2: self.modal('edit', 'Are you sure you want to rename this category ?', id, le))

        # ------------------------------------  block ------------------------------------------------- #

        self.horizontalLayout_3.addWidget(self.pushButton_4)
        self.pushButton_3 = QtGui.QPushButton(self.frame_3)
        self.pushButton_3.setStyleSheet(_fromUtf8("border-image: url(%s); background-color: transparent;") % gv.ch_pic)
        self.pushButton_3.setText(_fromUtf8(""))
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.pushButton_3.clicked.connect(lambda event, id=item[0]: self.__chIcon(id))
        self.horizontalLayout_3.addWidget(self.pushButton_3)

        # ------------------------------------  block ------------------------------------------------- #

        self.pushButton_2 = QtGui.QPushButton(self.frame_3)
        self.pushButton_2.setStyleSheet(_fromUtf8("border-image: url(%s);background-color: transparent;") % gv.cancel)
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


        childs = self.frame_2.findChildren(QtGui.QFrame)

        for child in childs:
            child.setParent(None)

        cat_list = sqlite.get_categories(gv.db)

        for item in cat_list:
            self.single_category_object(item)

        self.ui.reBuildCategories()


    def handleKeyRelease(self, event):
        # print('key release:', event.key(), type(event.key()))
        QtGui.QLineEdit.keyReleaseEvent(self.lineEdit, event)
        if event.key() == 16777220:
            self._insertIntoCategories(gv.db, self.lineEdit)

    # ------------------------------- db actions -----------------------------------------

    def __getAns(self, param):
        self.ans =  param


    def _insertIntoCategories(self, db, le):

        var = le.text()
        var2 = var.title()

        if len(var2) > 0:
            ans = sqlite.insert_into_categories(db, var2)
            le.setText('')

            if ans is True:
                self.reBuildCategories()
                self.ui.statusbar.showMessage('Success, new category has been added', 3000)
            else:
                self.ui.statusbar.showMessage(str(ans), 3000)
        else:
            self.ui.statusbar.showMessage('Category can not be empty string', 3000)


    def __editCategory(self, category_id, entry):
        response = sqlite.update_category_name(gv.db, category_id, entry)

        if response is True:
            self.reBuildCategories()
            self.ui.statusbar.showMessage('Success, category has been updated', 3000)
        else:
            self.ui.statusbar.showMessage(str(response), 3000)


    def __delCategory(self, category_id):

        response = sqlite.remove_category(gv.db, category_id)
        if response is True:
            self.reBuildCategories()
            self.ui.statusbar.showMessage('Success, category has been deleted', 3000)
        else:
            self.ui.statusbar.showMessage(str(response), 3000)


    def __chIcon(self, id):

        file_path = fd.fileDialog()
        fp = file_path.getPath()

        # check if correct path is  chosen
        if_exist = os.path.isfile(fp)

        if if_exist == True:
            cwd = os.getcwd() + '/imgs/required'
            img_dir, fileName = os.path.split(fp)

            if cwd == img_dir:
                sqlite.update_category(gv.db, id, fp)

            else:
                dst = cwd + '/' + fileName
                if_exist = os.path.isfile(dst)

                if if_exist == True:
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
                    copyfile(fp, dst)

                sqlite.update_category(gv.db, id, dst)


            self.reBuildCategories()

    # --------------------------------  block  -------------------------------------

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.pushButton_4.setToolTip(_translate("Form", "<html><head/><body><p>rename</p></body></html>", None))
        self.pushButton_3.setToolTip(_translate("Form", "<html><head/><body><p>picture</p></body></html>", None))
        self.pushButton_2.setToolTip(_translate("Form", "<html><head/><body><p>delete</p></body></html>", None))
        self.pushButton_2.setWhatsThis(_translate("Form", "<html><head/><body><p>delete</p></body></html>", None))



