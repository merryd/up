# coding=utf-8

from appium import webdriver

import time

desired_caps = {

                'platformName': 'Android',

                'deviceName': 'emulator-5554 ',

                'platformVersion': '19',

               # 'app':'D:\shoujitaobao_160',

                'appPackage': 'com.taobao.taobao',

                'appActivity': 'com.taobao.tao.welcome.Welcome',

                'unicodeKeyboard': True,

                'resetKeyboard': True  #隐藏键盘

                }

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)

# 休眠五秒等待页面加载完成

time.sleep(10)

driver.find_element_by_id("com.taobao.taobao:id/home_searchedit").click()

time.sleep(5)

driver.find_element_by_id("com.taobao.taobao:id/searchEdit").click()

driver.find_element_by_id("com.taobao.taobao:id/searchEdit").send_keys(u"零食")

driver.quit()