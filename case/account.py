from selenium import webdriver
from time import sleep
from model.login import Login
import unittest

class Account(unittest.TestCase):
    u'''账号信息模块'''
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        login = Login(cls.driver)
        login.loginSuccess()
        cls.driver.find_element_by_class_name('hea-admin-info').click()
        sleep(1)
        cls.driver.execute_script('return document.querySelector("ul.hea-admin-down li")').click()
        sleep(1)

    def upload(self):
        u'''文件上传测试用例'''
        self.driver.execute_script('return document.querySelector(".myset input[type=\'file\']")').send_keys('D:\\Backup\\桌面\\文档\\图片\\1.png')
        sleep(1)
        self.driver.save_screenshot('upload.png')

    @classmethod
    def tearDownClass(cls):
        sleep(5)
        cls.driver.close()