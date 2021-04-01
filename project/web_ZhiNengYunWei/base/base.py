from selenium.webdriver.support.wait import WebDriverWait
from web_ZhiNengYunWei.tools.get_log import GetLogger
from selenium import webdriver
import time, allure

log = GetLogger().get_log()

class BaseCase:
    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    driver.get('http://10.136.107.175:7007/views/index.html')

    #使用显示等待定位元素
    def b_find(self, element, timeout=30, poll=0.8):
        try:
            log.info('查找元素{}'.format(element))
            return WebDriverWait(self.driver,timeout,poll).until(lambda x: x.find_element(*element))
        except:
            log.error('{}元素超时,没有获取到此元素'.format(element))

    #定位元素
    # def loc(self,element):
    #     return self.driver.find_element(*element)
    
    # 定位一组元素 
    def b_finds(self,loc,timeout=30,poll=0.8):
        try:
            log.info('查找元素{}'.format(loc))
            return WebDriverWait(self.driver,
                                timeout=timeout,
                                poll_frequency=poll).until(lambda x:x.find_elements(*loc))
        except:
            log.error('{}元素超时,没有获取到此元素'.format(loc))
            
    #获取一组元素文本方法
    def b_get_texts(self,loc):
        log.info('获取{}文本'.format(loc))
        itmes = self.b_finds(loc)
        titles = [item.text for item in itmes]
        return titles

    #点击元素
    def b_click(self, element):
        log.info('点击{}'.format(element))
        self.b_find(element).click()

    # 输入信息
    def b_input(self, element, value):
        log.info('正在定位{}'.format(element))
        el = self.b_find(element)
        log.info('清空{}'.format(element))
        el.clear()
        log.info('输入{}'.format(element))
        el.send_keys(value)

    # 获取元素的文本
    def b_gettext(self, element):
        log.info('获取{}文本'.format(element))
        return self.b_find(element).text

    #切换iframe
    def b_iframe_to(self,loc):
        el = self.b_find(loc)
        self.driver.switch_to.frame(el)
    
    def b_screenshot(self):
        log.info('正在截图')
        FileName = "./web_ZhiNengYunWei/Image/{}.png".format(time.strftime("%Y_%m_%d %H_%M_%S"))
        self.driver.save_screenshot(FileName)
        with open(FileName, mode='rb') as f:
            file = f.read()
            allure.attach(file, '异常截图', allure.attachment_type.PNG)
            log.info("页面截图文件保存在：{}".format(FileName))

    # 捕获是否找到了元素
    def b_exist(self, element):
        try:
            self.b_find(element,timeout=3)
            return True
        except:
            return False
        