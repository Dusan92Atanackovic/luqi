#-*- coding: utf-8 -*-

#Form implementation generated from reading ui file 'installations.ui'

#Created by: PyQt4 UI code generator 4.11.4



from PyQt4 import QtCore, QtGui

import sys
sys.path.append('/home/atana/Documents/python projects/luqi/luqi/server-scripts')

import client
import globalVars as gv
import pickle

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



TCP_IP = '192.168.88.185'
TCP_PORT = 9900



class Ui_Form(object):


    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(744, 652)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        self.verticalLayout = QtGui.QVBoxLayout(Form)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.frame = QtGui.QFrame(Form)


        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.frame)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))


        self.lineEdit = QtGui.QLineEdit(self.frame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit.sizePolicy().hasHeightForWidth())
        self.lineEdit.setSizePolicy(sizePolicy)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.lineEdit.keyReleaseEvent = self.handleKeyRelease
        self.horizontalLayout.addWidget(self.lineEdit)

        self.comboBox = QtGui.QComboBox(self.frame)
        self.comboBox.setMinimumSize(QtCore.QSize(200, 0))
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.comboBox.currentIndexChanged.connect(lambda event: self.cbAction())
        self.horizontalLayout.addWidget(self.comboBox)
        self.horizontalLayout_2.addLayout(self.horizontalLayout)
        self.verticalLayout.addWidget(self.frame)

        self.frame_2 = QtGui.QFrame(Form)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_2.setObjectName(_fromUtf8("frame_2"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout(self.frame_2)
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))

        self.tableWidget = QtGui.QTableWidget(self.frame_2)
        self.tableWidget.setObjectName(_fromUtf8("tableWidget"))
        self.tableWidget.setColumnCount(3)

        item = QtGui.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)

        item2 = QtGui.QTableWidgetItem('name')
        self.tableWidget.setHorizontalHeaderItem(0, item2)

        item3 = QtGui.QTableWidgetItem('version')
        item3.setBackgroundColor(QtGui.QColor(255, 125, 0))
        self.tableWidget.setHorizontalHeaderItem(1, item3)

        item4 = QtGui.QTableWidgetItem('download')

        self.tableWidget.setHorizontalHeaderItem(2, item4)

        # ---------------------------   STYLES ---------------------------------------------- #

        self.tableWidget.horizontalHeader().setStyleSheet(gv.background_green)
        self.tableWidget.verticalHeader().setStyleSheet(gv.background_green)

        self.horizontalLayout_3.addWidget(self.tableWidget)

        # ---------------------------------------------------------------------------------- #


        self.verticalLayout.addWidget(self.frame_2)

        # set stretching
        self.tableWidget.horizontalHeader().setResizeMode(0, QtGui.QHeaderView.Stretch)
        self.tableWidget.horizontalHeader().setResizeMode(1, QtGui.QHeaderView.Stretch)
        self.tableWidget.horizontalHeader().setResizeMode(2, QtGui.QHeaderView.Stretch)

        self.getTableData()

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    # get data
    def getTableData(self):

        k = client.Klijent(TCP_IP, TCP_PORT)
        dict = {'0001': ''}
        k.send(dict)
        self.programs_list = k.recive()
        k.close

        k = client.Klijent(TCP_IP, TCP_PORT)
        dict = {'0002': ''}
        k.send(dict)
        categories = k.recive()
        k.close

        if(len(categories) > 0):
            for x in categories:
                y = categories[x]
                self.comboBox.addItem(y[1])

    # fill table with data
    def fillTable(self, program_list):
        cr = 0
        cc = 2
        self.tableWidget.setRowCount(0)

        for i in program_list:
            self.tableWidget.insertRow(self.tableWidget.rowCount())

            k = program_list[i]
            for j in range(0, 2):
                item = QtGui.QTableWidgetItem()
                item.setText(k[j+1])
                item.setTextAlignment(QtCore.Qt.AlignCenter)
                self.tableWidget.setItem(self.tableWidget.rowCount()-1, j, item)

            button = QtGui.QPushButton()
            button.setText('Download')
            button.setStyleSheet(gv.style_lg_w_b)
            self.tableWidget.setCellWidget(cr, cc, button)
            button.clicked.connect(
                lambda event, item=k: self.download(item))
            cr += 1

    # filter category
    def cbAction(self):
        cb_text = self.comboBox.currentText()

        if cb_text == 'All':
            self.tableWidget.setRowCount(0)
            self.fillTable(self.programs_list)

        else:
            k = client.Klijent(TCP_IP, TCP_PORT)
            dict = {'0003': cb_text}
            k.send(dict)
            category = k.recive()
            for item in category:
                cat_key = item
            k.close
            tmpl = {}

            if not cat_key:
                key = 1

            self.tableWidget.setRowCount(0)

            for key in self.programs_list:
                tpl = self.programs_list[key]
                if tpl[7] == cat_key:
                    tmpl.update({key: tpl})

            self.fillTable(tmpl)

    # manage keyRelease - cals searchByName
    def handleKeyRelease(self, event):
        # print('key release:', event.key(), type(event.key()))
        QtGui.QLineEdit.keyReleaseEvent(self.lineEdit, event)
        if event.key() == 16777220:
            self.searchByName()

    # searches programs by name
    def searchByName(self):

        te = self.lineEdit.text()
        if len(te) > 0:
            k = client.Klijent(TCP_IP, TCP_PORT)
            dict = {'0004': te}
            k.send(dict)
            single = k.recive()
            k.close
            self.fillTable(single)
            self.lineEdit.clear()
        else:
            self.fillTable(self.programs_list)

    # this is download
    def download(self, i):
        print('cell click', i)
        # get category by name and vers
        # ovaj i treba ubaciti u lokalnu bazu
        # uz provere da li vec postoji program



    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        # item = self.tableWidget.horizontalHeaderItem(0)
        # item.setText(_translate("Form", "name", None))
        # item = self.tableWidget.horizontalHeaderItem(1)
        # item.setText(_translate("Form", "version", None))
        # item = self.tableWidget.horizontalHeaderItem(2)
        # item.setText(_translate("Form", "get", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Form = QtGui.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

