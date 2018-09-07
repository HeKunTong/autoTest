from selenium import webdriver
from selenium.webdriver import ActionChains
from time import sleep
from model.login import Login
import unittest

class FileArea(unittest.TestCase):
    u'''文件区域模块'''
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        login = Login(cls.driver)
        login.loginSuccess()
        # 在会话框输入林靖
        search = cls.driver.execute_script('return document.querySelector(".indexsection-friends-search input")')
        search.clear()
        search.send_keys('林靖')
        sleep(1)
        # 选择与林靖会话
        cls.driver.execute_script('return document.querySelector("ul.indexsection-friends-ul li")').click()
        sleep(1)
        # 点击常用图片
        cls.driver.execute_script('return document.querySelector(".contact-send-tools img[src=\'/static/images/contact_img_file_list.png\']")').click()
        sleep(1)
        # 点击我的存储
        cls.driver.execute_script('return document.querySelectorAll(".contact-imglist>.qqface-title>.item")[2]').click()
        sleep(1)

    def upload(self):
        u'''文件上传测试用例'''
        upload = self.driver.execute_script('return document.querySelector(".upload-mix-input")')
        upload.send_keys('D:\\Backup\\桌面\文档\\消息记录处理.doc')
        sleep(2)

    def edit(self):
        u'''修改文件测试用例'''
        dom = self.driver.execute_script('return document.querySelector(".contact-imglist-img[style=\'display: block;\'] .item")')
        ActionChains(self.driver).move_to_element(dom).perform()
        sleep(1)
        self.driver.execute_script('return document.querySelector(".contact-imglist-img[style=\'display: block;\'] .item i.edit")').click()
        file = self.driver.execute_script('return document.querySelector(".contact-imglist-img[style=\'display: block;\'] .item .edit-name")')
        file.clear()
        filename = 'test'
        file.send_keys(filename)
        self.driver.execute_script('return document.querySelector(".contact-imglist>.qqface-title>.item.active")').click()
        sleep(2)
        value = self.driver.execute_script('return document.querySelector(".contact-imglist-img[style=\'display: block;\'] .item .tit")').text
        self.assertEqual(value, filename)

    @classmethod
    def tearDownClass(cls):
        sleep(5)
        cls.driver.close()