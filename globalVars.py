__author__ = 'atana'

try:
    from PyQt4 import QtCore, QtGui
except Exception as e:
    print('Error in importing libs : globalVars : ', e)
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
style_lg_w = (_fromUtf8("background-color: qlineargradient(spread:pad,x1:0.1, y1:0.3, x2:0.7, y2:0.1, stop:0 lightgreen, stop:1 white);"))
style_lg_w_b = (_fromUtf8("background-color: qlineargradient(spread:pad,x1:0.1, y1:0.3, x2:0.7, y2:0.1, stop:0 lightgreen, stop:1 white); border:1px solid darkgreen;"))
background_green = "::section{Background-color:green; color: white; text-align: center; }"

saveDisket = 'imgs/required/btns/disketa.ico'
dir = 'imgs/required/btns/dir.png'
add = 'imgs/required/btns/add.png'
cancel = 'imgs/required/btns/cancel.png'
ch_pic = 'imgs/required/btns/ch_pic.png'
edit = 'imgs/required/btns/edit.jpg'
trash = 'imgs/required/btns/trash.png'
ok = 'imgs/required/btns/save.png'