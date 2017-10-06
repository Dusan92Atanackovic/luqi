# this is EDIT programs FORM

from PyQt4 import QtCore, QtGui
try:
    from shutil import copyfile
    import globalVars as gv
    import sqlite
    import subprocess
    import sys, os ,time, hashlib
    import fileDialogs as fd
except Exception as e:
    print('Error in importing libs : programsForm: ', e)

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

    def __init__(self, ui, programObject, terminal, app):
        self.ui = ui
        self.data = programObject
        self.terminal = terminal
        self.terminal.setText('This is terminal-like widget')
        self.app = app


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
        self.imageButton.clicked.connect(lambda event: self.ch_pic())
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
        self.installButton.clicked.connect(lambda event: self.run_command(self.lineEdit_install))
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
        self.updateButton.clicked.connect(lambda event: self.run_command(self.lineEdit_update))
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
        self.uninstallButton.clicked.connect(lambda event: self.run_command(self.lineEdit_uninstall))
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
        self.saveButton.clicked.connect(lambda event: self.updateProgram())

        # ------------------------------------  block ------------------------------------------------- #

        self.horizontalLayout_9.addWidget(self.saveButton)
        self.verticalLayout_3.addWidget(self.frame_5)
        self.verticalLayout.addWidget(self.frame_2)

        self.retranslateUi(Form)
        self.fillData()

        QtCore.QMetaObject.connectSlotsByName(Form)
        Form.setWindowModality(QtCore.Qt.ApplicationModal)


    def updateProgram(self):

        fields = {
        'name': self.lineEdit_Name.text(),
        'vers': self.lineEdit_Version.text(),
        'inst': self.lineEdit_install.text(),
        'updt': self.lineEdit_update.text(),
        'delt': self.lineEdit_uninstall.text(),
        'id'  : self.data.id }

        try:
            resp = sqlite.update_program(gv.db, **fields)
            if resp is True:
                self.ui.statusbar.showMessage('Program has been updated successfully', 3000)
            else:
                error = 'Exception in updateProgram: ' + str(resp)
                self.ui.statusbar.showMessage(error, 3000)
        except Exception as e:
            error = 'Exception in updateProgram: ' + str(e)
            self.ui.statusbar.showMessage(error, 3000)


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
        self.nameLabel.setText(_translate("Form", "    name :", None))
        self.versionLabel.setText(_translate("Form", "version :", None))
        self.installButton.setText(_translate("Form", "install", None))
        self.updateButton.setText(_translate("Form", "update", None))
        self.uninstallButton.setText(_translate("Form", "uninstall", None))
        self.saveButton.setText(_translate("Form", "Save", None))


    def run_command(self, cmnd):
        sudo_password = '18901890' + '\n'
        sudos = ['sudo', '-S']
        terminal = self.terminal

        terminal.clear()

        for item in eval(cmnd.text()):
            cmd = sudos + item.split()

            p = subprocess.Popen(cmd,  stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, bufsize=1, universal_newlines=True)
            p.stdin.write(sudo_password)
            p.poll()

            while True:
                line = p.stdout.readline()
                terminal.append(line)
                terminal.moveCursor(QtGui.QTextCursor.End)
                self.app.processEvents()
                if not line and p.poll is not None: break

            while True:
                err = p.stderr.readline()
                terminal.append(err)
                terminal.moveCursor(QtGui.QTextCursor.End)
                self.app.processEvents()
                if not err and p.poll is not None: break
            terminal.append('\n * END OF PROCESS *')


    def fif(self):
        #find installation file
        pass


    def ch_pic(self):
        id = self.data.id


        file_path = fd.fileDialog()
        fp = file_path.getPath()

        # check if correct path is  chosen
        if_exist = os.path.isfile(fp)

        if if_exist == True:
            cwd = os.getcwd() + '/imgs'
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

                ans = sqlite.update_program_img(gv.db, id, dst)

                if ans is True:
                    self.ui.statusbar.showMessage('Image has been updated', 3000)
                    self.ui.categoryFilter((self.data.category, None))

                else:
                    error = 'Exception in ch_pic: ' + str(ans)
                    self.ui.statusbar.showMessage(error, 3000)

