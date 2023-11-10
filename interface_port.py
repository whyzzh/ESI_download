import pandas as pd
from PyQt5.QtWidgets import QMainWindow, QFileDialog, QMessageBox, QDialog, QTableWidgetItem
from PyQt5.QtCore import QThread, pyqtSignal
from PyQt5.QtGui import QBrush, QColor
from ESI_ui import Ui_MainWindow
from download_datas import DataDownload, DOCTYPE_NUMBER, FIELD_NUMBER, CollegesAddtion
from datas_combination import DataCombination
from final_update import StatisticUpdate, update_style
from addition_colleges import Ui_Dialog
from chromedriver_update import *
from functools import partial
import time
import os


class MyMainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        """初始化参数及界面状态"""
        super(MyMainWindow, self).__init__(parent)
        self.url = 'https://esi.clarivate.com/IndicatorsAction.action?Init=Yes&SrcApp=IC2LS&SID=H3-akPx2Fx2BtEqfh5ExxadFn7SiT9xxJl00avrMt-18x2dLfygerVKBr6ix2BC4bxxs5fRAx3Dx3DqdgS2m1DnF7Fr6stphx2BgHgx3Dx3D-qBgNuLRjcgZrPm66fhjx2Fmwx3Dx3D-h9tQNJ9Nv4eh45yLvkdX3gx3Dx3D'
        self.setupUi(self)
        self.init_ui()
        self.init_signal()
        self.resultPath = None
        self.excelsPath = None
        self.statsPath = None
        self.progress_step_main = float(100 / (DOCTYPE_NUMBER * (FIELD_NUMBER + 1)))
        self.progress_num_main = 0
        self.progress_num_sub = 0

    def init_ui(self):
        """初始化界面状态"""
        # 在 "网页地址" 栏显示需要爬取的url
        self.lineEdit_url.setText(self.url)
        self.lineEdit_url.setCursorPosition(0)  # 显示爬取网址，并靠左显示

        # 将结果路径的 "选择路径..." 按钮置为可点击状态
        self.pushButton_result_path.setEnabled(True)
        self.lineEdit_result_path.setEnabled(False)

        # 将 "数据下载" 板块相应按键置于不可点击状态
        self.pushButton_download_start.setEnabled(False)  # 开始运行
        self.pushButton_download_path.setEnabled(False)  # 查看保存路径
        self.pushButton_addtion.setEnabled(False)  # 完善新增高校信息

        # 将 "生成ESI统计表" 板块相应按键置于不可点击状态
        # self.pushButton_generate_start.setEnabled(False)  # 开始生成
        self.pushButton_check_ESI.setEnabled(False)  # 查看生成结果

        # 将 "学科统计表生成" 板块相应按键置于不可点击状态，以及将统计表路径栏置于不可编辑状态
        self.pushButton_ESI_stat.setEnabled(False)  # ESI学科数据表“选择文件...”按钮
        self.lineEdit_ESI_stat.setEnabled(False)  # ESI学科数据表路径文本栏
        self.pushButton_final_stat.setEnabled(False)  # 各高校ESI数据统计表“选择文件...”按钮
        self.lineEdit_final_stat.setEnabled(False)  # 各高校ESI数据统计表路径文本栏
        self.pushButton_sub_table_update.setEnabled(False)  # 统计表更新
        self.pushButton_check_sub_table.setEnabled(False)  # 查看统计表

        # 将 "程序操作" 板块相应按键置于可点击状态
        self.pushButton_update_driver.setEnabled(True)  # 更新驱动
        self.pushButton_refresh.setEnabled(True)  # 刷新程序
        self.pushButton_exit.setEnabled(True)  # 退出程序

        # 将进度条置于0%处
        self.progressBar_main.setValue(0)

        # 将年份，月份栏置为当前时间
        currentTime = time.localtime()
        currentYear = currentTime.tm_year
        currentMonth = currentTime.tm_mon
        if currentMonth % 2 == 0:
            currentMonth -= 1
        self.spinBox_year.setValue(currentYear)
        self.spinBox_month.setValue(currentMonth)

    def init_signal(self):
        """初始化信号与槽函数连接"""
        self.pushButton_result_path.clicked.connect(self.choose_result_path)
        self.pushButton_download_start.clicked.connect(self.download_main)
        self.pushButton_download_path.clicked.connect(self.check_download_path)
        self.pushButton_addtion.clicked.connect(self.get_addition_list)
        self.pushButton_generate_start.clicked.connect(self.generate_ESI)
        self.pushButton_check_ESI.clicked.connect(self.check_com_result)

        self.pushButton_ESI_stat.clicked.connect(self.choose_ESI_file)
        self.pushButton_final_stat.clicked.connect(self.choose_sub_file)
        self.pushButton_sub_table_update.clicked.connect(self.update_statistic)
        self.pushButton_check_sub_table.clicked.connect(self.check_upd_result)

        self.pushButton_update_driver.clicked.connect(self.update_webdriver)
        self.pushButton_refresh.clicked.connect(self.refresh_program)
        self.pushButton_exit.clicked.connect(self.close)

    def choose_result_path(self):
        """选择结果保存路径"""
        resultPath = QFileDialog.getExistingDirectory(self, "选取结果保存路径", './')
        self.lineEdit_result_path.setCursorPosition(0)

        if os.path.exists(resultPath):
            # 若路径存在，则将 "开始运行" 按键置于可点击状态
            self.pushButton_download_start.setEnabled(True)
        else:
            # 若路径不存在，则弹出报错窗口
            noFile = QMessageBox()
            noFile.setWindowTitle("Error")
            noFile.setText("没有选择文件")
            noFile.setIcon(QMessageBox.Critical)
            noFile.setStandardButtons(QMessageBox.Close)
            return
        self.resultPath = resultPath.replace('/', '\\')
        self.lineEdit_result_path.setText(self.resultPath)
        self.excelsPath = self.resultPath + r'\doc_excels'
        self.pushButton_ESI_stat.setEnabled(True)
        self.lineEdit_ESI_stat.setEnabled(True)
        self.pushButton_final_stat.setEnabled(True)
        self.lineEdit_final_stat.setEnabled(True)

    def download_main(self):
        """运行数据下载程序"""
        self.progress_num_main = 0
        # 将其他引发进程的按键全部置为不可点击状态
        self.pushButton_generate_start.setEnabled(False)

        # 重命名进度条为数据下载任务
        self.label_progress_main.setText('从网页下载数据...')

        # 运行数据下载进程
        self.waitTime = self.spinBox_wait_time.value()
        self.downloadThread = DownloadThread(self.url, self.resultPath, self.waitTime, self.excelsPath)
        self.downloadThread.startOut.connect(partial(self.refresh_ui, '--------数据下载任务开始--------'))
        self.downloadThread.progressOut.connect(self.refresh_ui)
        self.downloadThread.finishedOut.connect(partial(self.refresh_ui, '--------数据下载任务结束--------'))
        self.downloadThread.resultListOut.connect(self.get_list)
        self.downloadThread.start()

    def generate_ESI(self):
        """运行生成ESI数据表程序"""
        # 重置进度条信息
        
        if self.resultPath is None:
            noResPath = QMessageBox()
            noResPath.setWindowTitle("No result path!")
            noResPath.setText("未指定结果保存路径！")
            noResPath.setIcon(QMessageBox.Critical)
            noResPath.setStandardButtons(QMessageBox.Close)
            noResPath.exec_()
            return
        self.label_progress_main.setText('ESI数据表生成...')
        self.progressBar_main.setValue(0)
        self.progress_num_main = 0

        self.year = self.spinBox_year.value()
        self.month = self.spinBox_month.value()
        self.generateThread = GenerateThread(self.excelsPath, self.resultPath, self.year, self.month)
        self.generateThread.startOut.connect(partial(self.refresh_ui, '--------ESI数据表生成任务开始--------'))
        self.generateThread.processOut.connect(self.refresh_ui)
        self.generateThread.finishedOut.connect(partial(self.refresh_ui, '--------ESI数据表生成任务结束--------'))
        self.generateThread.resultXlsOut.connect(self.get_result_file)
        self.generateThread.start()

    def choose_ESI_file(self):
        """选择ESI数据统计表路径"""
        ESIFile, _ = QFileDialog.getOpenFileName(self, "选取ESI数据统计表", './', "所有Excel文件(*.xlsx)")
        self.lineEdit_result_path.setCursorPosition(0)

        if not os.path.exists(ESIFile):
            # 若路径不存在，则弹出报错窗口
            noFile = QMessageBox()
            noFile.setWindowTitle("Error")
            noFile.setText("没有选择文件")
            noFile.setIcon(QMessageBox.Critical)
            noFile.setStandardButtons(QMessageBox.Close)
            return
        self.resultFile_com = ESIFile.replace('/', '\\')
        self.lineEdit_ESI_stat.setText(self.resultFile_com)

    def choose_sub_file(self):
        """选择上一次更新的学科数据统计表路径"""
        statsFile, _ = QFileDialog.getOpenFileName(self, "选取学科数据统计表", './', "所有Excel文件(*.xlsx)")
        self.lineEdit_result_path.setCursorPosition(0)

        if os.path.exists(statsFile):
            # 若路径存在，则将 "统计表更新" 按键置于可点击状态
            self.pushButton_sub_table_update.setEnabled(True)
        else:
            # 若路径不存在，则弹出报错窗口
            noFile = QMessageBox()
            noFile.setWindowTitle("Error")
            noFile.setText("没有选择文件")
            noFile.setIcon(QMessageBox.Critical)
            noFile.setStandardButtons(QMessageBox.Close)
            return
        self.statsPath = statsFile.replace('/', '\\')
        self.lineEdit_final_stat.setText(self.statsPath)
        self.pushButton_sub_table_update.setEnabled(True)
    
    def update_statistic(self):
        """更新ESI数据统计表"""
        # 检查ESI数据表路径是否存在

        self.resultFile_com = self.lineEdit_ESI_stat.text()
        if not os.path.exists(self.resultFile_com):
            noFile = QMessageBox()
            noFile.setWindowTitle("Error")
            noFile.setText("ESI数据表路径无效")
            noFile.setIcon(QMessageBox.Critical)
            noFile.setStandardButtons(QMessageBox.Close)
            return
        self.label_progress_main.setText('ESI学科统计表更新...')
        self.progressBar_main.setValue(0)

        self.year = self.spinBox_year.value()
        self.month = self.spinBox_month.value()
        self.updateThread = UpdateThread(self.resultFile_com, self.statsPath, self.resultPath, self.year, self.month)
        self.updateThread.startOut.connect(partial(self.refresh_ui, '--------学科统计表生成任务开始--------'))
        self.updateThread.processOut.connect(self.refresh_ui)
        self.updateThread.finishedOut.connect(partial(self.refresh_ui, '--------学科统计表生成任务结束--------'))
        self.updateThread.resultXlsOut.connect(self.get_result_file_upd)
        self.updateThread.start()

    def refresh_ui(self, work_log):
        """根据运行过程更新日志栏，进度条及按钮状态"""
        if work_log == 'plus':
            self.update_progressBar()
            return
        elif work_log == 'excels_path':
            # 将 "查看保存路径" 按键置为可点击
            self.pushButton_download_path.setEnabled(True)
            return
        elif work_log == 'finished_download':
            self.progressBar_main.setValue(100)
            self.label_progress_main.setText('任务完成')
            return
        elif work_log == 'timeout':
            # 若网页请求超时，则弹出报错窗口
            self.pop_dialog(QMessageBox.Warning, 'TimeOut', '网页刷新等待超时！')
            self.label_progress_main.setText('当前无进程')
            self.progressBar_main.setValue(0)
            return
        elif work_log == 'addition_completed':
            self.pushButton_addtion.setEnabled(True)
            self.pushButton_generate_start.setEnabled(True)
            work_log = '新增高校筛选完成'
        elif work_log == 'global_finished':
            self.label_progress_main.setText('正在将数据写入excel...')
            return
        elif work_log == 'finished_com':
            self.pushButton_check_ESI.setEnabled(True)
            return
        elif work_log == 'finished_upd':
            self.progressBar_main.setValue(100)
            self.label_progress_main.setText('任务完成')
            self.pushButton_check_sub_table.setEnabled(True)
            return
        elif work_log == 'update_error':
            self.pop_dialog(QMessageBox.Critical, 'Error', '数据表更新过程发生错误！')
            self.label_progress_main.setText('当前无进程')
            return
        elif work_log == 'driver_error':
            self.pop_dialog(QMessageBox.Critical, 'Error', '网页驱动不存在或驱动版本错误！')
            return
        elif work_log == 'None':
            work_log = 'Excel文件下载错误，请重新开始下载操作！'
            self.pop_dialog(QMessageBox.Critical, 'Error', 'Excel文件下载错误！')
            self.progress_num_main = 0
            self.progressBar_main.setValue(0)
            self.label_progress_main.setText('当前无进程')

        logTime = '[' + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + ']：'
        logText = logTime + work_log
        self.textBrowser.append(logText)

    def update_progressBar(self):
        """数据下载任务中，根据运行进度加载进度条"""
        # 进程进度条更新
        self.progress_num_main += self.progress_step_main
        self.progressBar_main.setValue(int(self.progress_num_main))

    def update_webdriver(self):
        """更新chromedriver"""
        updateRes = check_chrome_driver_update()
        if updateRes == -1:
            self.pop_dialog(QMessageBox.Warning, 'No need to update', '网页驱动已经是正确版本')
        elif updateRes == 0:
            self.pop_dialog(QMessageBox.Critical, 'Error', '网页驱动更新失败！')
        else:
            self.pop_dialog(QMessageBox.Information, 'Finished', '网页驱动更新完成！')

    def check_download_path(self):
        """弹出下载路径"""
        os.startfile(self.excelsPath)

    def get_result_file(self, result_file):
        """获取生成的ESI结果文件路径"""
        # self.resultFile_com = result_file
        self.lineEdit_ESI_stat.setText(result_file)

    def check_com_result(self):
        """弹出生成的ESI结果文件"""
        if os.path.exists(self.resultFile_com):
            os.startfile(self.resultFile_com)

    def get_result_file_upd(self, result_file):
        """获取生成的ESI结果文件路径"""
        self.resultFile_upd = result_file

    def check_upd_result(self):
        """弹出更新后的学科数据统计表文件"""
        if os.path.exists(self.resultFile_upd):
            os.startfile(self.resultFile_upd)

    def get_list(self, addition_list):
        """将获得的新增高校列表变为类成员"""
        self.addtionList = addition_list

    def get_addition_list(self):
        """弹出查看并完善新增高校信息窗口"""
        # 弹窗初始化
        self.addtionDialog = QDialog()
        Ui_Dialog.setupUi(self, self.addtionDialog)

        # 获取新增高校数量，并设置弹窗表格行数
        self.num_add = len(self.addtionList)
        self.tableWidget.setRowCount(self.num_add)

        # 填入新增高校名称列表
        for i in range(len(self.addtionList)):
            item_add = QTableWidgetItem(self.addtionList[i])
            item_add.setBackground(QBrush(QColor(200, 200, 200)))
            self.tableWidget.setItem(i, 0, item_add)
            for j in range(1, 3):
                item_add = QTableWidgetItem("")
                self.tableWidget.setItem(i, j, item_add)

        # 弹窗按钮信号连接
        self.pushButton_okey_dia.clicked.connect(self.renew_contrast)
        self.pushButton_cancel_dia.clicked.connect(self.close_dialog)

        # 运行弹窗
        self.addtionDialog.exec_()

    def renew_contrast(self):
        """更新高校对照表"""
        df_contrast = pd.read_excel('schools_contrast.xlsx')
        self.df_addition = pd.DataFrame(columns=['Institutions', '高校', 'Countries', '省份'])
        self.refresh_ui('正在更新高校对照表数据...')
        for row in range(self.num_add):
            addition_i = []
            for col in range(3):
                addition_i.append(self.tableWidget.item(row, col).text())
            df_addition_i = pd.DataFrame(
                {'Institutions': [addition_i[0]],
                 '高校': [addition_i[1]],
                 'Countries': ['中国'],
                 '省份': [addition_i[2]]}
            )
            self.df_addition = self.df_addition.append(df_addition_i)
        self.addtionDialog.close()
        self.refresh_ui('高校对照表数据更新完成')
        self.df_addition.rename(columns={'Countries': '国别'}, inplace=True)
        df_contrast = df_contrast.append(self.df_addition)
        # df_contrast.rename(columns={'Countries': '国别'}, inplace=True)
        df_contrast.to_excel('schools_contrast.xlsx', index=False)
        self.refresh_ui('高校对照数据表已更新完成！')

    def close_dialog(self):
        """直接关闭弹窗"""
        self.addtionDialog.close()
        
    def pop_dialog(self, e_type, title, text):
        """弹出错误窗口"""
        popDia = QMessageBox()
        popDia.setWindowTitle(title)
        popDia.setText(text)
        popDia.setIcon(e_type)
        popDia.setStandardButtons(QMessageBox.Close)
        popDia.exec_()

    def refresh_program(self):
        """刷新程序"""
        # self.textBrowser.append('显示个内容')
        # self.addtionList = ['COLLEGE']
        pass


class DownloadThread(QThread):
    startOut = pyqtSignal()
    progressOut = pyqtSignal(str)
    finishedOut = pyqtSignal()
    resultListOut = pyqtSignal(list)

    def __init__(self, url, result_path, wait_time, excels_path):
        super(DownloadThread, self).__init__()
        self.url = url
        self.resultPath = result_path
        self.waitTime = wait_time
        self.excelsPath = excels_path

    def run(self):
        errorLogs = ['None', 'driver_error', 'timeout']
        self.startOut.emit()
        dataDownload = DataDownload(self.url, self.resultPath, self.waitTime, self.excelsPath)
        logText = dataDownload.start()
        while True:
            try:
                logMessage = next(logText)
                self.progressOut.emit(logMessage)
                if logMessage in errorLogs:
                    self.finishedOut.emit()
                    return
            except StopIteration:
                break

        colleges_addtion = CollegesAddtion(self.excelsPath)
        logText = colleges_addtion.start()
        while True:
            try:
                self.progressOut.emit(next(logText))
            except StopIteration:
                break

        self.resultListOut.emit(dataDownload.additionList)
        self.finishedOut.emit()


class GenerateThread(QThread):
    startOut = pyqtSignal()
    processOut = pyqtSignal(str)
    finishedOut = pyqtSignal()
    resultXlsOut = pyqtSignal(str)

    def __init__(self, excels_path, result_path, year, month):
        super(GenerateThread, self).__init__()
        self.excelsPath = excels_path
        self.resultPath = result_path
        self.year = year
        self.month = month

    def run(self):
        self.startOut.emit()
        dataCombination = DataCombination(self.excelsPath, self.resultPath, self.year, self.month)
        logText = dataCombination.start()
        while True:
            try:
                self.processOut.emit(next(logText))
            except StopIteration:
                break
        self.finishedOut.emit()
        result_excel = dataCombination.get_excel_filename()
        self.resultXlsOut.emit(result_excel)


class UpdateThread(QThread):
    startOut = pyqtSignal()
    processOut = pyqtSignal(str)
    finishedOut = pyqtSignal()
    resultXlsOut = pyqtSignal(str)

    def __init__(self, datas_file, target_file, res_path, year, month):
        super(UpdateThread, self).__init__()
        self.datasFile = datas_file
        self.targetFile = target_file
        self.year = year
        self.resPath = res_path
        self.month = month

    def run(self):
        self.startOut.emit()
        statsUpdate = StatisticUpdate(self.datasFile, self.targetFile, self.resPath, self.year, self.month)
        logText = statsUpdate.start()
        while True:
            try:
                self.processOut.emit(next(logText))
            except StopIteration:
                break
        self.finishedOut.emit()
        result_excel = statsUpdate.get_excel_filename()
        self.resultXlsOut.emit(result_excel)

