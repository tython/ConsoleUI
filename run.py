#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 202/02/07 18:48
# @Author  : Tang Yiwei
# @Email   : 892398433@qq.com
# @File    : run.py
# @Software: PyCharm

import sys
import pytest
import argparse
from selenium import webdriver
import conf.global_variable as gd
from conf.settings import HUB_ADDRES,chromeDriverFilePath,ieDriverFilePath,firefoxDriverFilePath,edgeDriverFilePath,operaDriverFilePath


def get_args():
    """命令行参数解析"""
    parser = argparse.ArgumentParser(description=u'可选择参数：')
    parser.add_argument('-e', '--environment', choices=['preview', 'product','testing','staging'],
                        default='product', help=u'预发布环境preview，线上环境product,testing环境testing，staging环境staging')
    parser.add_argument('-d', '--driver_name', choices=['chrome', 'firefox', 'edge', 'opera','ie'],
                        default='chrome', help=u'选择测试的浏览器["chrome", "firefox", "edge", "opera", "ie"]')
    parser.add_argument('-a', '--address', choices=['local', 'remote'],
                        default='local', help=u'选择在本地运行或者远程运行["local", "remote"]')
    args = parser.parse_args()
    if args.environment in ('pre', 'preview'):
        print("测试预发布环境")
        gd.set_value('environment', 'preview')
        gd.set_value('site', 'https://pek2console3.qingcloud.com/login')
    elif args.environment in ('pro', 'product'):
        print("测试qingcloud线上环境")
        gd.set_value('environment', 'product')
        gd.set_value('site', 'https://console.qingcloud.com/login')
    elif args.environment in ('test', 'testing'):
        print("测试testing环境")
        gd.set_value('environment', 'testing')
        gd.set_value('site', 'http://console.qingcloud-portal.com/login')
    elif args.environment in ('stag', 'staging'):
        print("测试staging环境")
        gd.set_value('environment', 'staging')
        gd.set_value('site', 'http://console.portal.staging.com/login')
    else:
        print(u"请输入preview/product/testing/staging")
        exit()
    if args.driver_name in ('chrome'):
        print("测试谷歌浏览器")
        gd.set_value('driver_name', 'chrome')
    elif args.driver_name in ('firefox'):
        print("测试火狐浏览器")
        gd.set_value('driver_name', 'firefox')
    elif args.driver_name in ('edge'):
        print("测试edge浏览器")
        gd.set_value('driver_name', 'edge')
    elif args.driver_name in ('ie'):
        print("测试ie浏览器")
        gd.set_value('driver_name', 'ie')
    else:
        print(u"请输入chrome/firefox/edge")
        exit()
    if args.address in ('local'):
        print(u"使用本地浏览器进行测试")
        gd.set_value('run_addres','local')
    elif args.address in ('remote'):
        print(u"使用远程浏览器进行测试")
        gd.set_value('run_addres', 'remote')
    else:
        print(u"请输入local/remote")
        exit()

def set_driver(driver_name,run_addres):
    """设置driver"""
    global driver
    if driver_name.strip().lower() == "chrome":
        if run_addres == "remote":
            driver = webdriver.Remote(
                command_executor=HUB_ADDRES,
                desired_capabilities={
                    "browserName": "chrome",
                    "video": "True",
                    "platform": "ANY"
                }
            )
            print("当前会话ID:",driver.session_id)
            gd.set_value('driver', driver)
        else:
            chrome_options = webdriver.ChromeOptions()
            chrome_options.add_argument('--start-maximized')  # 浏览器最大化
            chrome_options.add_argument('--disable-infobars')  # 不提醒chrome正在受自动化软件控制
            prefs = {
                'profile.default_content_setting_values':
                    {
                        'notifications': 2,  # 设置不弹出谷歌浏览器左上角提示框
                        # 'images': 2 #禁用图片加载
                    },
                'plugins.plugins_disabled': ['Chrome PDF Viewer', 'Adobe Falsh Player'],  # 禁用浏览器的PDF和Flash插件
                'download.default_directory': gd.get_value('download_path'),  # 设置项目的默认下载路径
                'credentials_enable_service': False,  # 设置不弹出保存密码提示
                "profile.password_manager_enabled": False
            }
            chrome_options.add_experimental_option('prefs', prefs)  # 设置默认下载路径
            chrome_options.add_argument("disable-infobars")  # 禁用浏览器显示正在被自动化程序控制的提示
            chrome_options.add_argument("--disable-extensions")  # 禁用扩展插件
            chrome_options.add_argument("--start-maximized")  # 启动最大化
            # chrome_options.add_argument("--headless") # 无界面方式运行
            chrome_options.add_argument("--incognito")  # 隐身模式
            chrome_options.add_argument(r'--user-data-dir={}'.format(gd.get_value('user_data')))  # 设置用户文件夹，可免登陆
            driver = webdriver.Chrome('{}\\drivers\\chrome\\chromedriver.exe'.format(gd.get_value('root_path')), options=chrome_options)
            print("当前会话ID:", driver.session_id)
            gd.set_value('driver', driver)
    elif driver_name.strip().lower() == "firefox":
        if run_addres == "remote":
            driver = webdriver.Remote(
                command_executor=HUB_ADDRES,
                desired_capabilities={
                    "browserName": "firefox",
                    "video": "True",
                    "platform": "ANY"
                }
            )
            print("当前会话ID:", driver.session_id)
            gd.set_value('driver', driver)
        else:
            profile = webdriver.FirefoxProfile()
            # profile.set_preference("permissions.default.stylesheet",2) #禁用CSS
            # profile.set_preference("permissions.default.image",2) #禁用images
            profile.set_preference('network.proxy.type', 0)  # firefox设置代理(默认是0，就是直接连接；1就是手工配置代理)
            profile.set_preference('browser.download.dir', gd.get_value('download_path'))  # 设置下载路径
            profile.set_preference('browser.download.folderList', 2)  # 设置成2表示使用自定义下载路径；设置成0表示下载到桌面；设置成1表示下载到默认路径
            profile.set_preference('browser.download.manager.showWhenStarting', False)  # 在开始下载时是否显示下载管理器
            profile.set_preference("dom.ipc.plugins.enabled.libflashplayer.so", False)  # 禁用Falsh插件
            profile.set_preference("intl.accept_languages", "zh-CN")  # 设置浏览器语言
            options = webdriver.FirefoxOptions()
            options.add_argument('--headless')  # 无界面方式运行
            driver = webdriver.Firefox(executable_path=firefoxDriverFilePath, firefox_profile=profile)
            print("当前会话ID:", driver.session_id)
            gd.set_value('driver', driver)
    elif driver_name.strip().lower() == "ie":
        from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
        caps = DesiredCapabilities.INTERNETEXPLORER
        caps['ignoreProtectedModeSettings'] = True  # 禁用IE保护模式
        driver = webdriver.Ie(executable_path=ieDriverFilePath, capabilities=caps)
        print("当前会话ID:", driver.session_id)
        gd.set_value('driver', driver)
    elif driver_name.strip().lower() == 'edge':
        driver = webdriver.Edge(executable_path=edgeDriverFilePath)
        print("当前会话ID:", driver.session_id)
        gd.set_value('driver', driver)
    elif driver_name.strip().lower() == "opera":
        driver = webdriver.Opera(executable_path=operaDriverFilePath)
        print("当前会话ID:", driver.session_id)
        gd.set_value('driver', driver)
    elif driver_name.strip().lower() == "phantomjs":
        driver = webdriver.PhantomJS()  # Selenium已弃用此浏览器
        print("当前会话ID:", driver.session_id)
        gd.set_value('driver', driver)
    else:
        print("没有找到浏览器驱动，请检查驱动配置！")

def write_environment_properties():
    """写入当前测试的环境变量信息到allure配置文件"""
    global driver
    with open('./results/environment.properties',mode='w',encoding='utf-8')as f:
        f.writelines(f"Browser.Version={driver.capabilities}\n")
        f.writelines(f"test.environment={gd.global_dict.get('environment')}\n")
        f.writelines(f"testUrl={gd.global_dict.get('site')}\n")
        f.writelines(f"python.Version={sys.version}\n")

def main():
    """运行pytest命令启动测试"""
    pytest.main(['-v', '-s', './script/', '--html=report/pytest-report/reports.html', '--self-contained-html','--alluredir=./results'])

def allure_report():
    """生成allure测试报告"""
    import os
    os.system("allure generate ./results/ -o ./report/allure-report --clean")
    os.system("allure open -h 127.0.0.1 -p 8883 ./report/")

if __name__ == '__main__':
    gd.init()  # 初始化全局变量
    get_args()  # 命令行参数解析
    # log = Logger('szh')  # 初始化log配置
    driver_name = gd.get_value('driver_name')
    run_addres = gd.get_value('run_addres')
    set_driver(driver_name,run_addres)  # 初始化driver
    write_environment_properties()
    main()  # 运行pytest测试集
    # gd.get_value('driver').quit()  # 关闭selenium driver
    # allure_report()
