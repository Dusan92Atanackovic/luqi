from PyQt4 import QtCore, QtGui
import globalVars as gv

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

class programsFormClass(object):
    '''
        self.Form - Qwidget

            self.frame - top container for: img-button , name, and version
                self.imageButton -      img button
                self.nameLabel -        name label
                self.lineEdit_Name -    input for name
                self.versionLabel -     version label
                self.lineEdit_Version - input for version

            self.frame_2
                self.frame_4
                    self.dirButton -    button for dir choser
                self.installButton    + lineEdit_install
                self.updateButton     + lineEdit_update
                self.uninstallButton  + lineEdit_uninstall
                self.frame_5
                    self.saveButton   - button for saving changes

    '''

    def __init__(self, ui, programObject):
        self.ui = ui
        self.data = programObject


    def setupUi(self):

        self.Form = QtGui.QWidget()
        Form = self.Form
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(563, 382)

        self.verticalLayout = QtGui.QVBoxLayout(Form)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))

        # ------------------------------------  block ------------------------------------------------- #

        self.frame = QtGui.QFrame(Form)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))

        self.horizontalLayout = QtGui.QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))

        # ------------------------------------  block ------------------------------------------------- #
                                          #  img button #

        self.imageButton = QtGui.QPushButton(self.frame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.imageButton.sizePolicy().hasHeightForWidth())
        self.imageButton.setMinimumSize(QtCore.QSize(120, 100))
        self.imageButton.setSizePolicy(sizePolicy)
        self.imageButton.setObjectName(_fromUtf8("imageButton"))
        self.horizontalLayout.addWidget(self.imageButton)

        # ------------------------------------  block ------------------------------------------------- #

        self.frame_3 = QtGui.QFrame(self.frame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy)
        self.frame_3.setMinimumSize(QtCore.QSize(0, 120))
        self.frame_3.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_3.setObjectName(_fromUtf8("frame_3"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.frame_3)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))

        # ------------------------------------  block ------------------------------------------------- #

        self.horizontalLayout_7 = QtGui.QHBoxLayout()
        self.horizontalLayout_7.setObjectName(_fromUtf8("horizontalLayout_7"))


        self.nameLabel = QtGui.QLabel(self.frame_3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.nameLabel.sizePolicy().hasHeightForWidth())
        self.nameLabel.setSizePolicy(sizePolicy)
        self.nameLabel.setMinimumSize(QtCore.QSize(60, 0))
        self.nameLabel.setObjectName(_fromUtf8("label"))
        self.horizontalLayout_7.addWidget(self.nameLabel)

        # ------------------------------------  block ------------------------------------------------- #

        self.lineEdit_Name = QtGui.QLineEdit(self.frame_3)
        self.lineEdit_Name.setObjectName(_fromUtf8("lineEdit"))
        self.horizontalLayout_7.addWidget(self.lineEdit_Name)

        # ------------------------------------  block ------------------------------------------------- #

        self.verticalLayout_2.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_8 = QtGui.QHBoxLayout()
        self.horizontalLayout_8.setObjectName(_fromUtf8("horizontalLayout_8"))

        # ------------------------------------  block ------------------------------------------------- #

        self.versionLabel = QtGui.QLabel(self.frame_3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.versionLabel.sizePolicy().hasHeightForWidth())
        self.versionLabel.setSizePolicy(sizePolicy)
        self.versionLabel.setMinimumSize(QtCore.QSize(60, 0))
        self.versionLabel.setMaximumSize(QtCore.QSize(50, 16777215))
        self.versionLabel.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout_8.addWidget(self.versionLabel)

        # ------------------------------------  block ------------------------------------------------- #

        self.lineEdit_Version = QtGui.QLineEdit(self.frame_3)
        self.lineEdit_Version.setObjectName(_fromUtf8("lineEdit_2"))
        self.horizontalLayout_8.addWidget(self.lineEdit_Version)
        self.verticalLayout_2.addLayout(self.horizontalLayout_8)
        self.horizontalLayout.addWidget(self.frame_3)

        self.verticalLayout.addWidget(self.frame)

        # ------------------------------------  block ------------------------------------------------- #
        # ------------------------------------  block ------------------------------------------------- #
        # ------------------------------------  block ------------------------------------------------- #
        # ------------------------------------  block ------------------------------------------------- #
        # ------------------------------------  block ------------------------------------------------- #

        self.frame_2 = QtGui.QFrame(Form)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_2.setObjectName(_fromUtf8("frame_2"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.frame_2)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))

        # ------------------------------------  block ------------------------------------------------- #

        self.frame_4 = QtGui.QFrame(self.frame_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_4.sizePolicy().hasHeightForWidth())
        self.frame_4.setSizePolicy(sizePolicy)
        self.frame_4.setStyleSheet(_fromUtf8("border:0; padding:0; margin:0;"))
        self.frame_4.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_4.setObjectName(_fromUtf8("frame_4"))

        # ------------------------------------  block ------------------------------------------------- #

        self.horizontalLayout_6 = QtGui.QHBoxLayout(self.frame_4)
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))

        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem)

        # ------------------------------------  block ------------------------------------------------- #

        self.dirButton = QtGui.QPushButton(self.frame_4)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dirButton.sizePolicy().hasHeightForWidth())

        # ------------------------------------  block ------------------------------------------------- #

        self.dirButton.setSizePolicy(sizePolicy)
        self.dirButton.setMaximumSize(QtCore.QSize(50, 20))
        self.dirButton.setStyleSheet(_fromUtf8("border: 1px solid darkgray; border-radius:5px;"))
        self.dirButton.setObjectName(_fromUtf8("installButton"))
        stil = "border-image:url(%s); background-repeat: no-repeat;" % (gv.dir)
        self.dirButton.setStyleSheet(_fromUtf8(stil))
        self.horizontalLayout_5.addWidget(self.dirButton)



        self.horizontalLayout_6.addLayout(self.horizontalLayout_5)

        # ------------------------------------  block ------------------------------------------------- #

        self.verticalLayout_3.addWidget(self.frame_4)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))

        self.installButton = QtGui.QPushButton(self.frame_2)
        self.installButton.setObjectName(_fromUtf8("installButton"))
        self.horizontalLayout_2.addWidget(self.installButton)

        self.lineEdit_install = QtGui.QLineEdit(self.frame_2)
        self.lineEdit_install.setObjectName(_fromUtf8("lineEdit_install"))
        self.horizontalLayout_2.addWidget(self.lineEdit_install)

        self.verticalLayout_3.addLayout(self.horizontalLayout_2)


        # ------------------------------------  block ------------------------------------------------- #


        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))

        self.updateButton = QtGui.QPushButton(self.frame_2)
        self.updateButton.setObjectName(_fromUtf8("updateButton"))
        self.horizontalLayout_3.addWidget(self.updateButton)


        self.lineEdit_update = QtGui.QLineEdit(self.frame_2)
        self.lineEdit_update.setObjectName(_fromUtf8("lineEdit_update"))
        self.horizontalLayout_3.addWidget(self.lineEdit_update)

        self.verticalLayout_3.addLayout(self.horizontalLayout_3)

        # ------------------------------------  block ------------------------------------------------- #


        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))

        self.uninstallButton = QtGui.QPushButton(self.frame_2)
        self.uninstallButton.setObjectName(_fromUtf8("uninstallButton"))
        self.horizontalLayout_4.addWidget(self.uninstallButton)

        self.lineEdit_uninstall = QtGui.QLineEdit(self.frame_2)
        self.lineEdit_uninstall.setObjectName(_fromUtf8("lineEdit_uninstall"))
        self.horizontalLayout_4.addWidget(self.lineEdit_uninstall)

        self.verticalLayout_3.addLayout(self.horizontalLayout_4)

        # ------------------------------------  block ------------------------------------------------- #

        self.frame_5 = QtGui.QFrame(self.frame_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_5.sizePolicy().hasHeightForWidth())
        self.frame_5.setSizePolicy(sizePolicy)
        self.frame_5.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_5.setObjectName(_fromUtf8("frame_5"))
        self.horizontalLayout_9 = QtGui.QHBoxLayout(self.frame_5)
        self.horizontalLayout_9.setObjectName(_fromUtf8("horizontalLayout_9"))

        # ------------------------------------  block ------------------------------------------------- #

        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem1)

        self.saveButton = QtGui.QPushButton(self.frame_5)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.saveButton.sizePolicy().hasHeightForWidth())
        self.saveButton.setSizePolicy(sizePolicy)
        self.saveButton.setObjectName(_fromUtf8("saveButton"))
        self.saveButton.setIcon(QtGui.QIcon(gv.saveDisket))

        # ------------------------------------  block ------------------------------------------------- #

        self.horizontalLayout_9.addWidget(self.saveButton)
        self.verticalLayout_3.addWidget(self.frame_5)
        self.verticalLayout.addWidget(self.frame_2)

        self.retranslateUi(Form)
        self.fillData()

        QtCore.QMetaObject.connectSlotsByName(Form)
        Form.setWindowModality(QtCore.Qt.ApplicationModal)



    def fillData(self):
        stil = "border-image:url(%s); background-repeat: no-repeat;" % (self.data.img)
        self.imageButton.setStyleSheet(_fromUtf8(stil))
        self.lineEdit_Name.setText(self.data.name)
        self.lineEdit_Version.setText(self.data.version)
        self.lineEdit_install.setText(self.data.command)
        self.lineEdit_update.setText(self.data.update)
        self.lineEdit_uninstall.setText(self.data.delete)


    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        # self.imageButton.setText(_translate("Form", "image", None))
        self.nameLabel.setText(_translate("Form", "    name :", None))
        self.versionLabel.setText(_translate("Form", "version :", None))
        # self.dirButton.setText(_translate("Form", "dir", None))
        self.installButton.setText(_translate("Form", "install", None))
        self.updateButton.setText(_translate("Form", "update", None))
        self.uninstallButton.setText(_translate("Form", "uninstall", None))
        self.saveButton.setText(_translate("Form", "Save", None))