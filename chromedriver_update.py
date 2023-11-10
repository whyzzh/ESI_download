import os
import re
import sys
import winreg
import zipfile
from pathlib import Path
import requests

loc = Path.cwd()  # 程序所在目录
base_url = 'http://npm.taobao.org/mirrors/chromedriver/'  # chromedriver在国内的镜像网站
version_re = re.compile(r'^[1-9]\d*\.\d*.\d*')  # 匹配前3位版本信息


def get_chrome_version():
    """通过注册表查询Chrome版本信息: HKEY_CURRENT_USER\SOFTWARE\Google\Chrome\BLBeacon: version"""
    try:
        key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, 'SOFTWARE\Google\Chrome\BLBeacon')
        value = winreg.QueryValueEx(key, 'version')[0]
        return version_re.findall(value)[0]
    except WindowsError as e:
        return '0.0.0'  # 没有安装Chrome浏览器


def get_chrome_driver_version():
    try:
        result = os.popen('chromedriver --version').read()
        version = result.split(' ')[1]
        return '.'.join(version.split('.')[:-1])
    except Exception as e:
        return '0.0.0'  # 没有安装ChromeDriver


def get_latest_chrome_driver(chrome_version):
    url = f'{base_url}LATEST_RELEASE_{chrome_version}'
    latest_version = requests.get(url).text
    download_url = f'{base_url}{latest_version}/chromedriver_win32.zip'

    # 下载chromedriver zip文件
    response = requests.get(download_url)
    # loc = root.joinpath('Scripts')
    local_file = loc / 'chromedriver.zip'
    print(local_file)
    with open(local_file, 'wb') as zip_file:
        zip_file.write(response.content)

    # 解压缩zip文件到python安装目录
    f = zipfile.ZipFile(local_file, 'r')
    for file in f.namelist():
        f.extract(file, loc)
    f.close()

    local_file.unlink()  # 解压缩完成后删除zip文件
    print('Update success')


def check_chrome_driver_update():
    chrome_version = get_chrome_version()
    driver_version = get_chrome_driver_version()
    if chrome_version == driver_version:
        print('No need to update')
        return -1
    else:
        try:
            get_latest_chrome_driver(chrome_version)
            return 1
        except Exception as e:
            print(f'Fail to update: {e}')
            return 0


if __name__ == '__main__':
    check_chrome_driver_update()
