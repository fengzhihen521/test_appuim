#上传图片
from app.capability import driver,NoSuchElementException

driver.find_element_by_id('com.tal.kaoyan:id/login_register_text').click()
driver.find_element_by_id('com.tal.kaoyan:id/activity_register_userheader').click()

driver.find_elements_by_id('com.tal.kaoyan:id/item_image')[4].click()
driver.find_element_by_id('com.tal.kaoyan:id/save').click()
