
from time import sleep
from selenium.webdriver.common.keys import Keys
import datetime



class Topics:
    """PageObjectives"""
    TOPIC_MENUITEM_XPATH='//*[@id="root"]/section/aside/div/ul/li[5]/span/a'
    ADD_BTN_XPATH='//*[@id="root"]/section/section/main/div/div/div[1]/div/div[2]/button/span[1]/span'
    SPECIALIZATION_XPATH="//div[@class='ant-select-selection-overflow']"
    SPECIALIZATION_TXT_XPATH="//div/input[@class='ant-select-selection-search-input']"
    SPECIALIZATION_NAMES_XPATH="//div[@class='ant-select-tree-list-holder']//div[@class='ant-select-tree-list-holder-inner']//span[4]"
    SPECIALIZATION_SELECT_XPATH="//div[@class='ant-select-tree-list-holder']//div[@class='ant-select-tree-treenode ant-select-tree-treenode-switcher-close']/span[3]/span"
    SPECIALIZATION_DROPDOWN_BTN_XPATH="//div[@class='ant-select-tree-list-holder']//div[@class='ant-select-tree-treenode ant-select-tree-treenode-switcher-close']/span[2]/span"
    CATEGORY_DROPDOWN_XPATH='//*[@id="basic"]/div/div[2]/div[2]/div/div/div[1]/div/div[1]/div[1]'
    CATEGORY_LIST_XPATH="//div[@class=' css-26l3qy-menu']/div/div"
    OUT_OF_LABELS_XPATH='//*[@id="basic"]/div/div[2]/div[1]'

    FORMAT1_RADIO_BTN_XPATH="//input[@class='ant-radio-input'][@value='1']"
    FORMAT2_RADIO_BTN_XPATH="//input[@class='ant-radio-input'][@value='2']"
    FORMAT3_RADIO_BTN_XPATH="//input[@class='ant-radio-input'][@value='3']"

    TITLE_TXT_XPATH='//*[@id="basic"]/div/div[4]/div[2]/div/div/div[1]/input'
    DESCRIPTION_TXT_XPATH="//textarea[@class='ant-input']"

    F1_DOC1_UPLOAD_XPATH="//input[@name='pdf']"
    F1_DOC2_UPLOAD_XPATH="//input[@name='pdfsecond']"

    F2_IMAGE_UPLOAD_XPATH="//input[@name='multi_image']"
    F2_PDF_SELECT="//input[@class='ant-radio-input'][@value='pdf']"
    F2_EXTERNALURL_SELECT="//input[@class='ant-radio-input'][@value='external']"
    F2_PDF_UPLOAD_XPATH="//input[@class='ant-input'][@type='file'][@accept='image/pdf']"
    F2_EXTERNALURL_TXT_XPATH='//*[@id="basic"]/div/div[8]/div[2]/div/div/div[1]/input'

    F3_VIDEOURL_TXT_XPATH='//*[@id="basic"]/div/div[6]/div[2]/div/div/div[1]/input'

    PUBLISH_NOW_RADIO_XPATH="//input[@class='ant-radio-input'][@value='now']"
    PUBLISH_LATTER_RADIO_BUTTON="//input[@class='ant-radio-input'][@value='later']"
    SAVE_BTN_XPATH="//button[@class='ant-btn ant-btn-primary'][@type='submit']"

    NAME_LIST = '//Table/tbody/tr/td[2]'
    PAGES = "//ul[@class='ant-pagination ant-table-pagination ant-table-pagination-right']/li"
    NEXT_BTN_XPATH = "//ul[@class='ant-pagination ant-table-pagination ant-table-pagination-right']/li[last()]"

    PUBLISH_LATTER_DATE_TXT_XPATH='//*[@id="basic"]/div/div[9]/div/div/div/div/div/div/div/input'
    NOW_LINKTEXT_XPATH="//li[@class='ant-picker-now']/a"
    DATES_XPATH="//table[@class='ant-picker-content']//tr/td/div"
    OK_BUTTON_XPATH="//li[@class='ant-picker-ok']/button"
    NEXT_MONTH_BTN_XPATH="//div[@class='ant-picker-header']/button[@class='ant-picker-header-next-btn']"
    PREVIOUSE_MONTH_BTN_XPATH="//div[@class='ant-picker-header']/button[@class='ant-picker-header-prev-btn']"

    SPECIALITIES='/html/body/div[4]/div/div/div/div/div/div[3]/div[1]/div'

    DELETE_CONFIRM_BUTTON_XPATH="//div[@class='ant-popover-buttons']/button[2]"



    """Methods"""

    def __init__(self,driver):
        self.driver=driver

    def Click_on_Topics(self):
        self.driver.find_element_by_xpath(self.TOPIC_MENUITEM_XPATH).click()

    def Click_on_Add(self):
        self.driver.find_element_by_xpath(self.ADD_BTN_XPATH).click()

    def Click_on_specialization(self,spec):
        sleep(1)
        self.driver.find_element_by_xpath(self.SPECIALIZATION_XPATH).click()
        sleep(2)
        self.driver.find_element_by_xpath(self.SPECIALIZATION_TXT_XPATH).send_keys(spec)

    def select_specialization(self,Spec):
        Names = self.driver.find_elements_by_xpath(self.SPECIALIZATION_NAMES_XPATH)
        for name in Names:
            if name.text==Spec:
                sleep(2)
                name.click()
                break

    def Remove_spec_list(self):
        self.driver.find_element_by_xpath(self.OUT_OF_LABELS_XPATH).click()

    def Click_on_Category(self):
        self.driver.find_element_by_xpath(self.CATEGORY_DROPDOWN_XPATH).click()

    def select_Category(self,category):
        Names = self.driver.find_elements_by_xpath(self.CATEGORY_LIST_XPATH)
        for name in Names:
            Category_name=name.text
            if Category_name==category:
                sleep(2)
                name.click()
                break

    def select_format1(self):
        self.driver.find_element_by_xpath(self.FORMAT1_RADIO_BTN_XPATH).click()

    def select_format2(self):
        self.driver.find_element_by_xpath(self.FORMAT2_RADIO_BTN_XPATH).click()

    def select_format3(self):
        self.driver.find_element_by_xpath(self.FORMAT3_RADIO_BTN_XPATH).click()

    def Add_Title(self,Title):
        self.driver.find_element_by_xpath(self.TITLE_TXT_XPATH).click()
        self.driver.find_element_by_xpath(self.TITLE_TXT_XPATH).send_keys(Keys.CONTROL + "a")
        self.driver.find_element_by_xpath(self.TITLE_TXT_XPATH).send_keys(Keys.DELETE)
        self.driver.find_element_by_xpath(self.TITLE_TXT_XPATH).send_keys(Title)

    def Add_Description(self,Des):
        self.driver.find_element_by_xpath(self.DESCRIPTION_TXT_XPATH).click()
        self.driver.find_element_by_xpath(self.DESCRIPTION_TXT_XPATH).clear()
        self.driver.find_element_by_xpath(self.DESCRIPTION_TXT_XPATH).send_keys(Des)

    def F1_Doc1_upload(self,Image):
        self.driver.find_element_by_xpath(self.F1_DOC1_UPLOAD_XPATH).send_keys(Image)

    def F1_Doc2_upload(self,Image):
        self.driver.find_element_by_xpath(self.F1_DOC2_UPLOAD_XPATH).send_keys(Image)

    def F2_img_upload(self,Image):
        self.driver.find_element_by_xpath(self.F2_IMAGE_UPLOAD_XPATH).send_keys(Image)

    def F2_select_pdf(self):
        self.driver.find_element_by_xpath(self.F2_PDF_SELECT).click()

    def F2_select_ExternalURL(self):
        self.driver.find_element_by_xpath(self.F2_EXTERNALURL_SELECT).click()

    def F2_pdf_upload(self,Image):
        self.driver.find_element_by_xpath(self.F2_PDF_UPLOAD_XPATH).send_keys(Image)

    def F2_ExternalURL_add(self,URL):
        self.driver.find_element_by_xpath(self.F2_EXTERNALURL_TXT_XPATH).click()
        self.driver.find_element_by_xpath(self.F2_EXTERNALURL_TXT_XPATH).clear()
        self.driver.find_element_by_xpath(self.F2_EXTERNALURL_TXT_XPATH).send_keys(URL)

    def F3_VideoURL_add(self,URL):
        self.driver.find_element_by_xpath(self.F3_VIDEOURL_TXT_XPATH).click()
        self.driver.find_element_by_xpath(self.F3_VIDEOURL_TXT_XPATH).send_keys(URL)


    def Click_Publish_now(self):
        self.driver.find_element_by_xpath(self.PUBLISH_NOW_RADIO_XPATH).click()

    def Click_Publish_Latter(self):
        self.driver.find_element_by_xpath(self.PUBLISH_LATTER_RADIO_BUTTON).click()

    def Select_datepicker(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        current_day = datetime.datetime.now().day
        self.driver.find_element_by_xpath(self.PUBLISH_LATTER_DATE_TXT_XPATH).send_keys(current_day)

    def Click_Now(self):
        self.driver.find_element_by_xpath(self.NOW_LINKTEXT_XPATH).click()

    def Click_ok(self):
        self.driver.find_element_by_xpath(self.OK_BUTTON_XPATH).click()

    def Select_next_month(self):
        sleep(1)
        self.driver.find_element_by_xpath(self.NEXT_MONTH_BTN_XPATH).click()

    def Select_prev_month(self):
        sleep(1)
        self.driver.find_element_by_xpath(self.PREVIOUSE_MONTH_BTN_XPATH).click()

    def Select_Year(self,YEAR):
        Year = datetime.datetime.now().year

    def Select_Month(self,MONTH):
        Month = datetime.datetime.now().month

    def Select_Day(self,DAY):
        Dates=self.driver.find_elements_by_xpath(self.DATES_XPATH)
        for date in Dates:
            if date.text==DAY:
                date.click()
                break

    def Click_Save(self):
        self.driver.find_element_by_xpath(self.SAVE_BTN_XPATH).click()

    def Check_Topic_found(self,Title):
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

    def Click_on_Edit_topic(self,Topic):
        sleep(2)
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        Page_count = len(self.driver.find_elements_by_xpath(self.PAGES)) - 2

        x = 0
        for j in range(Page_count):
            Names = self.driver.find_elements_by_xpath(self.NAME_LIST)
            for i in range(len(Names)):
                Tit = self.driver.find_element_by_xpath("//Table/tbody/tr[" + str(i + 1) + "]/td[2]").text
                if Tit == Topic:
                    self.driver.find_element_by_xpath("//Table/tbody/tr[" + str(i + 1) + "]/td[4]/div/div[1]/button").click()
                    x=1
            if x == 1:
                break
            else:
                self.driver.find_element_by_xpath(self.NEXT_BTN_XPATH).click()

    def Click_on_Delete_topic(self,Topic):
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






