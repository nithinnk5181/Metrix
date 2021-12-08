#   pytest -v -s --html=Reports/test_test_Specialities_report.html --self-contained-html Testcases/test_Specialities.py --browser Firefox
#  pytest -v -s Admin/Testcases/test_Specialities.py --browser Firefox
#  pytest -v -s Admin/Testcases/test_Specialities.py --browser Chrome


from Admin.Pageobjectives.Specialities import Specialities
from Admin.PreRequirements.PREREQUIRMENTS import PREREQUIRMENTS
import pytest
from Admin.Utilities.readproperties import ReadConfig
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
import inspect

BASEURL=ReadConfig.getBaseuRL()

class Test_Add_Specialities:


    @pytest.mark.run(order=15)
    @pytest.mark.sanity
    @pytest.mark.regression
    def test_Add_Specialities_success(self, setup):
        self.driver = setup
        self.driver.get(BASEURL)

        ##ClassObjects
        self.SP = Specialities(self.driver)

        # test start here
        PREREQUIRMENTS.Login_Success(self, setup)
        self.SP.Click_on_Specialities()
        self.SP.Click_on_Add()
        Speci_Name="SPEC" + PREREQUIRMENTS.random_generator()  # cReating Random Speciality name
        self.SP.Add_name(Speci_Name)

        self.SP.Click_Save()

        self.SP.Click_on_Specialities()
        Check = self.SP.Check_Speciality_name(Speci_Name)
        if Check == 1:
            assert True
            self.driver.close()
        else:
            # To take the Screenshote
            FunName =inspect.currentframe().f_code.co_name
            PREREQUIRMENTS.TAKE_SCREENSHOT(self, FunName)
            assert False


    @pytest.mark.run(order=16)
    @pytest.mark.regression
    def test_Add_Specialities_fail_without_name(self, setup):
        self.driver = setup
        self.driver.get(BASEURL)

        ##ClassObjects
        self.SP = Specialities(self.driver)

        # test start here
        PREREQUIRMENTS.Login_Success(self, setup)
        self.SP.Click_on_Specialities()
        self.SP.Click_on_Add()
        self.SP.Remove_name()
        self.SP.Click_Save()

        try:
            self.driver.find_element_by_xpath("//*[text()='Name cannot be empty']")
            assert True
            self.driver.close()
        except:
            # To take the Screenshote
            FunName = inspect.currentframe().f_code.co_name
            PREREQUIRMENTS.TAKE_SCREENSHOT(self, FunName)
            assert False


class Test_Edit_Specialities:


    @pytest.mark.run(order=17)
    @pytest.mark.regression
    @pytest.mark.sanity
    def test_Edit_Specialities_success(self, setup):
        self.driver = setup
        self.driver.get(BASEURL)

        ##ClassObjects
        self.SP = Specialities(self.driver)

        ##PreRequirments
        Speciality_Name = PREREQUIRMENTS.Add_Specialities_success(self, setup)

        # test start here
        ##PREREQUIRMENTS.Login_Success(self, setup)
        PREREQUIRMENTS.GetURL(self, setup)
        self.SP.Click_on_Specialities()
        self.SP.Click_Edit_spacialities(Speciality_Name)
        Speci_Name = "NEWSPEC" + PREREQUIRMENTS.random_generator()  # cReating Random Speciality name
        self.SP.Add_name(Speci_Name)
        self.SP.Click_Save()

        self.SP.Click_on_Specialities()
        Check_New = self.SP.Check_Speciality_name(Speci_Name)
        self.SP.Click_on_Specialities()
        Check = self.SP.Check_Speciality_name(Speciality_Name)

        if Check == 1:
            # To take the Screenshote
            FunName = inspect.currentframe().f_code.co_name
            PREREQUIRMENTS.TAKE_SCREENSHOT(self, FunName)
            assert False
        elif Check_New==0:
            # To take the Screenshote
            FunName = inspect.currentframe().f_code.co_name
            PREREQUIRMENTS.TAKE_SCREENSHOT(self, FunName)
            assert False
        else:
            assert True
            self.driver.close()

    @pytest.mark.run(order=18)
    @pytest.mark.regression
    def test_Edit_Specialities_negative_without_name(self, setup):
        self.driver = setup
        self.driver.get(BASEURL)

        ##ClassObjects
        self.SP = Specialities(self.driver)

        ##PreRequirments
        Speciality_Name = PREREQUIRMENTS.Add_Specialities_success(self, setup)

        # test start here
        ##PREREQUIRMENTS.Login_Success(self, setup)
        PREREQUIRMENTS.GetURL(self, setup)
        self.SP.Click_on_Specialities()
        self.SP.Click_Edit_spacialities(Speciality_Name)
        self.SP.Remove_name()
        self.SP.Click_Save()
        try:
            self.driver.find_element_by_xpath("//*[text()='Name cannot be empty']")
            assert True
            self.driver.close()
        except:
            # To take the Screenshote
            FunName = inspect.currentframe().f_code.co_name
            PREREQUIRMENTS.TAKE_SCREENSHOT(self, FunName)
            assert False

class Test_Delete_Specialities:

    @pytest.mark.run(order=19)
    @pytest.mark.regression
    @pytest.mark.sanity
    def test_Delete_Specialities_success(self, setup):
        self.driver = setup
        self.driver.get(BASEURL)

        ##ClassObjects
        self.SP = Specialities(self.driver)

        ##PreRequirments
        Speciality_Name = PREREQUIRMENTS.Add_Specialities_success(self, setup)

        # test start here
        ##PREREQUIRMENTS.Login_Success(self, setup)
        PREREQUIRMENTS.GetURL(self, setup)
        self.SP.Click_on_Specialities()
        self.SP.Click_Delete_spacialities(Speciality_Name)
        self.SP.Confirm_delete()

        self.SP.Click_on_Specialities()
        Check = self.SP.Check_Speciality_name(Speciality_Name)
        if Check == 1:
            # To take the Screenshote
            FunName = inspect.currentframe().f_code.co_name
            PREREQUIRMENTS.TAKE_SCREENSHOT(self, FunName)
            assert False
        else:
            assert True
            self.driver.close()

    @pytest.mark.run(order=20)
    @pytest.mark.regression
    def test_Delete_Specialities_fail(self, setup):
        self.driver = setup
        self.driver.get(BASEURL)

        ##ClassObjects
        self.SP = Specialities(self.driver)

        ##PreRequirments
        Speciality_Name = PREREQUIRMENTS.Add_Specialities_success(self, setup)

        # test start here
        ##PREREQUIRMENTS.Login_Success(self, setup)
        PREREQUIRMENTS.GetURL(self, setup)
        self.SP.Click_on_Specialities()
        self.SP.Click_Delete_spacialities(Speciality_Name)
        self.SP.Declain_delete()

        self.SP.Click_on_Specialities()
        Check = self.SP.Check_Speciality_name(Speciality_Name)
        if Check == 1:
            assert True
            self.driver.close()
        else:
            # To take the Screenshote
            FunName = inspect.currentframe().f_code.co_name
            PREREQUIRMENTS.TAKE_SCREENSHOT(self, FunName)
            assert False



class Test_Sub_Specialities:

    @pytest.mark.sanity
    @pytest.mark.regression
    @pytest.mark.run(order=21)
    def test_Add_Sub_Specialities_success(self, setup):
        self.driver = setup
        self.driver.get(BASEURL)

        ##ClassObjects
        self.SP = Specialities(self.driver)

        ##PreRequirments
        Speciality_Name = PREREQUIRMENTS.Add_Specialities_success(self, setup)

        # test start here
        ##PREREQUIRMENTS.Login_Success(self, setup)
        PREREQUIRMENTS.GetURL(self, setup)
        self.SP.Click_on_Specialities()
        self.SP.Click_Sub_spacialities(Speciality_Name)
        self.SP.Click_on_Add()
        Sub_spec_Name = "SUBSPEC" + PREREQUIRMENTS.random_generator()  # cReating Random Speciality name
        self.SP.Add_name(Sub_spec_Name)
        self.SP.Click_Save()

        Check = self.SP.Check_Speciality_name(Sub_spec_Name)
        if Check == 1:
            assert True
            self.driver.close()
        else:
            # To take the Screenshote
            FunName = inspect.currentframe().f_code.co_name
            PREREQUIRMENTS.TAKE_SCREENSHOT(self, FunName)
            assert False

    @pytest.mark.regression
    @pytest.mark.run(order=22)
    def test_Add_Sub_Specialities_fail_without_name(self, setup):
        self.driver = setup
        self.driver.get(BASEURL)

        ##ClassObjects
        self.SP = Specialities(self.driver)

        ##PreRequirments
        Speciality_Name = PREREQUIRMENTS.Add_Specialities_success(self, setup)

        # test start here
        ##PREREQUIRMENTS.Login_Success(self, setup)
        PREREQUIRMENTS.GetURL(self, setup)
        self.SP.Click_on_Specialities()
        self.SP.Click_Sub_spacialities(Speciality_Name)
        self.SP.Click_on_Add()
        self.SP.Remove_name()
        self.SP.Click_Save()
        try:
            self.driver.find_element_by_xpath("//*[text()='Name cannot be empty']")
            assert True
            self.driver.close()
        except:
            # To take the Screenshote
            FunName = inspect.currentframe().f_code.co_name
            PREREQUIRMENTS.TAKE_SCREENSHOT(self, FunName)
            assert False


    @pytest.mark.regression
    @pytest.mark.run(order=23)
    def test_Sub_Specialities_Edit(self, setup):
        self.driver = setup
        self.driver.get(BASEURL)

        ##ClassObjects
        self.SP = Specialities(self.driver)

        ##PreRequirments
        Speciality_Name = PREREQUIRMENTS.Add_Specialities_success(self, setup)
        Sub_Speciality_Name = PREREQUIRMENTS.Add_Sub_Specialities_success(self, setup,Speciality_Name)

        # test start here
        ##PREREQUIRMENTS.Login_Success(self, setup)
        PREREQUIRMENTS.GetURL(self, setup)
        self.SP.Click_on_Specialities()
        self.SP.Click_Sub_spacialities(Speciality_Name)
        self.SP.Click_Edit_Sub_spacialities(Sub_Speciality_Name)

        New_SpeciSub_Name = "NEWSUBSPEC" + PREREQUIRMENTS.random_generator()  # cReating Random Speciality name
        self.SP.Add_name(New_SpeciSub_Name)
        self.SP.Click_Save()

        Check = self.SP.Check_Speciality_name(New_SpeciSub_Name)
        if Check == 1:
            assert True
            self.driver.close()
        else:
            # To take the Screenshote
            FunName = inspect.currentframe().f_code.co_name
            PREREQUIRMENTS.TAKE_SCREENSHOT(self, FunName)
            assert False

    @pytest.mark.regression
    @pytest.mark.run(order=24)
    def test_Sub_Specialities_Edit_fail(self, setup):
        self.driver = setup
        self.driver.get(BASEURL)

        ##ClassObjects
        self.SP = Specialities(self.driver)

        ##PreRequirments
        Speciality_Name = PREREQUIRMENTS.Add_Specialities_success(self, setup)
        Sub_Speciality_Name = PREREQUIRMENTS.Add_Sub_Specialities_success(self, setup, Speciality_Name)

        # test start here
        ##PREREQUIRMENTS.Login_Success(self, setup)
        PREREQUIRMENTS.GetURL(self, setup)
        self.SP.Click_on_Specialities()
        self.SP.Click_Sub_spacialities(Speciality_Name)
        self.SP.Click_Edit_Sub_spacialities(Sub_Speciality_Name)
        self.SP.Remove_name()
        self.SP.Click_Save()

        try:
            self.driver.find_element_by_xpath("//*[text()='Name cannot be empty']")
            assert True
            self.driver.close()
        except:
            # To take the Screenshote
            FunName = inspect.currentframe().f_code.co_name
            PREREQUIRMENTS.TAKE_SCREENSHOT(self, FunName)
            assert False

    @pytest.mark.regression
    @pytest.mark.run(order=25)
    def test_Sub_Specialities_Delete(self, setup):
        self.driver = setup
        self.driver.get(BASEURL)

        ##ClassObjects
        self.SP = Specialities(self.driver)

        ##PreRequirments
        Speciality_Name = PREREQUIRMENTS.Add_Specialities_success(self, setup)
        Sub_Speciality_Name = PREREQUIRMENTS.Add_Sub_Specialities_success(self, setup, Speciality_Name)

        # test start here
        ##PREREQUIRMENTS.Login_Success(self, setup)
        PREREQUIRMENTS.GetURL(self, setup)
        self.SP.Click_on_Specialities()
        self.SP.Click_Sub_spacialities(Speciality_Name)
        self.SP.Click_Delete_Sub_spacialities(Sub_Speciality_Name)
        self.SP.Confirm_delete()

        Check = self.SP.Check_Speciality_name(Sub_Speciality_Name)
        if Check == 1:
            # To take the Screenshote
            FunName = inspect.currentframe().f_code.co_name
            PREREQUIRMENTS.TAKE_SCREENSHOT(self, FunName)
            assert False
        else:
            assert True
            self.driver.close()

    @pytest.mark.regression
    @pytest.mark.run(order=26)
    def test_Sub_Specialities_Delete_fail(self, setup):
        self.driver = setup
        self.driver.get(BASEURL)

        ##ClassObjects
        self.SP = Specialities(self.driver)

        ##PreRequirments
        Speciality_Name = PREREQUIRMENTS.Add_Specialities_success(self, setup)
        Sub_Speciality_Name = PREREQUIRMENTS.Add_Sub_Specialities_success(self, setup, Speciality_Name)

        # test start here
        ##PREREQUIRMENTS.Login_Success(self, setup)
        PREREQUIRMENTS.GetURL(self, setup)
        self.SP.Click_on_Specialities()
        self.SP.Click_Sub_spacialities(Speciality_Name)
        self.SP.Click_Delete_Sub_spacialities(Sub_Speciality_Name)
        self.SP.Declain_delete()

        Check = self.SP.Check_Speciality_name(Sub_Speciality_Name)
        if Check == 1:
            assert True
            self.driver.close()
        else:
            # To take the Screenshote
            FunName = inspect.currentframe().f_code.co_name
            PREREQUIRMENTS.TAKE_SCREENSHOT(self, FunName)
            assert False

