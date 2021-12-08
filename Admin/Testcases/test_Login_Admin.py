#   pytest -v -s --html=Reports/test_Login_Admin_report.html --self-contained-html Testcases/test_Login_Admin.py --browser Firefox
#  pytest -v -s Admin/Testcases/test_Login_Admin.py --browser Firefox
#  pytest -v -s Admin/Testcases/test_Login_Admin.py --browser Chrome

from Admin.Pageobjectives.Login_Admin import LoginAdmin
from Admin.PreRequirements.PREREQUIRMENTS import PREREQUIRMENTS
import pytest
from Admin.Utilities.readproperties import ReadConfig
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import inspect
from time import sleep

BASEURL=ReadConfig.getBaseuRL()

class Test_Signin_Admin:

    @pytest.mark.sanity
    @pytest.mark.regression
    @pytest.mark.run(order=1)
    def test_Login_Success(self, setup):
        self.driver = setup
        self.driver.get(BASEURL)


        ##ClassObjects
        self.LA = LoginAdmin(self.driver)

        #test start here
        self.LA.Login_Success()
        ExpectedURL="https://clinictest.metrictreelabs.com/data"
        try:
            WebDriverWait(self.driver, 10).until(EC.url_to_be(ExpectedURL))  # Wait for the next page to load
            self.driver.close()
            assert True
        except:
            # To take the Screenshote
            FunName = inspect.currentframe().f_code.co_name
            PREREQUIRMENTS.TAKE_SCREENSHOT(self, FunName)
            assert False

    @pytest.mark.run(order=2)
    @pytest.mark.regression
    def test_Login_Fail(self, setup):
        self.driver = setup
        self.driver.get(BASEURL)


        ##ClassObjects
        self.LA = LoginAdmin(self.driver)

        #test start here
        self.LA.Login_Fail("xxx","yyyy")
        ExpectedURL="https://clinictest.metrictreelabs.com/data"
        try:
            WebDriverWait(self.driver, 1).until(EC.url_to_be(ExpectedURL))  # Wait for the next page to load
            # To take the Screenshote
            FunName = inspect.currentframe().f_code.co_name
            PREREQUIRMENTS.TAKE_SCREENSHOT(self, FunName)
            assert False

        except:
            self.driver.close()
            assert True

    @pytest.mark.run(order=3)
    @pytest.mark.regression
    def test_Login_with_NullValue(self, setup):
        self.driver = setup
        self.driver.get(BASEURL)


        ##ClassObjects
        self.LA = LoginAdmin(self.driver)

        #test start here
        self.LA.Login_Fail("","")
        ExpectedURL="https://clinictest.metrictreelabs.com/data"
        try:
            WebDriverWait(self.driver, 1).until(EC.url_to_be(ExpectedURL))  # Wait for the next page to load
            # To take the Screenshote
            FunName = inspect.currentframe().f_code.co_name
            PREREQUIRMENTS.TAKE_SCREENSHOT(self, FunName)
            assert False

        except:
            self.driver.close()
            assert True

    @pytest.mark.run(order=4)
    @pytest.mark.sanity
    @pytest.mark.regression
    def test_Logout(self, setup):
        self.driver = setup
        self.driver.get(BASEURL)

        ##ClassObjects
        self.LA = LoginAdmin(self.driver)

        # test start here
        self.LA.Login_Success()
        sleep(2)
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        self.LA.Logout()
        ExpectedURL = "https://clinictest.metrictreelabs.com/"
        try:
            WebDriverWait(self.driver, 1).until(EC.url_to_be(ExpectedURL))  # Wait for the next page to load
            self.driver.close()
            assert True

        except:
            # To take the Screenshote
            FunName = inspect.currentframe().f_code.co_name
            PREREQUIRMENTS.TAKE_SCREENSHOT(self, FunName)
            assert False


    @pytest.mark.skip
    @pytest.mark.run(order=5)
    @pytest.mark.regression
    def test_Forget_password(self, setup):
        pass









