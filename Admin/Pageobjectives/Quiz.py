from time import sleep
from selenium.webdriver.common.keys import Keys


class Quiz:
    """PageObjectives"""
    QUIZ_MENUITEM_XPATH='//*[@id="root"]/section/aside/div/ul/li[10]/span/a'
    ADD_BTN_XPATH='//*[@id="root"]/section/section/main/div/div/div[1]/div/div[2]/button/span[1]/span'
    SPECIALITY_DROPDOWN_XPATH='//*[@id="basic"]/div[1]/div/div[1]/div[2]/div/div/div[1]/div/div[1]/div[1]'
    SPECIALITY_ITEMS_XPATH="//div[@class=' css-26l3qy-menu']/div/div"
    SUB_SPECIALITY_DROPDOWN_XPATH='//*[@id="basic"]/div[1]/div/div[2]/div[2]/div/div/div[1]/div/div[1]/div[1]'
    SUB_SPECIALITY_ITEMS_XPATH="//div[@class=' css-26l3qy-menu']/div/div"
    TITLE_TXT_XPATH='//*[@id="title"]'
    URL_TXT_XPATH='//*[@id="url"]'
    ENABLE_RADIO_XPATH='//*[@id="basic"]/div[1]/div/div[5]/div[2]/div/div/div[1]/label[1]/span[1]/input'
    DISABLE_RADIO_XPATH='//*[@id="basic"]/div[1]/div/div[5]/div[2]/div/div/div[1]/label[2]/span[1]/input'
    SAVE_BTN_XPATH='//*[@id="basic"]/div[2]/div/div/div/button'

    NAME_LIST = '//Table/tbody/tr/td[2]'
    PAGES = "//ul[@class='ant-pagination ant-table-pagination ant-table-pagination-right']/li"
    NEXT_BTN_XPATH = "//ul[@class='ant-pagination ant-table-pagination ant-table-pagination-right']/li[last()]"

    DELETE_CONFIRM_BUTTON_XPATH="//button[@class='ant-btn ant-btn-primary ant-btn-sm']"


    """Methods"""
    def __init__(self,driver):
        self.driver=driver

    def Click_on_Topics(self):
        self.driver.find_element_by_xpath(self.QUIZ_MENUITEM_XPATH).click()

    def Click_on_Add(self):
        self.driver.find_element_by_xpath(self.ADD_BTN_XPATH).click()

    def Click_on_speciality(self):
        sleep(2)
        self.driver.find_element_by_xpath(self.SPECIALITY_DROPDOWN_XPATH).click()

    def Select_speciality(self,Speciality):
        Names = self.driver.find_elements_by_xpath(self.SPECIALITY_ITEMS_XPATH)
        for name in Names:
            Spec_name=name.text
            if Spec_name==Speciality:
                sleep(2)
                name.click()
                break

    def Click_on_Sub_speciality(self):
        self.driver.find_element_by_xpath(self.SUB_SPECIALITY_DROPDOWN_XPATH).click()

    def Select_Sub_speciality(self, Speciality):
        Names = self.driver.find_elements_by_xpath(self.SUB_SPECIALITY_ITEMS_XPATH)
        for name in Names:
            Spec_name = name.text
            if Spec_name == Speciality:
                sleep(2)
                name.click()
                break

    def Add_Title(self,Title):
        self.driver.find_element_by_xpath(self.TITLE_TXT_XPATH).click()
        self.driver.find_element_by_xpath(self.TITLE_TXT_XPATH).send_keys(Keys.CONTROL + "a")
        self.driver.find_element_by_xpath(self.TITLE_TXT_XPATH).send_keys(Keys.DELETE)
        self.driver.find_element_by_xpath(self.TITLE_TXT_XPATH).send_keys(Title)

    def Add_URL(self,URL):
        self.driver.find_element_by_xpath(self.URL_TXT_XPATH).click()
        self.driver.find_element_by_xpath(self.URL_TXT_XPATH).send_keys(Keys.CONTROL + "a")
        self.driver.find_element_by_xpath(self.URL_TXT_XPATH).send_keys(Keys.DELETE)
        self.driver.find_element_by_xpath(self.URL_TXT_XPATH).send_keys(URL)

    def Select_status_Enable(self,):
        self.driver.find_element_by_xpath(self.ENABLE_RADIO_XPATH).click()

    def Select_status_Disable(self,):
        self.driver.find_element_by_xpath(self.DISABLE_RADIO_XPATH).click()

    def Click_Save(self,):
        self.driver.find_element_by_xpath(self.SAVE_BTN_XPATH).click()

    def Check_Quiz_found(self,Title):
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

    def Click_edit_Quiz(self,Title):
        sleep(2)
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        Page_count = len(self.driver.find_elements_by_xpath(self.PAGES)) - 2

        x = 0
        for j in range(Page_count):
            Names = self.driver.find_elements_by_xpath(self.NAME_LIST)
            for i in range(len(Names)):
                Tit = self.driver.find_element_by_xpath("//Table/tbody/tr[" + str(i + 1) + "]/td[2]").text
                if Tit == Title:
                    self.driver.find_element_by_xpath("//Table/tbody/tr[" + str(i + 1) + "]/td[4]/div/div[1]/button").click()
                    x = 1
            if x == 1:
                break
            else:
                self.driver.find_element_by_xpath(self.NEXT_BTN_XPATH).click()


    def Click_on_Delete_Quiz(self,Topic):
        sleep(2)
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        Page_count = len(self.driver.find_elements_by_xpath(self.PAGES)) - 2

        x = 0
        for j in range(Page_count):
            Names = self.driver.find_elements_by_xpath(self.NAME_LIST)
            for i in range(len(Names)):
                Tit = self.driver.find_element_by_xpath("//Table/tbody/tr[" + str(i + 1) + "]/td[2]").text
                if Tit == Topic:
                    self.driver.find_element_by_xpath("//Table/tbody/tr[" + str(i + 1) + "]/td[4]/div/div[2]/button").click()
                    x=1
            if x == 1:
                break
            else:
                self.driver.find_element_by_xpath(self.NEXT_BTN_XPATH).click()

    def Confirm_delete(self):
        self.driver.find_element_by_xpath(self.DELETE_CONFIRM_BUTTON_XPATH).click()
