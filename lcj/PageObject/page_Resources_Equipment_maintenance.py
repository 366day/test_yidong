""" 资源 """
# 设备维护

from IP_Intelligent_system.base.base  import Base 
from selenium.webdriver.common.by import By

class PageEquipmentMaintenance(Base):
    """ 公用 """
    # 查询按钮
    page_button_selector = By.XPATH,'//*[text()="查询"]'
    # 查询节点数据
    page_selectors_node = By.CSS_SELECTOR,'[class="el-table_1_column_6   cellclazz"] [class="cell el-tooltip"]'
    
    """ 跳转 """
    # 资源菜单
    resources = By.CSS_SELECTOR,'[class="menu-icon menu_res"]'
    # 设备维护按钮
    maintenance = By.XPATH,'/html/body/div/div[1]/div[2]/ul[2]/li[2]'
    # 设备维护窗口
    maintenance_text = By.CSS_SELECTOR,'[id="resource/res.html"]'
    # 进入设备维护页面步骤
    def page_jump(self):
        # 点击资源菜单
        self.base_click(self.resources)
        # 点击设备维护按钮
        self.base_click(self.maintenance)
    def page_jump_text(self):
        # 获取维护窗口文本
        return self.base_get_text(self.maintenance_text)
    
    """ 节点名称选择验证 全国 """
    # 表单
    iframe_maintenance = By.CSS_SELECTOR,'[src="resource/res.html"]'
    # 节点名称
    node_id = By.CSS_SELECTOR,'div [class="vue-treeselect__input"]'
    # 选择全国
    add_chinese = By.CSS_SELECTOR,'[class="vue-treeselect__label"]'
    # 验证
    add_chinese_text = By.CSS_SELECTOR,'[class="row-4 el-row"] [class="vue-treeselect__single-value"]'
    # 节点名称选择步骤
    def page_node_validation(self):
        # 进入iframe表单
        self.base_iframe_to(self.iframe_maintenance)
        # 点击节点名称
        self.base_click(self.node_id)
        # 选择全国
        self.base_click(self.add_chinese)
    def page_node_validation_text(self):
        # 获取节点文本
        return self.base_get_text(self.add_chinese_text)

    """ 城市子节点名称选择步骤 安庆"""   
    # #  # 点击节点名称
    #     self.base_click(self.node_id)
    # 全国左侧下拉框
    node_add_chinese = By.CSS_SELECTOR,'[data-id="NOD9999"] div svg'
    # 安徽左侧下拉框
    node_anhui = By.CSS_SELECTOR,'[data-id="NOD0012"] [class="vue-treeselect__option-arrow-container"]'
    # 选择安庆节点
    node_anqing = By.CSS_SELECTOR,'[data-id="NOD0133"] [class="vue-treeselect__label"]'
    # 验证文本
    add_anqing_text = By.CSS_SELECTOR,'[class="row-4 el-row"] [class="vue-treeselect__single-value"]'
    def page_node_anqing(self):
        # 选择节点
        self.base_click(self.node_id)
        # 选择全国节点下拉框
        self.base_click(self.node_add_chinese)
        # 选择安徽节点下拉框
        self.base_click(self.node_anhui)
        # 选择安庆节点
        self.base_click(self.node_anqing)
    def page_node_anqing_text(self):
        return self.base_get_text(self.add_anqing_text)
    
    """ 全国子节点显示 """
    # 全国按钮下拉框
    add_drop_down = By.CSS_SELECTOR,' [data-id="NOD9999"] [class="vue-treeselect__option-arrow-container"]'
    # 所有省份text
    add_province = By.CSS_SELECTOR,'[class="vue-treeselect__label"]'
    # 子节点显示验证
    def page_provinces(self):
        # 进入iframe表单
        # self.base_iframe_to(self.iframe_maintenance)
        # 点击节点名称
        self.base_click(self.node_id)
        # 点击全国下拉框按钮
        self.base_click(self.add_drop_down)
        # 选择安徽节点下拉框
        self.base_click(self.node_anhui)
    def page_provinces_text(self):
        return self.base_get_texts(self.add_province)