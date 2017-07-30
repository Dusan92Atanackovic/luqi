# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'add_cat_form_ui.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

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

class Ui_Form(object):

    def setupUi(self):
        self.Form = QtGui.QDialog()
        Form = self.Form
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(504, 550)
        self.verticalLayout = QtGui.QVBoxLayout(Form)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))

        self.frame = QtGui.QFrame(Form)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setMinimumSize(QtCore.QSize(0, 50))
        self.frame.setStyleSheet(_fromUtf8("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0  green, stop:1 white);"))
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))

        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.frame)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))

        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))

        self.lineEdit = QtGui.QLineEdit(self.frame)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.horizontalLayout.addWidget(self.lineEdit)

        self.pushButton = QtGui.QPushButton(self.frame)
        self.pushButton.setMinimumSize(QtCore.QSize(50, 0))
        self.pushButton.setStyleSheet(_fromUtf8("border-image: url(imgs/required/btns/add.png);background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 white, stop:1 white);"))
        self.pushButton.setText(_fromUtf8(""))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.horizontalLayout.addWidget(self.pushButton)

        self.horizontalLayout_2.addLayout(self.horizontalLayout)

        self.verticalLayout.addWidget(self.frame)

        self.frame_2 = QtGui.QFrame(Form)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setStyleSheet(_fromUtf8("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 green, stop:1 white);"))
        self.frame_2.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_2.setObjectName(_fromUtf8("frame_2"))

        self.verticalLayout_2 = QtGui.QVBoxLayout(self.frame_2)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))

        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))

        self.frame_3 = QtGui.QFrame(self.frame_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy)
        self.frame_3.setStyleSheet(_fromUtf8("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 white, stop:1 green);"))
        self.frame_3.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_3.setObjectName(_fromUtf8("frame_3"))

        self.horizontalLayout_3 = QtGui.QHBoxLayout(self.frame_3)
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))

        self.lineEdit_2 = QtGui.QLineEdit(self.frame_3)

        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_2.sizePolicy().hasHeightForWidth())
        self.lineEdit_2.setSizePolicy(sizePolicy)
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))

        self.horizontalLayout_3.addWidget(self.lineEdit_2)

        self.pushButton_4 = QtGui.QPushButton(self.frame_3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_4.sizePolicy().hasHeightForWidth())
        self.pushButton_4.setSizePolicy(sizePolicy)
        self.pushButton_4.setStyleSheet(_fromUtf8("border-image: url(imgs/required/btns/edit.jpg);background-color: transparent;"))
        self.pushButton_4.setText(_fromUtf8(""))
        self.pushButton_4.setObjectName(_fromUtf8("pushButton_4"))

        self.horizontalLayout_3.addWidget(self.pushButton_4)
        self.pushButton_3 = QtGui.QPushButton(self.frame_3)
        self.pushButton_3.setStyleSheet(_fromUtf8("border-image: url(imgs/required/btns/ch_pic.png); background-color: transparent;"))
        self.pushButton_3.setText(_fromUtf8(""))
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.horizontalLayout_3.addWidget(self.pushButton_3)

        self.pushButton_2 = QtGui.QPushButton(self.frame_3)
        self.pushButton_2.setStyleSheet(_fromUtf8("border-image: url(imgs/required/btns/trash.png);background-color: transparent;"))
        self.pushButton_2.setText(_fromUtf8(""))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.horizontalLayout_3.addWidget(self.pushButton_2)

        self.verticalLayout_3.addWidget(self.frame_3)
        self.verticalLayout_2.addLayout(self.verticalLayout_3)

        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(spacerItem)
        self.verticalLayout.addWidget(self.frame_2)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)


    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.pushButton_4.setToolTip(_translate("Form", "<html><head/><body><p>rename</p></body></html>", None))
        self.pushButton_3.setToolTip(_translate("Form", "<html><head/><body><p>picture</p></body></html>", None))
        self.pushButton_2.setToolTip(_translate("Form", "<html><head/><body><p>delete</p></body></html>", None))
        self.pushButton_2.setWhatsThis(_translate("Form", "<html><head/><body><p>delete</p></body></html>", None))



if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    # Form = QtGui.QDialog()
    ui = Ui_Form()
    ui.setupUi()
    ui.Form.show()
    sys.exit(app.exec_())

