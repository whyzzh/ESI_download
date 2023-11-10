# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ESI_ui.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1500, 1063)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(1500, 1000))
        MainWindow.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(-1, 10, -1, 10)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_url = QtWidgets.QLabel(self.centralwidget)
        self.label_url.setMinimumSize(QtCore.QSize(0, 50))
        self.label_url.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.label_url.setFont(font)
        self.label_url.setTextFormat(QtCore.Qt.AutoText)
        self.label_url.setObjectName("label_url")
        self.horizontalLayout.addWidget(self.label_url)
        self.lineEdit_url = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_url.sizePolicy().hasHeightForWidth())
        self.lineEdit_url.setSizePolicy(sizePolicy)
        self.lineEdit_url.setMinimumSize(QtCore.QSize(0, 50))
        self.lineEdit_url.setMaximumSize(QtCore.QSize(16777215, 50))
        self.lineEdit_url.setText("")
        self.lineEdit_url.setFrame(True)
        self.lineEdit_url.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.lineEdit_url.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lineEdit_url.setReadOnly(False)
        self.lineEdit_url.setCursorMoveStyle(QtCore.Qt.VisualMoveStyle)
        self.lineEdit_url.setObjectName("lineEdit_url")
        self.horizontalLayout.addWidget(self.lineEdit_url)
        self.gridLayout_5.addLayout(self.horizontalLayout, 0, 0, 1, 2)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setContentsMargins(-1, 10, -1, 10)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_result_path = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_result_path.sizePolicy().hasHeightForWidth())
        self.label_result_path.setSizePolicy(sizePolicy)
        self.label_result_path.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.label_result_path.setFont(font)
        self.label_result_path.setTextFormat(QtCore.Qt.AutoText)
        self.label_result_path.setObjectName("label_result_path")
        self.horizontalLayout_2.addWidget(self.label_result_path)
        self.lineEdit_result_path = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(4)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_result_path.sizePolicy().hasHeightForWidth())
        self.lineEdit_result_path.setSizePolicy(sizePolicy)
        self.lineEdit_result_path.setMinimumSize(QtCore.QSize(0, 60))
        self.lineEdit_result_path.setMaximumSize(QtCore.QSize(16777215, 60))
        self.lineEdit_result_path.setStyleSheet("QLineEdit::disabled{\n"
"    background-color: rgb(216, 216, 216);\n"
"    color:rgb(0, 0, 0);\n"
"    border-color: rgb(55, 55, 55);\n"
"}")
        self.lineEdit_result_path.setText("")
        self.lineEdit_result_path.setObjectName("lineEdit_result_path")
        self.horizontalLayout_2.addWidget(self.lineEdit_result_path)
        self.pushButton_result_path = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_result_path.sizePolicy().hasHeightForWidth())
        self.pushButton_result_path.setSizePolicy(sizePolicy)
        self.pushButton_result_path.setMinimumSize(QtCore.QSize(0, 60))
        self.pushButton_result_path.setMaximumSize(QtCore.QSize(16777215, 60))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        self.pushButton_result_path.setFont(font)
        self.pushButton_result_path.setObjectName("pushButton_result_path")
        self.horizontalLayout_2.addWidget(self.pushButton_result_path)
        self.gridLayout_5.addLayout(self.horizontalLayout_2, 1, 0, 1, 1)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setContentsMargins(20, 10, -1, 10)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_year = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_year.sizePolicy().hasHeightForWidth())
        self.label_year.setSizePolicy(sizePolicy)
        self.label_year.setMaximumSize(QtCore.QSize(100, 50))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.label_year.setFont(font)
        self.label_year.setTextFormat(QtCore.Qt.AutoText)
        self.label_year.setObjectName("label_year")
        self.horizontalLayout_3.addWidget(self.label_year)
        self.spinBox_year = QtWidgets.QSpinBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(2)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.spinBox_year.sizePolicy().hasHeightForWidth())
        self.spinBox_year.setSizePolicy(sizePolicy)
        self.spinBox_year.setMinimumSize(QtCore.QSize(100, 60))
        self.spinBox_year.setMaximumSize(QtCore.QSize(200, 60))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.spinBox_year.setFont(font)
        self.spinBox_year.setMaximum(2100)
        self.spinBox_year.setProperty("value", 2021)
        self.spinBox_year.setObjectName("spinBox_year")
        self.horizontalLayout_3.addWidget(self.spinBox_year)
        self.label_month = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_month.sizePolicy().hasHeightForWidth())
        self.label_month.setSizePolicy(sizePolicy)
        self.label_month.setMaximumSize(QtCore.QSize(100, 50))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.label_month.setFont(font)
        self.label_month.setTextFormat(QtCore.Qt.AutoText)
        self.label_month.setObjectName("label_month")
        self.horizontalLayout_3.addWidget(self.label_month)
        self.spinBox_month = QtWidgets.QSpinBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(2)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.spinBox_month.sizePolicy().hasHeightForWidth())
        self.spinBox_month.setSizePolicy(sizePolicy)
        self.spinBox_month.setMinimumSize(QtCore.QSize(60, 60))
        self.spinBox_month.setMaximumSize(QtCore.QSize(200, 60))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.spinBox_month.setFont(font)
        self.spinBox_month.setMinimum(1)
        self.spinBox_month.setMaximum(12)
        self.spinBox_month.setObjectName("spinBox_month")
        self.horizontalLayout_3.addWidget(self.spinBox_month)
        self.gridLayout_5.addLayout(self.horizontalLayout_3, 1, 1, 1, 1)
        self.groupBox_log = QtWidgets.QGroupBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_log.sizePolicy().hasHeightForWidth())
        self.groupBox_log.setSizePolicy(sizePolicy)
        self.groupBox_log.setMinimumSize(QtCore.QSize(0, 490))
        self.groupBox_log.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.groupBox_log.setObjectName("groupBox_log")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.groupBox_log)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.textBrowser = QtWidgets.QTextBrowser(self.groupBox_log)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textBrowser.sizePolicy().hasHeightForWidth())
        self.textBrowser.setSizePolicy(sizePolicy)
        self.textBrowser.setMinimumSize(QtCore.QSize(0, 0))
        self.textBrowser.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.textBrowser.setStyleSheet("background-color: rgb(10, 10, 10);\n"
"color: rgb(255, 255, 255);")
        self.textBrowser.setObjectName("textBrowser")
        self.gridLayout_6.addWidget(self.textBrowser, 0, 0, 1, 1)
        self.gridLayout_5.addWidget(self.groupBox_log, 2, 0, 1, 1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBox_download = QtWidgets.QGroupBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(12)
        sizePolicy.setHeightForWidth(self.groupBox_download.sizePolicy().hasHeightForWidth())
        self.groupBox_download.setSizePolicy(sizePolicy)
        self.groupBox_download.setMinimumSize(QtCore.QSize(600, 0))
        self.groupBox_download.setMaximumSize(QtCore.QSize(600, 16777215))
        self.groupBox_download.setObjectName("groupBox_download")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox_download)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_wait_time = QtWidgets.QLabel(self.groupBox_download)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_wait_time.sizePolicy().hasHeightForWidth())
        self.label_wait_time.setSizePolicy(sizePolicy)
        self.label_wait_time.setMaximumSize(QtCore.QSize(400, 30))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(11)
        self.label_wait_time.setFont(font)
        self.label_wait_time.setTextFormat(QtCore.Qt.AutoText)
        self.label_wait_time.setObjectName("label_wait_time")
        self.horizontalLayout_7.addWidget(self.label_wait_time)
        self.spinBox_wait_time = QtWidgets.QSpinBox(self.groupBox_download)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(2)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.spinBox_wait_time.sizePolicy().hasHeightForWidth())
        self.spinBox_wait_time.setSizePolicy(sizePolicy)
        self.spinBox_wait_time.setMinimumSize(QtCore.QSize(100, 40))
        self.spinBox_wait_time.setMaximumSize(QtCore.QSize(200, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.spinBox_wait_time.setFont(font)
        self.spinBox_wait_time.setMaximum(36000)
        self.spinBox_wait_time.setProperty("value", 30)
        self.spinBox_wait_time.setObjectName("spinBox_wait_time")
        self.horizontalLayout_7.addWidget(self.spinBox_wait_time)
        self.gridLayout.addLayout(self.horizontalLayout_7, 0, 0, 1, 2)
        self.pushButton_download_path = QtWidgets.QPushButton(self.groupBox_download)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_download_path.sizePolicy().hasHeightForWidth())
        self.pushButton_download_path.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(11)
        self.pushButton_download_path.setFont(font)
        self.pushButton_download_path.setObjectName("pushButton_download_path")
        self.gridLayout.addWidget(self.pushButton_download_path, 2, 0, 1, 1)
        self.pushButton_addtion = QtWidgets.QPushButton(self.groupBox_download)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_addtion.sizePolicy().hasHeightForWidth())
        self.pushButton_addtion.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(11)
        self.pushButton_addtion.setFont(font)
        self.pushButton_addtion.setObjectName("pushButton_addtion")
        self.gridLayout.addWidget(self.pushButton_addtion, 2, 1, 1, 1)
        self.pushButton_download_start = QtWidgets.QPushButton(self.groupBox_download)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_download_start.sizePolicy().hasHeightForWidth())
        self.pushButton_download_start.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(11)
        self.pushButton_download_start.setFont(font)
        self.pushButton_download_start.setObjectName("pushButton_download_start")
        self.gridLayout.addWidget(self.pushButton_download_start, 1, 0, 1, 2)
        self.verticalLayout.addWidget(self.groupBox_download)
        self.groupBox_add_colleges = QtWidgets.QGroupBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(6)
        sizePolicy.setHeightForWidth(self.groupBox_add_colleges.sizePolicy().hasHeightForWidth())
        self.groupBox_add_colleges.setSizePolicy(sizePolicy)
        self.groupBox_add_colleges.setMinimumSize(QtCore.QSize(600, 0))
        self.groupBox_add_colleges.setMaximumSize(QtCore.QSize(600, 16777215))
        self.groupBox_add_colleges.setObjectName("groupBox_add_colleges")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.groupBox_add_colleges)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.pushButton_generate_start = QtWidgets.QPushButton(self.groupBox_add_colleges)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_generate_start.sizePolicy().hasHeightForWidth())
        self.pushButton_generate_start.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(11)
        self.pushButton_generate_start.setFont(font)
        self.pushButton_generate_start.setObjectName("pushButton_generate_start")
        self.horizontalLayout_6.addWidget(self.pushButton_generate_start)
        self.pushButton_check_ESI = QtWidgets.QPushButton(self.groupBox_add_colleges)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_check_ESI.sizePolicy().hasHeightForWidth())
        self.pushButton_check_ESI.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(11)
        self.pushButton_check_ESI.setFont(font)
        self.pushButton_check_ESI.setObjectName("pushButton_check_ESI")
        self.horizontalLayout_6.addWidget(self.pushButton_check_ESI)
        self.verticalLayout.addWidget(self.groupBox_add_colleges)
        self.groupBox_sub_table = QtWidgets.QGroupBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(13)
        sizePolicy.setHeightForWidth(self.groupBox_sub_table.sizePolicy().hasHeightForWidth())
        self.groupBox_sub_table.setSizePolicy(sizePolicy)
        self.groupBox_sub_table.setMinimumSize(QtCore.QSize(600, 0))
        self.groupBox_sub_table.setMaximumSize(QtCore.QSize(600, 1000000))
        self.groupBox_sub_table.setObjectName("groupBox_sub_table")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox_sub_table)
        self.gridLayout_2.setSpacing(12)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.lineEdit_ESI_stat = QtWidgets.QLineEdit(self.groupBox_sub_table)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.lineEdit_ESI_stat.sizePolicy().hasHeightForWidth())
        self.lineEdit_ESI_stat.setSizePolicy(sizePolicy)
        self.lineEdit_ESI_stat.setMinimumSize(QtCore.QSize(0, 30))
        self.lineEdit_ESI_stat.setText("")
        self.lineEdit_ESI_stat.setObjectName("lineEdit_ESI_stat")
        self.horizontalLayout_4.addWidget(self.lineEdit_ESI_stat)
        self.pushButton_ESI_stat = QtWidgets.QPushButton(self.groupBox_sub_table)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.pushButton_ESI_stat.sizePolicy().hasHeightForWidth())
        self.pushButton_ESI_stat.setSizePolicy(sizePolicy)
        self.pushButton_ESI_stat.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        self.pushButton_ESI_stat.setFont(font)
        self.pushButton_ESI_stat.setObjectName("pushButton_ESI_stat")
        self.horizontalLayout_4.addWidget(self.pushButton_ESI_stat)
        self.gridLayout_2.addLayout(self.horizontalLayout_4, 1, 0, 1, 2)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.lineEdit_final_stat = QtWidgets.QLineEdit(self.groupBox_sub_table)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.lineEdit_final_stat.sizePolicy().hasHeightForWidth())
        self.lineEdit_final_stat.setSizePolicy(sizePolicy)
        self.lineEdit_final_stat.setMinimumSize(QtCore.QSize(0, 30))
        self.lineEdit_final_stat.setText("")
        self.lineEdit_final_stat.setObjectName("lineEdit_final_stat")
        self.horizontalLayout_5.addWidget(self.lineEdit_final_stat)
        self.pushButton_final_stat = QtWidgets.QPushButton(self.groupBox_sub_table)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.pushButton_final_stat.sizePolicy().hasHeightForWidth())
        self.pushButton_final_stat.setSizePolicy(sizePolicy)
        self.pushButton_final_stat.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        self.pushButton_final_stat.setFont(font)
        self.pushButton_final_stat.setObjectName("pushButton_final_stat")
        self.horizontalLayout_5.addWidget(self.pushButton_final_stat)
        self.gridLayout_2.addLayout(self.horizontalLayout_5, 3, 0, 1, 2)
        self.pushButton_sub_table_update = QtWidgets.QPushButton(self.groupBox_sub_table)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_sub_table_update.sizePolicy().hasHeightForWidth())
        self.pushButton_sub_table_update.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(11)
        self.pushButton_sub_table_update.setFont(font)
        self.pushButton_sub_table_update.setObjectName("pushButton_sub_table_update")
        self.gridLayout_2.addWidget(self.pushButton_sub_table_update, 4, 0, 1, 1)
        self.pushButton_check_sub_table = QtWidgets.QPushButton(self.groupBox_sub_table)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_check_sub_table.sizePolicy().hasHeightForWidth())
        self.pushButton_check_sub_table.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(11)
        self.pushButton_check_sub_table.setFont(font)
        self.pushButton_check_sub_table.setObjectName("pushButton_check_sub_table")
        self.gridLayout_2.addWidget(self.pushButton_check_sub_table, 4, 1, 1, 1)
        self.label_final_stat = QtWidgets.QLabel(self.groupBox_sub_table)
        self.label_final_stat.setObjectName("label_final_stat")
        self.gridLayout_2.addWidget(self.label_final_stat, 2, 0, 1, 2)
        self.label_ESI_stat = QtWidgets.QLabel(self.groupBox_sub_table)
        self.label_ESI_stat.setObjectName("label_ESI_stat")
        self.gridLayout_2.addWidget(self.label_ESI_stat, 0, 0, 1, 2)
        self.verticalLayout.addWidget(self.groupBox_sub_table)
        self.groupBox_program = QtWidgets.QGroupBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(10)
        sizePolicy.setHeightForWidth(self.groupBox_program.sizePolicy().hasHeightForWidth())
        self.groupBox_program.setSizePolicy(sizePolicy)
        self.groupBox_program.setMinimumSize(QtCore.QSize(0, 170))
        self.groupBox_program.setObjectName("groupBox_program")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.groupBox_program)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.pushButton_update_driver = QtWidgets.QPushButton(self.groupBox_program)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_update_driver.sizePolicy().hasHeightForWidth())
        self.pushButton_update_driver.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.pushButton_update_driver.setFont(font)
        self.pushButton_update_driver.setObjectName("pushButton_update_driver")
        self.gridLayout_3.addWidget(self.pushButton_update_driver, 0, 0, 1, 1)
        self.pushButton_refresh = QtWidgets.QPushButton(self.groupBox_program)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_refresh.sizePolicy().hasHeightForWidth())
        self.pushButton_refresh.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.pushButton_refresh.setFont(font)
        self.pushButton_refresh.setObjectName("pushButton_refresh")
        self.gridLayout_3.addWidget(self.pushButton_refresh, 0, 1, 1, 1)
        self.pushButton_exit = QtWidgets.QPushButton(self.groupBox_program)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_exit.sizePolicy().hasHeightForWidth())
        self.pushButton_exit.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.pushButton_exit.setFont(font)
        self.pushButton_exit.setObjectName("pushButton_exit")
        self.gridLayout_3.addWidget(self.pushButton_exit, 1, 0, 1, 2)
        self.verticalLayout.addWidget(self.groupBox_program)
        self.gridLayout_5.addLayout(self.verticalLayout, 2, 1, 1, 1)
        self.groupBox_progressbar = QtWidgets.QGroupBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_progressbar.sizePolicy().hasHeightForWidth())
        self.groupBox_progressbar.setSizePolicy(sizePolicy)
        self.groupBox_progressbar.setMinimumSize(QtCore.QSize(0, 120))
        self.groupBox_progressbar.setMaximumSize(QtCore.QSize(16777215, 200))
        self.groupBox_progressbar.setObjectName("groupBox_progressbar")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.groupBox_progressbar)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.label_progress_main = QtWidgets.QLabel(self.groupBox_progressbar)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_progress_main.sizePolicy().hasHeightForWidth())
        self.label_progress_main.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        self.label_progress_main.setFont(font)
        self.label_progress_main.setTextFormat(QtCore.Qt.AutoText)
        self.label_progress_main.setObjectName("label_progress_main")
        self.gridLayout_4.addWidget(self.label_progress_main, 0, 0, 1, 1)
        self.progressBar_main = QtWidgets.QProgressBar(self.groupBox_progressbar)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(3)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.progressBar_main.sizePolicy().hasHeightForWidth())
        self.progressBar_main.setSizePolicy(sizePolicy)
        self.progressBar_main.setMinimumSize(QtCore.QSize(0, 40))
        self.progressBar_main.setProperty("value", 24)
        self.progressBar_main.setObjectName("progressBar_main")
        self.gridLayout_4.addWidget(self.progressBar_main, 1, 0, 1, 1)
        self.gridLayout_5.addWidget(self.groupBox_progressbar, 3, 0, 1, 2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1500, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "ESI数据下载及整理"))
        self.label_url.setText(_translate("MainWindow", "网页地址："))
        self.label_result_path.setText(_translate("MainWindow", "结果路径："))
        self.pushButton_result_path.setText(_translate("MainWindow", "选择路径..."))
        self.label_year.setText(_translate("MainWindow", "年份："))
        self.label_month.setText(_translate("MainWindow", "月份："))
        self.groupBox_log.setTitle(_translate("MainWindow", "运行日志"))
        self.textBrowser.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'微软雅黑\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'SimSun\';\"><br /></p></body></html>"))
        self.groupBox_download.setTitle(_translate("MainWindow", "数据下载"))
        self.label_wait_time.setText(_translate("MainWindow", "网页刷新最长等待时间（秒）："))
        self.pushButton_download_path.setText(_translate("MainWindow", "查看保存路径"))
        self.pushButton_addtion.setText(_translate("MainWindow", "完善新增高校信息"))
        self.pushButton_download_start.setText(_translate("MainWindow", "开始运行"))
        self.groupBox_add_colleges.setTitle(_translate("MainWindow", "生成ESI数据表"))
        self.pushButton_generate_start.setText(_translate("MainWindow", "开始生成"))
        self.pushButton_check_ESI.setText(_translate("MainWindow", "查看生成结果"))
        self.groupBox_sub_table.setTitle(_translate("MainWindow", "学科统计表生成"))
        self.pushButton_ESI_stat.setText(_translate("MainWindow", "选择文件..."))
        self.pushButton_final_stat.setText(_translate("MainWindow", "选择文件..."))
        self.pushButton_sub_table_update.setText(_translate("MainWindow", "统计表更新"))
        self.pushButton_check_sub_table.setText(_translate("MainWindow", "查看统计表"))
        self.label_final_stat.setText(_translate("MainWindow", "各高校ESI数据统计表路径："))
        self.label_ESI_stat.setText(_translate("MainWindow", "ESI学科数据表路径："))
        self.groupBox_program.setTitle(_translate("MainWindow", "程序操作"))
        self.pushButton_update_driver.setText(_translate("MainWindow", "更新驱动"))
        self.pushButton_refresh.setText(_translate("MainWindow", "刷新程序"))
        self.pushButton_exit.setText(_translate("MainWindow", "退出程序"))
        self.groupBox_progressbar.setTitle(_translate("MainWindow", "任务进度"))
        self.label_progress_main.setText(_translate("MainWindow", "当前无进程"))