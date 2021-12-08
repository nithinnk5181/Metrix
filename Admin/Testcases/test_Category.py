
#   pytest -v -s --html=Reports/test_Category_report.html --self-contained-html Testcases/test_Category.py --browser Firefox
#  pytest -v -s Admin/Testcases/test_Category.py --browser Firefox
#  pytest -v -s Admin/Testcases/test_Category.py --browser Chrome

from Admin.Pageobjectives.Category import Category
from Admin.PreRequirements.PREREQUIRMENTS import PREREQUIRMENTS
import pytest
import inspect
from Admin.Utilities.readproperties import ReadConfig
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

BASEURL=ReadConfig.getBaseuRL()

class Test_Add_Category:

    @pytest.mark.run(order=6)
    @pytest.mark.sanity
    @pytest.mark.regression
    def test_Add_Category_success(self, setup):
        self.driver = setup
        self.driver.get(BASEURL)

        ##ClassObjects
        self.CA = Category(self.driver)

        # test start here
        PREREQUIRMENTS.Login_Success(self, setup)
        self.CA.Click_on_Category()
        self.CA.Click_on_add()
        Category_name = "CAT" + PREREQUIRMENTS.random_generator()  # cReating Random Category name
        self.CA.Add_Name(Category_name)
        self.CA.Add_image("C:/Users/NITHIN/PycharmProjects/ClinicTopics/Admin/ImageFiles/pexels-photo-7144362.jpeg")
        self.CA.Save()
        self.CA.Click_on_Category()
        Check = self.CA.Check_Categry_name(Category_name)
        if Check == 1:
            assert True
            self.driver.close()
        else:
            # To take the Screenshote
            FunName = inspect.currentframe().f_code.co_name
            PREREQUIRMENTS.TAKE_SCREENSHOT(self, FunName)
            assert False

    @pytest.mark.run(order=7)
    @pytest.mark.regression
    def test_Add_Category_fail_without_Name(self, setup):
        self.driver = setup
        self.driver.get(BASEURL)

        ##ClassObjects
        self.CA = Category(self.driver)

        # test start here
        PREREQUIRMENTS.Login_Success(self, setup)
        self.CA.Click_on_Category()
        self.CA.Click_on_add()
        self.CA.Add_image("C:/Users/NITHIN/PycharmProjects/ClinicTopics/Admin/ImageFiles/pexels-photo-7144362.jpeg")
        self.CA.Save()

        try:
            self.driver.find_element_by_xpath("//*[text()='Title is required']")
            assert True
            self.driver.close()
        except:
            # To take the Screenshote
            FunName = inspect.currentframe().f_code.co_name
            PREREQUIRMENTS.TAKE_SCREENSHOT(self, FunName)
            assert False

    @pytest.mark.run(order=8)
    @pytest.mark.regression
    def test_Add_Category_fail_without_Image(self, setup):
        self.driver = setup
        self.driver.get(BASEURL)

        ##ClassObjects
        self.CA = Category(self.driver)

        # test start here
        PREREQUIRMENTS.Login_Success(self, setup)
        self.CA.Click_on_Category()
        self.CA.Click_on_add()
        Category_name = "CAT" + PREREQUIRMENTS.random_generator()  # cReating Random Category name
        self.CA.Add_Name(Category_name)
        self.CA.Save()

        try:
            self.driver.find_element_by_xpath("//*[text()='Image is required']")
            assert True
            self.driver.close()
        except:
            # To take the Screenshote
            FunName = inspect.currentframe().f_code.co_name
            PREREQUIRMENTS.TAKE_SCREENSHOT(self, FunName)
            assert False


class Test_Delete_Category:

    @pytest.mark.run(order=9)
    @pytest.mark.sanity
    @pytest.mark.regression
    def test_Delete_Category_success(self, setup):
        self.driver = setup
        self.driver.get(BASEURL)

        ##ClassObjects
        self.CA = Category(self.driver)

        ##PreRequirments
        Category_Name=PREREQUIRMENTS.Add_Category_success(self,setup)


        # test start here
        ##PREREQUIRMENTS.Login_Success(self, setup)
        PREREQUIRMENTS.GetURL(self, setup)

        self.CA.Click_on_Category()
        self.CA.Delete_Categry(Category_Name)
        self.CA.Click_on_Category()
        Present=self.CA.Check_Categry_name(Category_Name)
        if Present==1:
            # To take the Screenshote
            FunName = inspect.currentframe().f_code.co_name
            PREREQUIRMENTS.TAKE_SCREENSHOT(self, FunName)
            assert False
        else:
            assert True
            self.driver.close()


    @pytest.mark.run(order=10)
    @pytest.mark.regression
    def test_Delete_Category_fail_without_confirmation(self, setup):
        self.driver = setup
        self.driver.get(BASEURL)

        ##ClassObjects
        self.CA = Category(self.driver)

        ##PreRequirments
        Category_Name = PREREQUIRMENTS.Add_Category_success(self, setup)

        # test start here
        ##PREREQUIRMENTS.Login_Success(self, setup)
        PREREQUIRMENTS.GetURL(self, setup)

        self.CA.Click_on_Category()
        self.CA.Cancel_delete_Categry(Category_Name)
        self.CA.Click_on_Category()
        Present = self.CA.Check_Categry_name(Category_Name)
        if Present == 1:
            assert True
            self.driver.close()
        else:
            # To take the Screenshote
            FunName = inspect.currentframe().f_code.co_name
            PREREQUIRMENTS.TAKE_SCREENSHOT(self, FunName)
            assert False

class Test_edit_Category:


    @pytest.mark.run(order=11)
    @pytest.mark.sanity
    @pytest.mark.regression
    def test_Edit_Category_Name(self, setup):
        self.driver = setup
        self.driver.get(BASEURL)

        ##ClassObjects
        self.CA = Category(self.driver)

        ##PreRequirments
        Category_Name=PREREQUIRMENTS.Add_Category_success(self,setup)


        # test start here
        ##PREREQUIRMENTS.Login_Success(self, setup)
        PREREQUIRMENTS.GetURL(self, setup)

        New_name="NEWCAT" + PREREQUIRMENTS.random_generator()#Create new Category name

        self.CA.Click_on_Category()
        self.CA.Click_Edit_category(Category_Name)
        self.CA.ChangeName(New_name)
        self.CA.Save()

        self.CA.Click_on_Category()
        Present=self.CA.Check_Categry_name(Category_Name)
        self.CA.Click_on_Category()
        Present_new=self.CA.Check_Categry_name(New_name)

        if Present==1:
            # To take the Screenshote
            FunName = inspect.currentframe().f_code.co_name
            PREREQUIRMENTS.TAKE_SCREENSHOT(self, FunName)
            assert False
        elif Present_new==0:
            # To take the Screenshote
            FunName = inspect.currentframe().f_code.co_name
            PREREQUIRMENTS.TAKE_SCREENSHOT(self, FunName)
            assert False
        else:
            assert True
            self.driver.close()

    @pytest.mark.run(order=12)
    @pytest.mark.regression
    def test_Edit_Category_Name_fail(self, setup):
        self.driver = setup
        self.driver.get(BASEURL)

        ##ClassObjects
        self.CA = Category(self.driver)

        ##PreRequirments
        Category_Name = PREREQUIRMENTS.Add_Category_success(self, setup)

        # test start here
        ##PREREQUIRMENTS.Login_Success(self, setup)
        PREREQUIRMENTS.GetURL(self, setup)

        New_name = "NEWCAT" + PREREQUIRMENTS.random_generator()  # Create new Category name

        self.CA.Click_on_Category()
        self.CA.Click_Edit_category(Category_Name)
        self.CA.ChangeName_to_null(New_name)
        self.CA.Save()
        try:
            self.CA.Click_on_Category()
            Present = self.CA.Check_Categry_name(Category_Name)

            # To take the Screenshote
            FunName = inspect.currentframe().f_code.co_name
            PREREQUIRMENTS.TAKE_SCREENSHOT(self, FunName)
            assert False
        except:

            try:
                self.driver.find_element_by_xpath("//*[text()='Title is required']")
                assert True
                self.driver.close()
            except:
                # To take the Screenshote
                FunName = inspect.currentframe().f_code.co_name
                PREREQUIRMENTS.TAKE_SCREENSHOT(self, FunName)
                assert False


    @pytest.mark.run(order=13)
    @pytest.mark.regression
    def test_Edit_Category_Image(self, setup):
        self.driver = setup
        self.driver.get(BASEURL)

        ##ClassObjects
        self.CA = Category(self.driver)

        ##PreRequirments
        Category_Name = PREREQUIRMENTS.Add_Category_success(self, setup)

        # test start here
        ##PREREQUIRMENTS.Login_Success(self, setup)
        PREREQUIRMENTS.GetURL(self, setup)

        New_name = "NEWCAT" + PREREQUIRMENTS.random_generator()  # Create new Category name

        self.CA.Click_on_Category()
        self.CA.Click_Edit_category(Category_Name)
        self.CA.Change_image("C:/Users/NITHIN/PycharmProjects/ClinicTopics/Admin/ImageFiles/Signs-of-Diabetes.png")
        self.CA.Save()
        try:
            self.driver.find_element_by_xpath("//*[text()='Image is required']")
            # To take the Screenshote
            FunName = inspect.currentframe().f_code.co_name
            PREREQUIRMENTS.TAKE_SCREENSHOT(self, FunName)
            assert False
        except:
            assert True
            self.driver.close()


    @pytest.mark.run(order=14)
    @pytest.mark.regression
    def test_Edit_both_Category_Name_AND_Image(self, setup):
        self.driver = setup
        self.driver.get(BASEURL)

        ##ClassObjects
        self.CA = Category(self.driver)

        ##PreRequirments
        Category_Name = PREREQUIRMENTS.Add_Category_success(self, setup)

        # test start here
        ##PREREQUIRMENTS.Login_Success(self, setup)
        PREREQUIRMENTS.GetURL(self, setup)

        New_name = "NEWCAT" + PREREQUIRMENTS.random_generator()  # Create new Category name

        self.CA.Click_on_Category()
        self.CA.Click_Edit_category(Category_Name)
        self.CA.ChangeName(New_name)
        self.CA.Change_image("C:/Users/NITHIN/PycharmProjects/ClinicTopics/Admin/ImageFiles/Signs-of-Diabetes.png")
        self.CA.Save()
        self.CA.Click_on_Category()
        Present = self.CA.Check_Categry_name(Category_Name)
        self.CA.Click_on_Category()
        Present_new = self.CA.Check_Categry_name(New_name)

        if Present == 1:
            # To take the Screenshote
            FunName = inspect.currentframe().f_code.co_name
            PREREQUIRMENTS.TAKE_SCREENSHOT(self, FunName)
            assert False
        elif Present_new == 0:
            # To take the Screenshote
            FunName = inspect.currentframe().f_code.co_name
            PREREQUIRMENTS.TAKE_SCREENSHOT(self, FunName)
            assert False
        else:
            assert True
            self.driver.close()

