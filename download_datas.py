# -*- coding: utf-8 -*-
"""
Created on Tue Mar  9 13:17:14 2021

@author: whyzzh
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, SessionNotCreatedException
import pandas as pd
import os
import time


DOCTYPE_NUMBER = 3
FIELD_NUMBER = 22


class DataDownload:
    def __init__(self, url, result_path, wait_time, excels_path):
        """
        初始化数据下载设置
        """
        self.url = url
        self.resultPath = result_path
        self.waitTime = wait_time  # 网页响应等待时间
        self.excelsPath = excels_path
        self.additionList = []

    def start(self):
        """运行数据下载程序"""
        yield '设置网页最长等待时间为：{:d}秒'.format(self.waitTime)
        options = webdriver.ChromeOptions()

        # 创建下载excel的文件夹路径
        excels_path = self.resultPath + r'\doc_excels'
        excels_path = excels_path.replace('/', '\\')
        if not os.path.exists(excels_path):
            os.makedirs(excels_path)
            yield 'excels_path路径创建成功！'
        else:
            yield 'excels_path路径已存在，可直接使用'

        # excel文件保存路径可查看
        yield "excels_path"

        # 设置浏览器文件下载默认路径
        prefs = {'download.default_directory': excels_path}
        options.add_experimental_option('prefs', prefs)

        # 设置chrome运行模式为无头模式
        # options.headless = True

        # 添加user-agent
        # userAgent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36'
        # options.add_argument(f'user-agent={userAgent}')

        # 通过service设置chromedriver路径
        driverPath = './chromedriver.exe'
        service = webdriver.ChromeService(executable_path=driverPath)

        # 初始化浏览器设置，并运行浏览器
        # try:
        browser = webdriver.Chrome(options=options, service=service)
        # except:
        #     yield "driver_error"
        #
        #     return
        browser.implicitly_wait(self.waitTime)  # 设置浏览器响应默认等待时间
        yield '打开Incites网页，等待加载中...'

        browser.get(self.url)
        yield '网页加载完成！'

        time.sleep(4)
        cookieNode = browser.find_elements_by_xpath('//button[@id="onetrust-accept-btn-handler"]')
        if len(cookieNode) > 0:
            while True:
                try:
                    cookieNode[0].click()
                    break
                except:
                    time.sleep(1)
                    continue
        try:
            self.click_institution(browser)
            yield '已将 "Results List" 选择为 "Institutions"'

            # 将3种论文类别，22种学科类别下的所有excel下载到保存路径
            for docType_i in range(DOCTYPE_NUMBER):
                yield "正在选择论文类型..."
                cata = self.select_paper_cata(browser, docType_i)
                self.select_field(browser, -1, docType_i)  # field_i等于-1的情况为下载综合排名数据，此时不需选择学科类型
                self.click_cus(browser, -1)

                yield "论文类型已选择为：{:s}".format(cata)
                yield cata + " - All Fields：正在下载excel文件..."

                self.download_excel(browser, excels_path, -1, docType_i)  # 从网页下载excel文件

                yield "{:s} - All Fields：excel文件下载完成".format(cata)
                yield "plus"

                for field_i in range(FIELD_NUMBER):
                    field = self.select_field(browser, field_i, docType_i)
                    self.click_cus(browser, field_i)
                    yield "{:s} - {:s}：正在下载excel文件...".format(cata, field)

                    getNoneFile = self.download_excel(browser, excels_path, field_i, docType_i)
                    if getNoneFile:
                        yield "None"  # 若Excel下载错误则终止进程

                    yield "{:s} - {:s}：excel文件下载完成".format(cata, field)
                    yield "plus"
            yield 'finished_download'

        except TimeoutException:
            yield 'timeout'

        # 关闭浏览器
        try:
            browser.close()
            yield '网页已关闭'
        except:
            yield '网页未打开'

        colleges_addtion = CollegesAddtion(self.excelsPath)
        logText = colleges_addtion.start()
        while True:
            try:
                yield next(logText)
            except StopIteration:
                break
        self.additionList = colleges_addtion.emit_addtion_list()

    def select_paper_cata(self, browser, docType_i):
        """
        将网页左侧的 'Include Results For' 点选为相应的三种类型
        """
        wait = WebDriverWait(browser, self.waitTime)
        wait.until(EC.presence_of_element_located((By.XPATH, '//tr[@class="x-grid-row  x-grid-data-row"]')))

        # 点击 'Include Results For' 下拉菜单
        browser.find_element_by_xpath('//div[@id="s2id_docType"]').click()

        # 点击论文类型
        ins_button_2_list = browser.find_elements_by_class_name('select2-results-dept-0')
        cata_name = ins_button_2_list[docType_i].text
        ins_button_2_list[docType_i].click()
        return cata_name

    def click_institution(self, browser):
        """
        将网页左上角的 'Result List' 点选为 'institutions'
        """
        wait = WebDriverWait(browser, self.waitTime)

        # 点击Result List右侧下拉菜单
        wait.until(EC.presence_of_element_located((By.XPATH, '//tr[@class="x-grid-row  x-grid-data-row"]')))

        browser.find_element_by_xpath('//div[@id="s2id_groupBy"]').click()

        # 点选Institutions选项
        ins_button_2_list = browser.find_elements_by_xpath('//ul[@class="select2-results"]/li')
        ins_button_2_list[2].click()

    def select_field(self, browser, field_i, docType_i):
        """
        依次点选网页左侧的 'Add Filter' -> 'Research Fields' -> 选择学科类型
        """
        if (field_i == -1) and (docType_i == 0):

            return
        wait = WebDriverWait(browser, self.waitTime)

        # 点击Add Filter
        browser.find_element_by_class_name('add-filters').click()
        wait.until(EC.presence_of_element_located((By.XPATH, '//tr[@class="x-grid-row  x-grid-data-row"]')))
        browser.find_element_by_class_name('add-filters').click()

        # 点击Research Fields
        sels = browser.find_elements_by_id('researchFields')
        sels[1].click()

        # 点击学科类型
        wait.until(EC.presence_of_element_located((By.XPATH, '//tr[@class="x-grid-row  x-grid-data-row"]')))
        field_sels = browser.find_elements_by_xpath(
            '//div[@class="popup-wrapper"]//div[@class="checkbox-2columns filter-values"]//label')
        field_name = field_sels[field_i].text
        field_sels[field_i].click()

        if field_i > 0:
            wait.until(EC.presence_of_element_located((By.XPATH, '//tr[@class="x-grid-row  x-grid-data-row"]')))
            field_sels = browser.find_elements_by_xpath(
                '//div[@class="popup-wrapper"]//div[@class="checkbox-2columns filter-values"]//label')
            field_sels[field_i - 1].click()

        return field_name
        # time.sleep(2)

    def click_cus(self, browser, field_i):
        """
        点击网页右下方数据表上端的 'Customize', 并在弹出窗口中点选所有选项
        """
        wait = WebDriverWait(browser, self.waitTime)

        # 点击 'Customize'
        wait.until(EC.presence_of_element_located((By.XPATH, '//tr[@class="x-grid-row  x-grid-data-row"]')))
        browser.find_element_by_class_name('checkbox-indicators').click()

        # 点击弹出选项卡中的顶部两个选项
        if field_i == -1:
            browser.find_element_by_xpath('//div[@class="popup-wrapper"]//label[@id="checkBoxOneLb1"]').click()
            browser.find_element_by_xpath('//div[@class="popup-wrapper"]//label[@id="checkBoxOneLb2"]').click()

        # 点击弹出选项卡中的底部三个选项
        wait.until(EC.element_to_be_clickable((By.XPATH, '//div[@class="popup-wrapper"]//input[@id="radioButtonOne"]')))
        browser.find_element_by_xpath('//div[@class="popup-wrapper"]//input[@id="radioButtonOne"]').click()

        wait = WebDriverWait(browser, self.waitTime)
        wait.until(EC.element_to_be_clickable((By.XPATH, '//div[@class="popup-wrapper"]//input[@id="radioButtonTwo"]')))
        browser.find_element_by_xpath('//div[@class="popup-wrapper"]//input[@id="radioButtonTwo"]').click()

        wait = WebDriverWait(browser, self.waitTime)
        wait.until(EC.element_to_be_clickable((By.XPATH, '//div[@class="popup-wrapper"]//input[@id="radioButtonThree"]')))
        browser.find_element_by_xpath('//div[@class="popup-wrapper"]//input[@id="radioButtonThree"]').click()

        # 点击OK
        browser.find_element_by_xpath('//div[@class="popup-wrapper"]//a[@class="primary-button"]').click()

    def download_excel(self, browser, ex_path, field_i, docType_i):
        """
        点击右上角的下载按钮，下载当前数据的excel表格到默认路径
        """
        wait = WebDriverWait(browser, self.waitTime)

        # 点击下载按钮
        wait.until(EC.presence_of_element_located((By.XPATH, '//tr[@class="x-grid-row  x-grid-data-row"]')))
        browser.find_element_by_xpath('//span[@id="action_export"]').click()
        browser.find_element_by_xpath('//span[@id="action_export"]').click()

        # 在后继弹出的菜单中点击 'XLS'，下载excel文件
        browser.find_element_by_xpath('//div[@class="popup-wrapper"]//li[@id="expXlsBtn"]//a[@href="javascript:void(0);"]').click()

        # excel重命名
        filename_pre = ex_path + r'\IndicatorsExport.xlsx'
        while not os.path.exists(filename_pre):
            time.sleep(0.5)
        time.sleep(1)
        if os.path.getsize(filename_pre) == 0:
            print('excel None - {:d}-{:d}'.format(docType_i + 1, field_i + 2))
            return True
        else:
            filename_new = ex_path + r'\%d-%d' % (docType_i + 1, field_i + 2) + '.xlsx'
            if os.path.exists(filename_new):
                os.remove(filename_new)
            os.rename(filename_pre, filename_new)
            return False


class CollegesAddtion:
    def __init__(self, excels_path):
        self.excelsPath = excels_path
        self.contrast_table = pd.read_excel('schools_contrast.xlsx')  # 高校中英文对照表
        self.resultList = []

    def start(self):
        """合并已下载的所有高校名单，并和现有高校对照表作对比，筛选出新增高校列表"""
        yield '正在筛选新增高校名单...'

        df_list = []
        df_colleges = pd.DataFrame()

        for i in range(FIELD_NUMBER + 1):
            xlsfile = self.excelsPath + '\\1-{:d}.xlsx'.format(i + 1)
            df_i_pre = pd.read_excel(xlsfile, skiprows=5, skipfooter=1)
            df_i = df_i_pre[df_i_pre['Countries/Regions'] == 'CHINA MAINLAND'].loc[:, ['Institutions', 'Countries/Regions']]
            df_list.append(df_i)
            df_colleges = pd.concat(df_list, join='outer')
            # yield 'plus_add'

        df_colleges.drop_duplicates(subset=['Institutions'], keep='first', inplace=True)
        # df_colleges.to_excel('df_colleges.xlsx')
        df_contrast = self.contrast_table[self.contrast_table['国别'] == '中国'].loc[:, ['Institutions', '国别']]
        df_contrast.rename(columns={"国别": "Countries"}, inplace=True)

        df_diff = df_colleges.append(df_contrast)
        df_diff = df_diff.drop_duplicates(subset=['Institutions'], keep=False)
        df_diff = df_diff.drop(df_diff[df_diff['Countries'] == '中国'].index)
        df_diff = df_diff.loc[:, 'Institutions']
        self.resultList = df_diff.values.tolist()
        # df_diff.to_excel('diff.xlsx')
        yield 'addition_completed'

    def emit_addtion_list(self):
        """传递已经筛选好的新增高校list"""
        return self.resultList