""" 前置条件 """
# driver
import pytest
from selenium import webdriver

# driver钩子函数
@pytest.fixture(scope="module",autouse=True)
def driver_get():   
        url = 'http://10.136.107.175:7007/views/login.html'
        driver = None  
        #如果driver不为None
        if driver is None:
            #获取浏览器驱动
            options = webdriver.ChromeOptions()
            options.add_experimental_option('excludeSwitches', ['enable-logging'])
            driver = webdriver.Chrome(options=options)
            #打开网页
            driver.get(url)
            #最大化
            driver.maximize_window()
        yield driver
        if driver:
            driver.quit()
            #清空driver内存
            driver = None