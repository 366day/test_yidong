from dyx.web_ZhiNengYunWei.PageObject.LoginPage.LoginPage import Test_在登录界面


def test_登录功能():
    Test_在登录界面().test_打开浏览器()
    Test_在登录界面().test_输入访问地址('http://10.136.107.175:7007/views/login.html')
    Test_在登录界面().test_输入用户名()
    Test_在登录界面().test_输入密码()
    Test_在登录界面().test_点击登录按钮()