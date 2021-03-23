""" 资源-设备管理 """
# 节点名称
from IP_Intelligent_system.PageObject.login_demo import Login
import pytest
from IP_Intelligent_system.PageObject.page_Resources_Equipment_maintenance import PageEquipmentMaintenance
from IP_Intelligent_system.tool.get_yaml import get_yaml
import allure,os
from IP_Intelligent_system.tool.get_log import GetLogger
log = GetLogger().get_logger()

@allure.feature('设备管理')
class Test_Resources():
    # 默认登陆
    @pytest.mark.usefixtures('driver_get')
    def test_login_01(self,driver_get):
        try:
            Login(driver_get).login()
        except:
            log.error('登陆失败')
            
    @allure.story('进入设备维护页面')
    @pytest.mark.usefixtures('driver_get')
    @pytest.mark.parametrize('data',get_yaml('Equipment_maintenance.yaml')['test_jump'])
    def test_jump_02(self,data,driver_get):
        PageEquipmentMaintenance(driver_get).page_jump()
        try:
            assert PageEquipmentMaintenance(driver_get).page_jump_text() == data['value']
            log.info("正在断言")
        except AssertionError as err:
            log.error(err)
            PageEquipmentMaintenance(driver_get).base_get_image()
            raise
    
    @allure.story('节点名称选择验证-全国')
    @pytest.mark.usefixtures('driver_get')
    @pytest.mark.parametrize('data',get_yaml('Equipment_maintenance.yaml')['test_node_validation'])
    def test_node_validation_03(self,data,driver_get):
        PageEquipmentMaintenance(driver_get).page_node_validation()
        try:
            assert PageEquipmentMaintenance(driver_get).page_node_validation_text() == data['value']
        except AssertionError as err:
            log.error(err)
            PageEquipmentMaintenance(driver_get).base_get_image()
            raise
     
    @allure.story('城市子节点选择-安庆')
    @pytest.mark.usefixtures('driver_get')
    @pytest.mark.parametrize('data',get_yaml('Equipment_maintenance.yaml')['test_node_anqing'])
    def test_node_anqing_04(self,data,driver_get):
        PageEquipmentMaintenance(driver_get).page_node_anqing()
        try:
            assert PageEquipmentMaintenance(driver_get).page_node_anqing_text() == data['value']
        except AssertionError as err:
            PageEquipmentMaintenance(driver_get).base_get_image()
            raise
        
    @allure.story('全国子节点显示')
    @pytest.mark.usefixtures('driver_get')
    @pytest.mark.parametrize('data',get_yaml('Equipment_maintenance.yaml')['test_provinces'])
    def test_provinces_5(self,data,driver_get):
        PageEquipmentMaintenance(driver_get).page_provinces()
        try:
            assert PageEquipmentMaintenance(driver_get).page_provinces_text() == data['values']
        except AssertionError as err:
            log.error(err)
            PageEquipmentMaintenance(driver_get).base_get_image()
            raise
            

    
        
            
if __name__ == "__main__":
    pytest.main(['-svv','-k test_ziyuan.py','--alluredir=../yidong_web/IP_Intelligent_system/report/case_allure'])
    os.system('allure serve ../yidong_web/IP_Intelligent_system/report/case_allure')
#  allure serve ../yidong_web/IP_Intelligent_system/report/case_allure
