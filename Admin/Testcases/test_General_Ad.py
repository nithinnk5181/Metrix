#   pytest -v -s --html=Reports/test_General_Ad_report.html --self-contained-html Testcases/test_General_Ad.py --browser Firefox
#  pytest -v -s Admin/Testcases/test_General_Ad.py --browser Firefox
#  pytest -v -s Admin/Testcases/test_General_Ad.py --browser Chrome

import inspect
from Admin.Pageobjectives.General_Ad import General_Ad
from Admin.PreRequirements.PREREQUIRMENTS import PREREQUIRMENTS
import pytest
import datetime
from Admin.Utilities.readproperties import ReadConfig
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from selenium.common.exceptions import ElementClickInterceptedException

BASEURL=ReadConfig.getBaseuRL()

class Test_Add_General_Ad:

    @pytest.mark.sanity
    @pytest.mark.regression
    @pytest.mark.run(order=62)
    def test_Add_General_Ad_success(self, setup):
        self.driver = setup
        self.driver.get(BASEURL)

        ##ClassObjects
        self.GA = General_Ad(self.driver)

        ##PreRequirments
        PREREQUIRMENTS.Login_Success(self, setup)
        Title="AD_"+PREREQUIRMENTS.random_generator()
        URL="https://www.google.co.in/"

        # test start here
        ##PREREQUIRMENTS.Login_Success(self, setup)
        PREREQUIRMENTS.GetURL(self, setup)
        self.GA.Click_on_General_ad()
        self.GA.Click_on_Add()
        sleep(3)
        self.GA.Add_Title(Title)
        self.GA.Add_Url(URL)
        self.GA.Add_Image("C:/Users/NITHIN/PycharmProjects/ClinicTopics/Admin/ImageFiles/pexels-photo-7144362.jpeg")
        self.GA.Enable_status()
        self.GA.Click_save()

        self.GA.Click_on_General_ad()
        sleep(2)
        Found=self.GA.Check_Ad_found(Title)
        if Found==1:
            assert True
            self.driver.close()
        else:
            # To take the Screenshote
            FunName = inspect.currentframe().f_code.co_name
            PREREQUIRMENTS.TAKE_SCREENSHOT(self, FunName)
            assert False

    @pytest.mark.regression
    @pytest.mark.run(order=63)
    def test_Add_General_Ad_Disable_status(self, setup):
        self.driver = setup
        self.driver.get(BASEURL)

        ##ClassObjects
        self.GA = General_Ad(self.driver)

        ##PreRequirments
        PREREQUIRMENTS.Login_Success(self, setup)
        Title = "AD_" + PREREQUIRMENTS.random_generator()
        URL = "https://www.google.co.in/"

        # test start here
        ##PREREQUIRMENTS.Login_Success(self, setup)
        PREREQUIRMENTS.GetURL(self, setup)
        self.GA.Click_on_General_ad()
        self.GA.Click_on_Add()
        sleep(3)
        self.GA.Add_Title(Title)
        self.GA.Add_Url(URL)
        self.GA.Add_Image("C:/Users/NITHIN/PycharmProjects/ClinicTopics/Admin/ImageFiles/pexels-photo-7144362.jpeg")
        self.GA.Disable_status()
        self.GA.Click_save()

        self.GA.Click_on_General_ad()
        sleep(2)
        Found = self.GA.Check_Ad_found(Title)
        if Found == 1:
            assert True
            self.driver.close()
        else:
            # To take the Screenshote
            FunName = inspect.currentframe().f_code.co_name
            PREREQUIRMENTS.TAKE_SCREENSHOT(self, FunName)
            assert False

    @pytest.mark.regression
    @pytest.mark.run(order=64)
    def test_Add_General_Ad_fail_without_data(self, setup):
        self.driver = setup
        self.driver.get(BASEURL)

        ##ClassObjects
        self.GA = General_Ad(self.driver)

        ##PreRequirments
        PREREQUIRMENTS.Login_Success(self, setup)
        Title="AD_"+PREREQUIRMENTS.random_generator()
        URL="https://www.google.co.in/"

        # test start here
        ##PREREQUIRMENTS.Login_Success(self, setup)
        PREREQUIRMENTS.GetURL(self, setup)
        self.GA.Click_on_General_ad()
        self.GA.Click_on_Add()
        sleep(3)
        self.GA.Enable_status()
        self.GA.Click_save()

        try:
            self.driver.find_element_by_xpath("//*[text()='Title is required']")
            self.driver.find_element_by_xpath("//*[text()='URL is required']")
            self.driver.find_element_by_xpath("//*[text()='Image is required']")

            assert True
            self.driver.close()
        except:
            # To take the Screenshote
            FunName = inspect.currentframe().f_code.co_name
            PREREQUIRMENTS.TAKE_SCREENSHOT(self, FunName)
            assert False


class Test_Edit_General_Ad:

    @pytest.mark.sanity
    @pytest.mark.regression
    @pytest.mark.run(order=65)
    def test_Edit_General_Ad_success(self, setup):
        self.driver = setup
        self.driver.get(BASEURL)

        ##ClassObjects
        self.GA = General_Ad(self.driver)

        ##PreRequirments
        PREREQUIRMENTS.Login_Success(self, setup)
        Title=PREREQUIRMENTS.Add_General_Ad(self, setup)
        New_Title="NEW_AD_"+PREREQUIRMENTS.random_generator()
        NewURL="https://www.facebook.com/"

        # test start here
        ##PREREQUIRMENTS.Login_Success(self, setup)
        PREREQUIRMENTS.GetURL(self, setup)
        self.GA.Click_on_General_ad()
        self.GA.Click_Edit_ad(Title)
        sleep(3)
        self.GA.Add_Title(New_Title)
        self.GA.Add_Url(NewURL)
        self.GA.Add_Image("C:/Users/NITHIN/PycharmProjects/ClinicTopics/Admin/ImageFiles/Signs-of-Diabetes.png")
        self.GA.Enable_status()
        self.GA.Click_save()

        sleep(5)
        self.GA.Click_on_General_ad()
        self.driver.refresh()
        Check = self.GA.Check_Ad_found(New_Title)
        if Check == 1:
            self.GA.Click_on_General_ad()
            sleep(3)
            Check = self.GA.Check_Ad_found(Title)
            if Check == 1:
                # To take the Screenshote
                FunName = inspect.currentframe().f_code.co_name
                PREREQUIRMENTS.TAKE_SCREENSHOT(self, FunName)
                assert False
            else:
                assert True
                self.driver.close()
        else:
            # To take the Screenshote
            FunName = inspect.currentframe().f_code.co_name
            PREREQUIRMENTS.TAKE_SCREENSHOT(self, FunName)
            assert False


class Test_Delete_General_Ad:
    @pytest.mark.sanity
    @pytest.mark.regression
    @pytest.mark.run(order=66)
    def test_Delete_General_Ad(self, setup):
        self.driver = setup
        self.driver.get(BASEURL)

        ##ClassObjects
        self.GA = General_Ad(self.driver)

        ##PreRequirments
        PREREQUIRMENTS.Login_Success(self, setup)
        Title=PREREQUIRMENTS.Add_General_Ad(self, setup)

        self.GA.Click_on_General_ad()
        self.GA.Click_Delete_ad(Title)
        self.GA.Confirm_delete()

        self.GA.Click_on_General_ad()
        sleep(3)
        Found = self.GA.Check_Ad_found(Title)
        if Found == 1:
            # To take the Screenshote
            FunName = inspect.currentframe().f_code.co_name
            PREREQUIRMENTS.TAKE_SCREENSHOT(self, FunName)
            assert False

        else:
            assert True
            self.driver.close()
