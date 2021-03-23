""" 此处封装基类 """
from selenium.webdriver.support.wait import WebDriverWait
import time,allure
from IP_Intelligent_system.tool.get_log import GetLogger

log = GetLogger().get_logger()
class Base:
    
    # 初始化driver
    def __init__(self,driver) -> None:
        self.driver = driver
    
    # 查找元素
    def base_find(self,loc,timeout=30,poll=0.5):
        try:
            log.info('查找元素{}'.format(loc))
            return WebDriverWait(self.driver,
                                timeout=timeout,
                                poll_frequency=poll).until(lambda x:x.find_element(*loc))
        except:
            log.error('{}元素超时,没有获取到此元素'.format(loc))
    # 定位一组元素 
    def base_finds(self,loc,timeout=30,poll=0.5):
        try:
            log.info('查找元素{}'.format(loc))
            return WebDriverWait(self.driver,
                                timeout=timeout,
                                poll_frequency=poll).until(lambda x:x.find_elements(*loc))
        except:
            log.error('{}元素超时,没有获取到此元素'.format(loc))
            
    #获取一组元素文本方法
    def base_get_texts(self,loc):
        log.info('获取{}文本'.format(loc))
        itmes = self.base_finds(loc)
        titles = [item.text for item in itmes]
        return titles
    
    #点击元素
    def base_click(self,loc):
        log.info('点击{}'.format(loc))
        self.base_find(loc).click()
    
    #输入元素
    def base_input(self,loc,value):
        #获取元素
        el = self.base_find(loc)
        #清空
        log.info('清空{}'.format(loc))
        el.clear()
        #输入
        log.info('输入{}'.format(loc))
        el.send_keys(value)
    
    #获取文本方法
    def base_get_text(self,loc):
        log.info('获取{}文本'.format(loc))
        return self.base_find(loc).text

    #截图
    # def base_get_image(self):
    #     log.info('正在截图')
    #     self.driver.get_screenshot_as_file("../yidong_web/IP_Intelligent_system/image/{}.png".
    #                                        format(time.strftime("%Y_%m_%d %H_%M_%S")))
    def base_get_image(self):
        log.info('正在截图')
        # self.driver.get_screenshot_as_file("../yidong_web/IP_Intelligent_system/image/{}.png".
        #                                    format(time.strftime("%Y_%m_%d %H_%M_%S")))
        file_name = "../yidong_web/IP_Intelligent_system/image/{}.png".format(time.strftime("%Y_%m_%d %H_%M_%S"))
        self.driver.save_screenshot(file_name)
        with open(file_name, mode='rb') as f:
            file = f.read()
            allure.attach(file, '异常截图', allure.attachment_type.PNG)
            log.info("页面截图文件保存在：{}".format(file_name))
        
    #弹窗处理，点击确定
    def base_click_ok(self,loc):
        el = self.base_find(loc)
        #点击确定
        el.accept()
    #点击取消
    def base_click_cancel(self,loc):
        el = self.base_find(loc)
        el.dismiss()
    
    #切换iframe
    def base_iframe_to(self,loc):
        el = self.base_find(loc)
        self.driver.switch_to.frame(el)
        
    #窗口切换，获取当前主窗口句柄
    def base_handle_to(self):
        handle = self.driver.current_window_handle
        return handle

    #获取当前所有窗口句柄
    def base_handles_to(self):
        handles = self.driver.window_handles
        for handle in handles:
            if handle != self.base_handle_to():
                self.driver.switch_to_window(handle)
                
    #切换到最初的句柄
    def base_handle_back(self,value):
        self.driver.close()
        self.driver.switch_to_window(value)
    
    #捕获是否找到了元素
    def base_element_is_exp(self, loc):
        try:
            self.base_find(loc,timeout=2)
            return True
        except:
            return False

if __name__ == '__main__':
    pass