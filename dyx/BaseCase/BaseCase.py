from selenium import webdriver


class BaseCase():
    driver = webdriver.Chrome()
    driver.maximize_window()

    def loc(self,element):
        return self.driver.find_element(*element)

    def click(self,element):
        self.loc(element).click()

    def input(self,element,text):
        self.loc(element).send_keys(*text)

    def GetText(self,element):
        return self.loc(element).text