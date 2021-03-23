import pytest
from IP_Intelligent_system.PageObject.page_login import PageLogin
from IP_Intelligent_system.tool.get_yaml import get_yaml
import allure,os
from IP_Intelligent_system.tool.get_log import GetLogger
log = GetLogger().get_logger()
@allure.feature('登陆case')
class TestLogin():
    # 登陆case
    @pytest.mark.usefixtures('driver_get')
    @pytest.mark.parametrize('data',get_yaml('login.yaml')['login'])
    @allure.story('验证是否2秒内进入首页')
    def test_login(self,driver_get,data):
        login = PageLogin(driver_get)

        login.page_login(data['username'],data['password'])
        try:
            # 断言两秒内是否找到此元素
            # assert login.page_home_get() == True
            assert 1 == 2
        except AssertionError as error:
            login.page_image_err()
            log.error(error)
            raise
       
    # @pytest.mark.usefixtures('driver_get')
    # @allure.story('错误截图验证')
    # def test_err_demo(self,driver_get):
    #     login = PageLogin(driver_get)
    #     try:
    #         assert 1 == 2
    #     except AssertionError as err:
    #     # except Exception as err:
    #         log.error(err)
    #         login.page_image_err()
    #         raise
            
if __name__ == "__main__":
    pytest.main(['-sv','--alluredir=../yidong_web/IP_Intelligent_system/report/case_allure'])
    # os.system('allure serve ../yidong_web/IP_Intelligent_system/report/case_allure')
#     pass
