#   pytest -v -s --html=Reports/test_Quiz_report.html --self-contained-html Testcases/test_Quiz.py --browser Firefox
#  pytest -v -s Admin/Testcases/test_Quiz.py --browser Firefox
#  pytest -v -s Admin/Testcases/test_Quiz.py --browser Chrome

import inspect
from Admin.Pageobjectives.Quiz import Quiz
from Admin.PreRequirements.PREREQUIRMENTS import PREREQUIRMENTS
import pytest
from Admin.Utilities.readproperties import ReadConfig
from time import sleep

BASEURL=ReadConfig.getBaseuRL()

class Test_Add_Quiz:

    @pytest.mark.sanity
    @pytest.mark.regression
    @pytest.mark.run(order=56)
    def test_Add_Quiz_success(self, setup):
        self.driver = setup
        self.driver.get(BASEURL)

        ##ClassObjects
        self.QU = Quiz(self.driver)

        ##PreRequirments
        PREREQUIRMENTS.Login_Success(self, setup)
        Speciality_Name = PREREQUIRMENTS.Add_Specialities_success(self, setup) ##Add Speciality
        Sub_Speciality_Name = PREREQUIRMENTS.Add_Sub_Specialities_success(self, setup, Speciality_Name) ##Add Zub Speciality
        Title="Quiz "+PREREQUIRMENTS.random_generator()
        URL="https://www.google.co.in/"

        # test start here
        ##PREREQUIRMENTS.Login_Success(self, setup)
        PREREQUIRMENTS.GetURL(self, setup)
        self.QU.Click_on_Topics()
        self.QU.Click_on_Add()
        self.QU.Click_on_speciality()
        sleep(3)
        self.QU.Select_speciality(Speciality_Name)
        self.QU.Click_on_Sub_speciality()
        sleep(3)
        self.QU.Select_Sub_speciality(Sub_Speciality_Name)
        self.QU.Add_Title(Title)
        self.QU.Add_URL(URL)
        self.QU.Select_status_Enable()
        self.QU.Click_Save()

        self.QU.Click_on_Topics()
        Found=self.QU.Check_Quiz_found(Title)
        if Found==1:
            assert True
            self.driver.close()
        else:
            # To take the Screenshote
            FunName = inspect.currentframe().f_code.co_name
            PREREQUIRMENTS.TAKE_SCREENSHOT(self, FunName)
            assert False

    @pytest.mark.regression
    @pytest.mark.run(order=57)
    def test_Add_Quiz_success_Disable_status(self, setup):
        self.driver = setup
        self.driver.get(BASEURL)

        ##ClassObjects
        self.QU = Quiz(self.driver)

        ##PreRequirments
        PREREQUIRMENTS.Login_Success(self, setup)
        Speciality_Name = PREREQUIRMENTS.Add_Specialities_success(self, setup)  ##Add Speciality
        Sub_Speciality_Name = PREREQUIRMENTS.Add_Sub_Specialities_success(self, setup,
                                                                          Speciality_Name)  ##Add Zub Speciality
        Title = "Quiz " + PREREQUIRMENTS.random_generator()
        URL = "https://www.google.co.in/"

        # test start here
        ##PREREQUIRMENTS.Login_Success(self, setup)
        PREREQUIRMENTS.GetURL(self, setup)
        self.QU.Click_on_Topics()
        self.QU.Click_on_Add()
        self.QU.Click_on_speciality()
        sleep(3)
        self.QU.Select_speciality(Speciality_Name)
        self.QU.Click_on_Sub_speciality()
        sleep(3)
        self.QU.Select_Sub_speciality(Sub_Speciality_Name)
        self.QU.Add_Title(Title)
        self.QU.Add_URL(URL)
        self.QU.Select_status_Disable()
        self.QU.Click_Save()

        self.QU.Click_on_Topics()
        Found = self.QU.Check_Quiz_found(Title)
        if Found == 1:
            assert True
            self.driver.close()
        else:
            # To take the Screenshote
            FunName = inspect.currentframe().f_code.co_name
            PREREQUIRMENTS.TAKE_SCREENSHOT(self, FunName)
            assert False

    @pytest.mark.regression
    @pytest.mark.run(order=58)
    def test_Add_Quiz_Fail_without_data(self, setup):
        self.driver = setup
        self.driver.get(BASEURL)

        ##ClassObjects
        self.QU = Quiz(self.driver)

        ##PreRequirments
        PREREQUIRMENTS.Login_Success(self, setup)

        # test start here
        ##PREREQUIRMENTS.Login_Success(self, setup)
        PREREQUIRMENTS.GetURL(self, setup)
        self.QU.Click_on_Topics()
        self.QU.Click_on_Add()
        sleep(1)
        self.QU.Click_Save()

        try:
            self.driver.find_element_by_xpath("//*[text()='Title is required']")
            self.driver.find_element_by_xpath("//*[text()='URL is required']")
            self.driver.find_element_by_xpath("//*[text()='Status is required']")

            assert True
            self.driver.close()
        except:
            # To take the Screenshote
            FunName = inspect.currentframe().f_code.co_name
            PREREQUIRMENTS.TAKE_SCREENSHOT(self, FunName)
            assert False

    @pytest.mark.regression
    @pytest.mark.run(order=59)
    def test_Add_Quiz_Fail_without_Specialisation_and_sub(self, setup):
        self.driver = setup
        self.driver.get(BASEURL)

        ##ClassObjects
        self.QU = Quiz(self.driver)

        ##PreRequirments
        PREREQUIRMENTS.Login_Success(self, setup)
        Title = "Quiz " + PREREQUIRMENTS.random_generator()
        URL = "https://www.google.co.in/"

        # test start here
        ##PREREQUIRMENTS.Login_Success(self, setup)
        PREREQUIRMENTS.GetURL(self, setup)
        self.QU.Click_on_Topics()
        self.QU.Click_on_Add()
        self.QU.Add_Title(Title)
        self.QU.Add_URL(URL)
        self.QU.Select_status_Enable()
        self.QU.Click_Save()

        self.driver.refresh()
        self.QU.Click_on_Topics()
        Found = self.QU.Check_Quiz_found(Title)
        if Found == 1:
            # To take the Screenshote
            FunName = inspect.currentframe().f_code.co_name
            PREREQUIRMENTS.TAKE_SCREENSHOT(self, FunName)
            assert False
        else:
            assert True
            self.driver.close()

class Test_Edit_Quiz:
    @pytest.mark.sanity
    @pytest.mark.regression
    @pytest.mark.run(order=60)
    def test_Edit_Quiz_success(self, setup):
        self.driver = setup
        self.driver.get(BASEURL)

        ##ClassObjects
        self.QU = Quiz(self.driver)

        ##PreRequirments
        PREREQUIRMENTS.Login_Success(self, setup)
        Title=PREREQUIRMENTS.Add_Quiz(self, setup)
        NewSpeciality_Name = PREREQUIRMENTS.Add_Specialities_success(self, setup)  ##Add Speciality
        NewSub_Speciality_Name = PREREQUIRMENTS.Add_Sub_Specialities_success(self, setup,NewSpeciality_Name)  ##Add Zub Speciality
        NewTitle = "Quiz " + PREREQUIRMENTS.random_generator()
        NewURL = "https://www.facebook.com/"

        # test start here
        ##PREREQUIRMENTS.Login_Success(self, setup)
        PREREQUIRMENTS.GetURL(self, setup)
        self.QU.Click_on_Topics()
        self.QU.Click_edit_Quiz(Title)
        self.QU.Click_on_speciality()
        sleep(3)
        self.QU.Select_speciality(NewSpeciality_Name)
        self.QU.Click_on_Sub_speciality()
        sleep(3)
        self.QU.Select_Sub_speciality(NewSub_Speciality_Name)
        self.QU.Add_Title(NewTitle)
        self.QU.Add_URL(NewURL)
        self.QU.Select_status_Enable()
        self.QU.Click_Save()

        self.QU.Click_on_Topics()
        sleep(5)
        Check = self.QU.Check_Quiz_found(NewTitle)
        if Check == 1:
            self.QU.Click_on_Topics()
            sleep(3)
            Check = self.QU.Check_Quiz_found(Title)
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

class Test_Delete_Quiz:
    @pytest.mark.sanity
    @pytest.mark.regression
    @pytest.mark.run(order=61)
    def test_Delete_Quiz_success(self, setup):
        self.driver = setup
        self.driver.get(BASEURL)

        ##ClassObjects
        self.QU = Quiz(self.driver)

        ##PreRequirments
        PREREQUIRMENTS.Login_Success(self, setup)
        Title=PREREQUIRMENTS.Add_Quiz(self, setup)

        # test start here
        ##PREREQUIRMENTS.Login_Success(self, setup)
        PREREQUIRMENTS.GetURL(self, setup)
        self.QU.Click_on_Topics()
        self.QU.Click_on_Delete_Quiz(Title)
        self.QU.Confirm_delete()

        self.QU.Click_on_Topics()
        sleep(3)
        Check = self.QU.Check_Quiz_found(Title)
        if Check == 1:
            # To take the Screenshote
            FunName = inspect.currentframe().f_code.co_name
            PREREQUIRMENTS.TAKE_SCREENSHOT(self, FunName)
            assert False
        else:
            assert True
            self.driver.close()


