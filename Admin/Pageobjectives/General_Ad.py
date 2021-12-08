from time import sleep
from selenium.webdriver.common.keys import Keys
import datetime

class General_Ad:
    """Pageobjectives"""
    GENERAL_AD_MENUITEM_XPATH='//*[@id="root"]/section/aside/div/ul/li[7]/span/a'
    ADD_BTN_XPATH='//*[@id="root"]/section/section/main/div/div/div[1]/div/div[2]/button/span[1]/span'
    TITLE_TXT_XPATH='//*[@id="title"]'
    URL_TXT_XPATH='//*[@id="url"]'
    IMAGE_XPATH='//*[@id="image"]'
    ENABLE_RADIO_XPATH='//*[@id="basic"]/div[1]/div/div[4]/div[2]/div/div/div/label[1]/span[1]/input'
    DISABLE_RADIO_XPATH='//*[@id="basic"]/div[1]/div/div[4]/div[2]/div/div/div/label[2]/span[1]/input'
    SAVE_BTN_XPATH='//*[@id="btn"]'

    NAME_LIST = '//Table/tbody/tr/td[2]'
    PAGES = "//ul[@class='ant-pagination ant-table-pagination ant-table-pagination-right']/li"
    NEXT_BTN_XPATH = "//ul[@class='ant-pagination ant-table-pagination ant-table-pagination-right']/li[last()]"

    DELETE_CONFIRM_BUTTON_XPATH="//button[@class='ant-btn ant-btn-primary ant-btn-sm']"



    """Methods"""
    def __init__(self,driver):
        self.driver=driver

    def Click_on_General_ad(self):
        self.driver.find_element_by_xpath(self.GENERAL_AD_MENUITEM_XPATH).click()

    def Click_on_Add(self):
        self.driver.find_element_by_xpath(self.ADD_BTN_XPATH).click()

    def Add_Title(self,Title):
        self.driver.find_element_by_xpath(self.TITLE_TXT_XPATH).click()
        self.driver.find_element_by_xpath(self.TITLE_TXT_XPATH).send_keys(Keys.CONTROL + "a")
        self.driver.find_element_by_xpath(self.TITLE_TXT_XPATH).send_keys(Keys.DELETE)
        self.driver.find_element_by_xpath(self.TITLE_TXT_XPATH).send_keys(Title)

    def Add_Url(self,Url):
        self.driver.find_element_by_xpath(self.URL_TXT_XPATH).click()
        self.driver.find_element_by_xpath(self.URL_TXT_XPATH).send_keys(Keys.CONTROL + "a")
        self.driver.find_element_by_xpath(self.URL_TXT_XPATH).send_keys(Keys.DELETE)
        self.driver.find_element_by_xpath(self.URL_TXT_XPATH).send_keys(Url)

    def Add_Image(self,Image):
        self.driver.find_element_by_xpath(self.IMAGE_XPATH).send_keys(Image)

    def Enable_status(self):
        self.driver.find_element_by_xpath(self.ENABLE_RADIO_XPATH).click()

    def Disable_status(self):
        self.driver.find_element_by_xpath(self.DISABLE_RADIO_XPATH).click()

    def Click_save(self):
        self.driver.find_element_by_xpath(self.SAVE_BTN_XPATH).click()

    def Check_Ad_found(self,Title):
        sleep(2)
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        Page_count=len(self.driver.find_elements_by_xpath(self.PAGES))-2

        x=0
        for j in range(Page_count):
            Names=self.driver.find_elements_by_xpath(self.NAME_LIST)
            for i in range(len(Names)):
                Tit=self.driver.find_element_by_xpath("//Table/tbody/tr["+str(i+1)+"]/td[2]").text
                if Tit==Title:
                    x = 1
                    return x
            if x==1:
                break
            else:
                self.driver.find_element_by_xpath(self.NEXT_BTN_XPATH).click()


    def Click_Edit_ad(self,Title):
        sleep(2)
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        Page_count = len(self.driver.find_elements_by_xpath(self.PAGES)) - 2

        x = 0
        for j in range(Page_count):
            Names = self.driver.find_elements_by_xpath(self.NAME_LIST)
            for i in range(len(Names)):
                Tit = self.driver.find_element_by_xpath("//Table/tbody/tr[" + str(i + 1) + "]/td[2]").text
                if Tit == Title:
                    self.driver.find_element_by_xpath("//Table/tbody/tr[" + str(i + 1) + "]/td[3]//div/div[1]/button").click()
                    x = 1
            if x == 1:
                break
            else:
                self.driver.find_element_by_xpath(self.NEXT_BTN_XPATH).click()

    def Click_Delete_ad(self,Title):
        sleep(2)
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        Page_count = len(self.driver.find_elements_by_xpath(self.PAGES)) - 2

        x = 0
        for j in range(Page_count):
            Names = self.driver.find_elements_by_xpath(self.NAME_LIST)
            for i in range(len(Names)):
                Tit = self.driver.find_element_by_xpath("//Table/tbody/tr[" + str(i + 1) + "]/td[2]").text
                if Tit == Title:
                    self.driver.find_element_by_xpath("//Table/tbody/tr[" + str(i + 1) + "]/td[3]//div/div[2]/button").click()
                    x = 1
            if x == 1:
                break
            else:
                self.driver.find_element_by_xpath(self.NEXT_BTN_XPATH).click()

    def Confirm_delete(self):
        self.driver.find_element_by_xpath(self.DELETE_CONFIRM_BUTTON_XPATH).click()

















