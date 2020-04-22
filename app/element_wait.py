#显示等待
from app.kyb_login import driver
from selenium.webdriver.support.ui import WebDriverWait #导入显示等待

WebDriverWait(driver,3).until(lambda x:x.find_element_by_id('com.tal.kaoyan:id/mainactivity_button_forum')) #显示等待
driver.find_element_by_id('com.tal.kaoyan:id/mainactivity_button_forum').click()
