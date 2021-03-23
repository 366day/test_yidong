
from IP_Intelligent_system import PageObject
from IP_Intelligent_system.base.base import Base


class Login(Base):
    def login(self):
        self.base_input(PageObject.user,'wangwen')
        self.base_input(PageObject.pwd,'2020WW_tc#')
        self.base_click(PageObject.span)