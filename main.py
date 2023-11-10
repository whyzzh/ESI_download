from PyQt5 import QtWidgets
import sys
from interface_port import MyMainWindow


app = QtWidgets.QApplication(sys.argv)
myWin = MyMainWindow()
myWin.show()
sys.exit(app.exec_())