class Quiz:
    """PageObjectives"""
    USERS_MENUITEM_XPATH='//*[@id="root"]/section/aside/div/ul/li[2]/span/a'



    """Methods"""
    def __init__(self,driver):
        self.driver=driver

    def Click_on_Topics(self):
        self.driver.find_element_by_xpath(self.USERS_MENUITEM_XPATH).click()