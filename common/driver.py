#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2019/10/14 23:37
# @Author  : Tang Yiwei
# @Email   : 892398433@qq.com
# @File    : driver.py
# @Software: PyCharm

from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from conf.settings import BASE_PATH,chromeDriverFilePath,firefoxDriverFilePath,ieDriverFilePath,edgeDriverFilePath,operaDriverFilePath
from util.logger import logger

def browser(browser="chrome"):
    """
    :param browser: 默认启动Chrome浏览器
    :return:
    设置 chrome 二进制文件位置 (binary_location)
    添加启动参数 (add_argument)
    添加扩展应用 (add_extension, add_encoded_extension)
    添加实验性质的设置参数 (add_experimental_option)
    设置调试器地址 (debugger_address)

    about:version - 显示当前版本
    about:memory - 显示本机浏览器内存使用状况
    about:plugins - 显示已安装插件
    about:histograms - 显示历史记录
    about:dns - 显示DNS状态
    about:cache - 显示缓存页面
    about:gpu -是否有硬件加速
    about:flags -开启一些插件 //使用后弹出这么些东西：“请小心，这些实验可能有风险”，不知会不会搞乱俺的配置啊！
    chrome://extensions/ - 查看已经安装的扩展

    --headless 无界面运行
    –user-data-dir=”[PATH]” 指定用户文件夹User Data路径，可以把书签这样的用户数据保存在系统分区以外的分区。
    –disk-cache-dir=”[PATH]“ 指定缓存Cache路径
    –disk-cache-size= 指定Cache大小，单位Byte
    –first run 重置到初始状态，第一次运行
    –incognito 隐身模式启动
    –disable-javascript 禁用Javascript
    –omnibox-popup-count=”num” 将地址栏弹出的提示菜单数量改为num个。我都改为15个了。
    –user-agent=”xxxxxxxx” 修改HTTP请求头部的Agent字符串，可以通过about:version页面查看修改效果
    –disable-plugins 禁止加载所有插件，可以增加速度。可以通过about:plugins页面查看效果
    –disable-javascript 禁用JavaScript，如果觉得速度慢在加上这个
    –disable-java 禁用java
    --disable-infobars 禁用浏览器正在被自动化程序控制的提示
    –start-maximized 启动就最大化
    –no-sandbox 取消沙盒模式
    –single-process 单进程运行
    –process-per-tab 每个标签使用单独进程
    –process-per-site 每个站点使用单独进程
    –in-process-plugins 插件不启用单独进程
    –disable-popup-blocking 禁用弹出拦截
    –disable-plugins 禁用插件
    –disable-images 禁用图像
    –incognito 启动进入隐身模式
    –enable-udd-profiles 启用账户切换菜单
    –proxy-pac-url 使用pac代理 [via 1/2]
    –lang=zh-CN 设置语言为简体中文
    –disk-cache-dir 自定义缓存目录
    –disk-cache-size 自定义缓存最大值（单位byte）
    –media-cache-size 自定义多媒体缓存最大值（单位byte）
    –bookmark-menu 在工具 栏增加一个书签按钮
    –enable-sync 启用书签同步
    –single-process 单进程运行Google Chrome
    –start-maximized 启动Google Chrome就最大化
    –disable-java 禁止Java
    –no-sandbox 非沙盒模式运行
    --window-size=1366,768 设置启动窗口大小
    --user-agent="" 设置请求头

    禁用图片加载--->
    prefs = {'profile.default_content_setting_values' : {'images' : 2}}
    禁用浏览器弹窗--->
    prefs = {'profile.default_content_setting_values' : {'notifications' : 2}}
    """
    try:
        if browser.strip().lower() == "chrome":
            chromeOptions = webdriver.ChromeOptions()
            prefs = {
                'profile.default_content_setting_values':
                    {
                        'notifications': 2,#设置不弹出谷歌浏览器左上角提示框
                        # 'images': 2 #禁用图片加载
                    },
                'plugins.plugins_disabled':['Chrome PDF Viewer','Adobe Falsh Player'],#禁用浏览器的PDF和Flash插件
                'download.default_directory': BASE_PATH+r'\testData\download',   #设置项目的默认下载路径
                'credentials_enable_service':False, #设置不弹出保存密码提示
                "profile.password_manager_enabled":False
            }
            chromeOptions.add_experimental_option('prefs', prefs)
            chromeOptions.add_argument("disable-infobars")#禁用浏览器显示正在被自动化程序控制的提示
            chromeOptions.add_argument("--disable-extensions")#禁用扩展插件
            chromeOptions.add_argument("--start-maximized")#启动最大化
            # chromeOptions.add_argument("--headless")#无界面方式运行
            chromeOptions.add_argument("--incognito")#隐身模式
            browser = webdriver.Chrome(executable_path=chromeDriverFilePath,chrome_options=chromeOptions)
        elif browser.strip().lower() == "firefox":
            profile = webdriver.FirefoxProfile()
            # profile.set_preference("permissions.default.stylesheet",2) #禁用CSS
            # profile.set_preference("permissions.default.image",2) #禁用images
            profile.set_preference("dom.ipc.plugins.enabled.libflashplayer.so",False) #禁用Falsh插件
            browser = webdriver.Firefox(executable_path=firefoxDriverFilePath,firefox_profile=profile)
        elif browser.strip().lower() == "ie":
            caps = DesiredCapabilities.INTERNETEXPLORER
            caps['ignoreProtectedModeSettings'] = True #禁用IE保护模式
            browser = webdriver.Ie(executable_path=ieDriverFilePath,capabilities=caps)
        elif browser.strip().lower() == 'edge':
            browser = webdriver.Edge(executable_path=edgeDriverFilePath)
        elif browser.strip().lower() == "opera":
            browser = webdriver.Opera(executable_path=operaDriverFilePath)
        elif browser.strip().lower() == "phantomjs":
            browser = webdriver.PhantomJS() #Selenium已弃用此浏览器
        else:
            print("没有找到浏览器驱动，请检查驱动配置！")
        return browser
    except FileNotFoundError as e:
        pass
    except Exception as e:
        pass

class Browser:

    _instance = None
    _driver = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super.__new__(cls)
        return cls._instance

    def __init__(self):
        pass

    @classmethod
    def get_driver(cls,browser="chrome"):
        if cls._driver is None:
            cls._driver = cls.create_driver(browser)
            logger.info("实例化" + browser + "浏览器")
        return cls._driver

    @classmethod
    def create_driver(cls, browers):
        driver = None
        try:
            if browers.lower() == "chrome":
                driver = webdriver.Chrome(executable_path=chromeDriverFilePath)
            elif browers.lower() == "firfox":
                driver = webdriver.Chrome(executable_path=firefoxDriverFilePath)
            elif browers.lower() == "ie":
                driver = webdriver.Ie(executable_path=ieDriverFilePath)
            elif browers.lower() == "Safari":
                driver = webdriver.Safari(executable_path=None)
            return driver
        except Exception as e:
            logger.error(f'浏览器驱动启动失败 {e}')


if __name__ == "__main__":
    # driver = browser()
    # url = "https://www.baidu.com"
    # driver.get(url)
    # print(driver.title)
    driver = Browser.get_driver()
    driver.get("http://www.baidu.com")
    from time import sleep
    sleep(2)
    driver.quit()
