
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class Category:
    """PageObjectives"""
    CATEGORY_MENUITEM_XPATH='//*[@id="root"]/section/aside/div/ul/li[4]/span/a'
    ADD_BUTTON_XPATH='//*[@id="root"]/section/section/main/div/div/div[1]/div/div[2]/button/span[1]/span'
    NAME_TXT_XPATH="//input[@class='ant-input'][@name='title']"
    FILE_BTN_NAME='image'
    SAVE_BUTTON_XPATH='/html/body/div[2]/div/div[2]/div/div/div[2]/form/div[2]/div/div/div/button'

    NAME_LIST='//Table/tbody/tr/td[2]'
    PAGES="//ul[@class='ant-pagination ant-table-pagination ant-table-pagination-right']/li"
    NEXT_BTN_XPATH="//ul[@class='ant-pagination ant-table-pagination ant-table-pagination-right']/li[last()]"

    DELETE_CONFIRM_BTN_XPATH="//div/button[@class='ant-btn ant-btn-primary ant-btn-sm']"
    DELETE_REJECT_BTN_XPATH="//div/button[@class='ant-btn ant-btn-sm']"




    """Methods"""

    def __init__(self,driver):
        self.driver=driver

    def Click_on_Category(self):
        self.driver.find_element_by_xpath(self.CATEGORY_MENUITEM_XPATH).click()

    def Click_on_add(self):
        self.driver.find_element_by_xpath(self.ADD_BUTTON_XPATH).click()


    def Add_Name(self,Cat):
        self.driver.find_element_by_xpath(self.NAME_TXT_XPATH).click()
        sleep(1)
        self.driver.find_element_by_xpath(self.NAME_TXT_XPATH).send_keys(Cat)

    def Add_image(self,image):
        self.driver.find_element_by_name(self.FILE_BTN_NAME).send_keys(image)

    def Save(self):
        self.driver.find_element_by_xpath(self.SAVE_BUTTON_XPATH).click()

    def Check_Categry_name(self,CatName):
        sleep(3)
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        Page_count=len(self.driver.find_elements_by_xpath(self.PAGES))-2

        x=0
        for j in range(Page_count):
            Names=self.driver.find_elements_by_xpath(self.NAME_LIST)
            for i in range(len(Names)):
                CategoryName=self.driver.find_element_by_xpath("//Table/tbody/tr["+str(i+1)+"]/td[2]").text
                if CategoryName==CatName:
                    x = 1
                    return x
            if x==1:
                break
            else:
                self.driver.find_element_by_xpath(self.NEXT_BTN_XPATH).click()



    def Delete_Categry(self,CatName):
            sleep(2)
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            Page_count=len(self.driver.find_elements_by_xpath(self.PAGES))-2

            x=0
            for j in range(Page_count):
                Names=self.driver.find_elements_by_xpath(self.NAME_LIST)
                for i in range(len(Names)):
                    CategoryName=self.driver.find_element_by_xpath("//Table//tr["+str(i+1)+"]/td[2]").text
                    if CategoryName==CatName:
                        x=1
                        self.driver.find_element_by_xpath("//Table/tbody/tr["+str(i+1)+"]/td[3]/div/div[2]").click()
                        element = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, self.DELETE_CONFIRM_BTN_XPATH)))
                        actions = ActionChains(self.driver)
                        actions.move_to_element(element).perform()
                        actions.click().perform()
                        break
                if x == 1:
                    break
                else:
                    self.driver.find_element_by_xpath(self.NEXT_BTN_XPATH).click()


    def Cancel_delete_Categry(self,CatName):
            sleep(2)
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            Page_count=len(self.driver.find_elements_by_xpath(self.PAGES))-2

            x=0
            for j in range(Page_count):
                Names=self.driver.find_elements_by_xpath(self.NAME_LIST)
                for i in range(len(Names)):
                    CategoryName=self.driver.find_element_by_xpath("//Table//tr["+str(i+1)+"]/td[2]").text
                    if CategoryName==CatName:
                        x=1
                        self.driver.find_element_by_xpath("//Table/tbody/tr["+str(i+1)+"]/td[3]/div/div[2]").click()
                        element = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, self.DELETE_REJECT_BTN_XPATH)))
                        actions = ActionChains(self.driver)
                        actions.move_to_element(element).perform()
                        actions.click().perform()
                        break
                if x == 1:
                    break
                else:
                    self.driver.find_element_by_xpath(self.NEXT_BTN_XPATH).click()


    def Click_Edit_category(self,CatName):
            sleep(2)
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            Page_count = len(self.driver.find_elements_by_xpath(self.PAGES)) - 2

            x = 0
            for j in range(Page_count):
                Names = self.driver.find_elements_by_xpath(self.NAME_LIST)
                for i in range(len(Names)):
                    CategoryName = self.driver.find_element_by_xpath("//Table//tr[" + str(i + 1) + "]/td[2]").text
                    if CategoryName == CatName:
                        x = 1
                        self.driver.find_element_by_xpath("//Table/tbody/tr[" + str(i + 1) + "]/td[3]/div/div[1]").click()
                        break
                if x == 1:
                    break
                else:
                    self.driver.find_element_by_xpath(self.NEXT_BTN_XPATH).click()


    def ChangeName(self,New_catName):
        self.driver.find_element_by_xpath(self.NAME_TXT_XPATH).click()
        sleep(1)
        self.driver.find_element_by_xpath(self.NAME_TXT_XPATH).send_keys(Keys.CONTROL + "a")
        self.driver.find_element_by_xpath(self.NAME_TXT_XPATH).send_keys(Keys.DELETE)
        sleep(1)
        self.driver.find_element_by_xpath(self.NAME_TXT_XPATH).send_keys(New_catName)

    def ChangeName_to_null(self,New_catName):
        self.driver.find_element_by_xpath(self.NAME_TXT_XPATH).click()
        sleep(1)
        self.driver.find_element_by_xpath(self.NAME_TXT_XPATH).send_keys(Keys.CONTROL + "a")
        self.driver.find_element_by_xpath(self.NAME_TXT_XPATH).send_keys(Keys.DELETE)

    def Change_image(self,image):
        self.driver.find_element_by_name(self.FILE_BTN_NAME).clear()
        self.driver.find_element_by_name(self.FILE_BTN_NAME).send_keys(image)



