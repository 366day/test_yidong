from dyx.web_ZhiNengYunWei.BaseCase.BaseCase import BaseCase
from selenium.webdriver.common.by import By
from selenium import webdriver


# 资源--电路维护界面
class 在电路维护界面(BaseCase):

    def 点击首页登录按钮(self):
        login = (By.CLASS_NAME,'loginBtn___2v65B')
        self.click(login)