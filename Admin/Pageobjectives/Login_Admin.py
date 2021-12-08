from Admin.Utilities.readproperties import ReadConfig


class LoginAdmin:

    """PageObjectives"""
    USERNAME_TXT_ID="email"
    PASSWORD_TXT_ID="password"
    LOGIN_BTN_XPATH='//*[@id="root"]/section/section/main/form/div/div[4]/button'
    LOGOUT_BTN_XPATH='//*[@id="root"]/section/aside/div/ul/li[12]/span/a'

    USERNAME = ReadConfig.getUsername()
    PASSWORD = ReadConfig.getPassword()


    """Methods"""
    def __init__(self,driver):
        self.driver=driver

    def Login_Success(self):
        self.driver.find_element_by_id(self.USERNAME_TXT_ID).send_keys(self.USERNAME)
        self.driver.find_element_by_id(self.PASSWORD_TXT_ID).send_keys(self.PASSWORD)
        self.driver.find_element_by_xpath(self.LOGIN_BTN_XPATH).click()

    def Login_Fail(self,x,y):
        self.driver.find_element_by_id(self.USERNAME_TXT_ID).send_keys(x)
        self.driver.find_element_by_id(self.PASSWORD_TXT_ID).send_keys(y)
        self.driver.find_element_by_xpath(self.LOGIN_BTN_XPATH).click()

    def Logout(self):
        self.driver.find_element_by_xpath(self.LOGOUT_BTN_XPATH).click()






































