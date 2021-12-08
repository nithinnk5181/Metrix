
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class Specialities:
    """PageObjectives"""
    SPECIALITIES_MENUITEM_XPATH='//*[@id="root"]/section/aside/div/ul/li[3]/span/a'
    ADD_BTN_XPATH='//*[@id="root"]/section/section/main/div/div/div[1]/div/div[2]/button/span[1]/span'
    NAME_INPUT_XPATH='//*[@id="spec_name"]'
    SAVE_BTN_XPATH='//*[@id="basic"]/div[2]/div/div/div/div/button'

    NAME_LIST = '//Table/tbody/tr/td[2]'
    PAGES = "//ul[@class='ant-pagination ant-table-pagination ant-table-pagination-right']/li"
    NEXT_BTN_XPATH = "//ul[@class='ant-pagination ant-table-pagination ant-table-pagination-right']/li[last()]"
    CONFIRM_DELETE_BTN_XPATH="//button[@class='ant-btn ant-btn-primary ant-btn-sm']/span"
    DECLAIN_DELETE_BTN_XPATH="//button[@class='ant-btn ant-btn-sm']/span"

    """Methods"""

    def __init__(self,driver):
        self.driver=driver

    def Click_on_Specialities(self):
        self.driver.find_element_by_xpath(self.SPECIALITIES_MENUITEM_XPATH).click()

    def Click_on_Add(self):
        self.driver.find_element_by_xpath(self.ADD_BTN_XPATH).click()

    def Remove_name(self):
        sleep(1)
        self.driver.find_element_by_xpath(self.NAME_INPUT_XPATH).click()
        self.driver.find_element_by_xpath(self.NAME_INPUT_XPATH).send_keys(Keys.CONTROL + "a")
        self.driver.find_element_by_xpath(self.NAME_INPUT_XPATH).send_keys(Keys.DELETE)

    def Add_name(self,Spec_name):
        sleep(1)
        self.driver.find_element_by_xpath(self.NAME_INPUT_XPATH).click()
        self.driver.find_element_by_xpath(self.NAME_INPUT_XPATH).send_keys(Keys.CONTROL + "a")
        self.driver.find_element_by_xpath(self.NAME_INPUT_XPATH).send_keys(Keys.DELETE)
        sleep(1)
        self.driver.find_element_by_xpath(self.NAME_INPUT_XPATH).send_keys(Spec_name)

    def Click_Save(self):
        self.driver.find_element_by_xpath(self.SAVE_BTN_XPATH).click()

    def Check_Speciality_name(self,Spec_name):
        sleep(3)
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        Page_count=len(self.driver.find_elements_by_xpath(self.PAGES))-2

        x=0
        for j in range(Page_count):
            Names=self.driver.find_elements_by_xpath(self.NAME_LIST)
            for i in range(len(Names)):
                Speciality_name=self.driver.find_element_by_xpath("//Table/tbody/tr["+str(i+1)+"]/td[2]").text
                if Speciality_name==Spec_name:
                    x = 1
                    return x
            if x==1:
                break

            else:
                self.driver.find_element_by_xpath(self.NEXT_BTN_XPATH).click()

    def Click_Sub_spacialities(self,Spec_name):
        sleep(2)
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        Page_count = len(self.driver.find_elements_by_xpath(self.PAGES)) - 2

        x = 0
        for j in range(Page_count):
            Names = self.driver.find_elements_by_xpath(self.NAME_LIST)
            for i in range(len(Names)):
                Speciality_name = self.driver.find_element_by_xpath("//Table//tr[" + str(i + 1) + "]/td[2]").text
                if Spec_name == Speciality_name:
                    x = 1
                    self.driver.find_element_by_xpath("//Table/tbody/tr[" + str(i + 1) + "]/td[3]/div/div[3]/button/a").click()
                    break
            if x==1:

                break
            else:
                self.driver.find_element_by_xpath(self.NEXT_BTN_XPATH).click()


    def Click_Edit_Sub_spacialities(self,Sub_Speciality_name):
        sleep(2)
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        Page_count = len(self.driver.find_elements_by_xpath(self.PAGES)) - 2

        x = 0
        for j in range(Page_count):
            Names = self.driver.find_elements_by_xpath(self.NAME_LIST)
            for i in range(len(Names)):
                Sub_spec_Name = self.driver.find_element_by_xpath("//Table//tr[" + str(i + 1) + "]/td[2]").text
                if Sub_spec_Name == Sub_Speciality_name:
                    x = 1
                    self.driver.find_element_by_xpath("//Table/tbody/tr[" + str(i + 1) + "]/td[3]/div/div[1]/button/span").click()
                    break
            if x==1:
                break
            else:
                self.driver.find_element_by_xpath(self.NEXT_BTN_XPATH).click()

    def Click_Edit_spacialities(self,Speciality_name):
        sleep(2)
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        Page_count = len(self.driver.find_elements_by_xpath(self.PAGES)) - 2

        x = 0
        for j in range(Page_count):
            Names = self.driver.find_elements_by_xpath(self.NAME_LIST)
            for i in range(len(Names)):
                Spec_Name = self.driver.find_element_by_xpath("//Table//tr[" + str(i + 1) + "]/td[2]").text
                if Spec_Name == Speciality_name:
                    x = 1
                    self.driver.find_element_by_xpath("//Table/tbody/tr[" + str(i + 1) + "]/td[3]/div/div[1]/button/span/span").click()
                    break
            if x == 1:
                break
            else:
                self.driver.find_element_by_xpath(self.NEXT_BTN_XPATH).click()

    def Click_Delete_spacialities(self,Speciality_name):
        sleep(2)
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        Page_count = len(self.driver.find_elements_by_xpath(self.PAGES)) - 2

        x = 0
        for j in range(Page_count):
            Names = self.driver.find_elements_by_xpath(self.NAME_LIST)
            for i in range(len(Names)):
                Spec_Name = self.driver.find_element_by_xpath("//Table//tr[" + str(i + 1) + "]/td[2]").text
                if Spec_Name == Speciality_name:
                    x = 1
                    self.driver.find_element_by_xpath("//Table/tbody/tr[" + str(i + 1) + "]/td[3]/div/div[2]/button/span/span").click()
                    break
            if x == 1:
                break
            else:
                self.driver.find_element_by_xpath(self.NEXT_BTN_XPATH).click()

    def Confirm_delete(self):
        element = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, self.CONFIRM_DELETE_BTN_XPATH)))
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        actions.click().perform()

    def Declain_delete(self):
        element = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, self.DECLAIN_DELETE_BTN_XPATH)))
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        actions.click().perform()

    def Click_Delete_Sub_spacialities(self,Sub_Speciality_name):
        sleep(2)
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        Page_count = len(self.driver.find_elements_by_xpath(self.PAGES)) - 2

        x = 0
        for j in range(Page_count):
            Names = self.driver.find_elements_by_xpath(self.NAME_LIST)
            for i in range(len(Names)):
                Sub_spec_Name = self.driver.find_element_by_xpath("//Table//tr[" + str(i + 1) + "]/td[2]").text
                if Sub_spec_Name == Sub_Speciality_name:
                    x = 1
                    self.driver.find_element_by_xpath("//Table/tbody/tr[" + str(i + 1) + "]/td[3]/div/div[2]/button/span").click()
                    break
            if x == 1:
                break
            else:
                self.driver.find_element_by_xpath(self.NEXT_BTN_XPATH).click()
