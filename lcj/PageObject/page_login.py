""" 登陆封装 """
from IP_Intelligent_system.base.base import Base
from selenium.webdriver.common.by import By
# import pytest
# 登陆
class PageLogin(Base):
    # 账号
    user = By.CSS_SELECTOR,'[name="username"]'
    # 密码
    pwd = By.CSS_SELECTOR,'[name="password"]'
    # 登陆按钮
    span = By.CSS_SELECTOR,'div button span'
    # 首页获取
    home = By.CSS_SELECTOR,'div a [class="fa fa-home"]'
    # 账号输入
    
    def page_login_user(self,value):
        self.base_input(self.user,value)
    # 密码输入
    def page_login_pwd(self,value):
        self.base_input(self.pwd,value)
    # 点击登陆
    def page_span_click(self):
        self.base_click(self.span)
    # 是否找到首页按钮
    def page_home_get(self):
        return self.base_element_is_exp(self.home)
    # 截图
    def page_image_err(self):
        self.base_get_image()
        
    def page_login(self,user,pwd):
        """ 登陆组合 """
        self.page_login_user(user)
        self.page_login_pwd(pwd)
        self.page_span_click()
    
    