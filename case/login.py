from selenium import webdriver
from time import sleep
from config.index import domain
import unittest

class Login(unittest.TestCase):
    u'''登录模块'''
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        # 窗口最大化
        cls.driver.maximize_window()
        url = domain + '/#/login'
        cls.driver.get(url)
        cls.driver.implicitly_wait(10)

    def __login(self, account, password):
        sleep(1)
        inputEmail = self.driver.find_element_by_id('inputEmail')
        inputEmail.clear()
        inputEmail.send_keys(account)
        sleep(1)
        inputPassword = self.driver.find_element_by_id('inputPassword')
        inputPassword.clear()
        inputPassword.send_keys(password)
        sleep(1)
        submit = self.driver.find_element_by_id('submit')
        submit.click()
        sleep(1)

    # case: 请输入用户名
    def inputUserName(self):
        u'''请输入用户名测试用例'''
        sleep(1)
        self.__login('', '')
        errMsg = self.driver.find_element_by_id('bot_err').text
        self.assertEquals(u'请输入用户名!', errMsg)

    # case: 用户不存在
    def userNotExist(self):
        u'''用户不存在测试用例'''
        sleep(1)
        self.__login('1161709455!', '123456')
        errMsg = self.driver.find_element_by_id('bot_err').text
        self.assertEquals(u'用户名不存在!', errMsg)

    # case: 用户名或密码输入有误!
    def inCorrectUser(self):
        u'''账号密码错误测试用例'''
        sleep(1)
        self.__login('18959261286', '111111')
        errMsg = self.driver.find_element_by_id('bot_err').text
        self.assertEquals(u'用户名或密码输入有误!', errMsg)

    # case: 登录成功
    def loginSuccess(self):
        u'''账号密码错误测试用例'''
        sleep(1)
        self.__login('18959261286', '123456')
        modal = self.driver.execute_script('return document.querySelector(".ant-modal")')
        if modal:
            self.driver.execute_script('document.querySelectorAll(".ant-modal .ant-modal-footer button")[1].click()')
        sleep(3)
        url = self.driver.current_url
        self.assertEquals(domain + '/#/', url)

    @classmethod
    def tearDownClass(cls):
        sleep(2)
        cls.driver.close()