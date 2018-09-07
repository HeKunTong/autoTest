from config.index import domain
from time import sleep

class Login:
    def __init__(self, driver):
        self.driver = driver
        self.driver.maximize_window()
        url = domain + '/#/login'
        self.driver.get(url)
        self.driver.implicitly_wait(10)

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

    def loginSuccess(self):
        sleep(1)
        self.__login('*******', '*******')
        modal = self.driver.execute_script('return document.querySelector(".ant-modal")')
        if modal:
            self.driver.execute_script('document.querySelectorAll(".ant-modal .ant-modal-footer button")[1].click()')
        sleep(5)