from dyx.web_ZhiNengYunWei.BaseCase.BaseCase import BaseCase
from selenium.webdriver.common.by import By
import pytest,os


class Test_在登录界面(BaseCase):

    @pytest.mark.run(1)
    def test_打开浏览器(self):
        pass

    @pytest.mark.run(2)
    def test_输入访问地址(self,url='http://10.136.107.175:7007/views/login.html'):
        self.driver.get(url)

    @pytest.mark.run(3)
    def test_输入用户名(self,txt="dongyanxiong"):
        name=(By.NAME,'username')
        self.input(name,txt)

    @pytest.mark.run(4)
    def test_输入密码(self,txt="AAaa11~~"):
        passwd=(By.NAME,'password')
        self.input(passwd,txt)

    @pytest.mark.run(5)
    def test_点击登录按钮(self):
        login=(By.CLASS_NAME,'el-button.loginbtn.el-button--default.el-button--mini')
        self.click(login)