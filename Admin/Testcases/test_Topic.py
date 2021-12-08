#   pytest -v -s --html=Reports/test_test_Topic_report.html --self-contained-html Testcases/test_Topic.py --browser Firefox
#  pytest -v -s Admin/Testcases/test_Topic.py --browser Firefox
#  pytest -v -s Admin/Testcases/test_Topic.py --browser Chrome
import inspect

from Admin.Pageobjectives.Topic import Topics
from Admin.PreRequirements.PREREQUIRMENTS import PREREQUIRMENTS
import pytest
from Admin.Utilities.readproperties import ReadConfig
from time import sleep

BASEURL=ReadConfig.getBaseuRL()


class Test_Add_Topics_F1:

    @pytest.mark.sanity
    @pytest.mark.regression
    @pytest.mark.run(order=27)
    def test_Add_Topic_Format1_success(self, setup):
        self.driver = setup
        self.driver.get(BASEURL)

        ##ClassObjects
        self.TO = Topics(self.driver)

        ##PreRequirments
        PREREQUIRMENTS.Login_Success(self, setup)
        Speciality_Name = PREREQUIRMENTS.Add_Specialities_success(self, setup) ##Add Speciality
        Sub_Speciality_Name = PREREQUIRMENTS.Add_Sub_Specialities_success(self, setup, Speciality_Name) ##Add Zub Speciality
        Category_Name = PREREQUIRMENTS.Add_Category_success(self, setup) ##Add Category
        Title="F1 Title "+PREREQUIRMENTS.random_generator()

        # test start here
        ##PREREQUIRMENTS.Login_Success(self, setup)
        PREREQUIRMENTS.GetURL(self, setup)
        self.TO.Click_on_Topics()
        self.TO.Click_on_Add()
        self.TO.Click_on_specialization(Speciality_Name)
        sleep(3)
        self.TO.select_specialization(Speciality_Name)
        sleep(1)
        self.TO.Remove_spec_list()
        self.TO.Click_on_Category()
        self.TO.select_Category(Category_Name)
        self.TO.select_format1()
        self.TO.Add_Title(Title)
        self.TO.Add_Description("Testwejnfk weyfg bwu jwebfwbefiwehu iuwehfi wiuehdiuwehfi jweniqw")
        self.TO.F1_Doc1_upload("C:/Users/NITHIN/PycharmProjects/ClinicTopics/Admin/DocumentFiles/FRONT PAGE_ Corticosteroids in treatment of cough.pdf")
        self.TO.F1_Doc2_upload("C:/Users/NITHIN/PycharmProjects/ClinicTopics/Admin/DocumentFiles/SLIDE FLIP PAGE Corticosteroids in treatment of cough.pdf")
        self.TO.Click_Publish_now()
        self.TO.Click_Save()

        self.TO.Click_on_Topics()
        sleep(3)
        Check=self.TO.Check_Topic_found(Title)
        if Check == 1:
            assert True
            self.driver.close()
        else:
            # To take the Screenshote
            FunName = inspect.currentframe().f_code.co_name
            PREREQUIRMENTS.TAKE_SCREENSHOT(self, FunName)
            assert False

    @pytest.mark.sanity
    @pytest.mark.regression
    @pytest.mark.run(order=28)
    def test_Add_Topic_Format1_success_Publish_latter(self, setup):
        self.driver = setup
        self.driver.get(BASEURL)

        ##ClassObjects
        self.TO = Topics(self.driver)

        ##PreRequirments
        PREREQUIRMENTS.Login_Success(self, setup)
        Speciality_Name = PREREQUIRMENTS.Add_Specialities_success(self, setup)  ##Add Speciality
        Sub_Speciality_Name = PREREQUIRMENTS.Add_Sub_Specialities_success(self, setup,
                                                                          Speciality_Name)  ##Add Zub Speciality
        Category_Name = PREREQUIRMENTS.Add_Category_success(self, setup)  ##Add Category
        Title = "F1 Title " + PREREQUIRMENTS.random_generator()

        # test start here
        ##PREREQUIRMENTS.Login_Success(self, setup)
        PREREQUIRMENTS.GetURL(self, setup)
        self.TO.Click_on_Topics()
        self.TO.Click_on_Add()
        self.TO.Click_on_specialization(Speciality_Name)
        sleep(3)
        self.TO.select_specialization(Speciality_Name)
        sleep(1)
        self.TO.Remove_spec_list()
        self.TO.Click_on_Category()
        self.TO.select_Category(Category_Name)
        self.TO.select_format1()
        self.TO.Add_Title(Title)
        self.TO.Add_Description("Testwejnfk weyfg bwu jwebfwbefiwehu iuwehfi wiuehdiuwehfi jweniqw")
        self.TO.F1_Doc1_upload("C:/Users/NITHIN/PycharmProjects/ClinicTopics/Admin/DocumentFiles/FRONT PAGE_ Corticosteroids in treatment of cough.pdf")
        self.TO.F1_Doc2_upload("C:/Users/NITHIN/PycharmProjects/ClinicTopics/Admin/DocumentFiles/SLIDE FLIP PAGE Corticosteroids in treatment of cough.pdf")
        self.TO.Click_Publish_Latter()
        self.TO.Select_datepicker()
        try:
            self.TO.Click_Now()
        except:
            self.TO.Select_datepicker()
            self.TO.Click_Now()
        self.TO.Select_datepicker()
        self.TO.Select_next_month()
        self.TO.Select_Day("1")
        sleep(5)
        self.TO.Click_ok()
        self.TO.Click_Save()
        self.TO.Click_on_Topics()
        sleep(3)
        Check = self.TO.Check_Topic_found(Title)
        if Check == 1:
            assert True
            self.driver.close()
        else:
            # To take the Screenshote
            FunName = inspect.currentframe().f_code.co_name
            PREREQUIRMENTS.TAKE_SCREENSHOT(self, FunName)
            assert False

    @pytest.mark.regression
    @pytest.mark.run(order=29)
    def test_Add_Topic_Format1_fail_Without_specification(self, setup):
        self.driver = setup
        self.driver.get(BASEURL)

        ##ClassObjects
        self.TO = Topics(self.driver)

        ##PreRequirments
        PREREQUIRMENTS.Login_Success(self, setup)
        Category_Name = PREREQUIRMENTS.Add_Category_success(self, setup)  ##Add Category
        Title = "F1 Title " + PREREQUIRMENTS.random_generator()

        # test start here
        ##PREREQUIRMENTS.Login_Success(self, setup)
        PREREQUIRMENTS.GetURL(self, setup)
        self.TO.Click_on_Topics()
        self.TO.Click_on_Add()
        sleep(2)
        self.TO.Click_on_Category()
        self.TO.select_Category(Category_Name)
        self.TO.select_format1()
        self.TO.Add_Title(Title)
        self.TO.Add_Description("Testwejnfk weyfg bwu jwebfwbefiwehu iuwehfi wiuehdiuwehfi jweniqw")
        self.TO.F1_Doc1_upload("C:/Users/NITHIN/PycharmProjects/ClinicTopics/Admin/DocumentFiles/FRONT PAGE_ Corticosteroids in treatment of cough.pdf")
        self.TO.F1_Doc2_upload("C:/Users/NITHIN/PycharmProjects/ClinicTopics/Admin/DocumentFiles/SLIDE FLIP PAGE Corticosteroids in treatment of cough.pdf")
        self.TO.Click_Publish_now()
        self.TO.Click_Save()

        try:
            self.driver.find_element_by_xpath("//*[text()='Specialization cannot be empty']")
            self.driver.refresh()
            self.TO.Click_on_Topics()
            sleep(3)
            Check = self.TO.Check_Topic_found(Title)
            if Check == 1:
                # To take the Screenshote
                FunName = inspect.currentframe().f_code.co_name
                PREREQUIRMENTS.TAKE_SCREENSHOT(self, FunName)
                assert False
            else:
                assert True
                self.driver.close()

        except:
            # To take the Screenshote
            FunName = inspect.currentframe().f_code.co_name
            PREREQUIRMENTS.TAKE_SCREENSHOT(self, FunName)
            assert False

    @pytest.mark.regression
    @pytest.mark.run(order=30)
    def test_Add_Topic_Format1_fail_Without_Category(self, setup):
        self.driver = setup
        self.driver.get(BASEURL)

        ##ClassObjects
        self.TO = Topics(self.driver)

        ##PreRequirments
        PREREQUIRMENTS.Login_Success(self, setup)
        Speciality_Name = PREREQUIRMENTS.Add_Specialities_success(self, setup)  ##Add Speciality
        Sub_Speciality_Name = PREREQUIRMENTS.Add_Sub_Specialities_success(self, setup,Speciality_Name)  ##Add Zub Speciality
        Title = "F1 Title " + PREREQUIRMENTS.random_generator()

        # test start here
        ##PREREQUIRMENTS.Login_Success(self, setup)
        PREREQUIRMENTS.GetURL(self, setup)
        self.TO.Click_on_Topics()
        self.TO.Click_on_Add()
        self.TO.Click_on_specialization(Speciality_Name)
        sleep(3)
        self.TO.select_specialization(Speciality_Name)
        sleep(1)
        self.TO.Remove_spec_list()
        self.TO.select_format1()
        self.TO.Add_Title(Title)
        self.TO.Add_Description("Testwejnfk weyfg bwu jwebfwbefiwehu iuwehfi wiuehdiuwehfi jweniqw")
        self.TO.F1_Doc1_upload("C:/Users/NITHIN/PycharmProjects/ClinicTopics/Admin/DocumentFiles/FRONT PAGE_ Corticosteroids in treatment of cough.pdf")
        self.TO.F1_Doc2_upload("C:/Users/NITHIN/PycharmProjects/ClinicTopics/Admin/DocumentFiles/SLIDE FLIP PAGE Corticosteroids in treatment of cough.pdf")
        self.TO.Click_Publish_now()
        self.TO.Click_Save()

        try:
            self.driver.find_element_by_xpath("//*[text()='Category cannot be empty']")
            self.driver.refresh()
            self.TO.Click_on_Topics()
            sleep(3)
            Check = self.TO.Check_Topic_found(Title)
            if Check == 1:
                # To take the Screenshote
                FunName = inspect.currentframe().f_code.co_name
                PREREQUIRMENTS.TAKE_SCREENSHOT(self, FunName)
                assert False
            else:
                assert True
                self.driver.close()

        except:
            # To take the Screenshote
            FunName = inspect.currentframe().f_code.co_name
            PREREQUIRMENTS.TAKE_SCREENSHOT(self, FunName)
            assert False

    @pytest.mark.regression
    @pytest.mark.run(order=31)
    def test_Add_Topic_Format1_fail_Without_Title(self, setup):
        self.driver = setup
        self.driver.get(BASEURL)

        ##ClassObjects
        self.TO = Topics(self.driver)

        ##PreRequirments
        PREREQUIRMENTS.Login_Success(self, setup)
        Speciality_Name = PREREQUIRMENTS.Add_Specialities_success(self, setup)  ##Add Speciality
        Sub_Speciality_Name = PREREQUIRMENTS.Add_Sub_Specialities_success(self, setup,Speciality_Name)  ##Add Zub Speciality
        Category_Name = PREREQUIRMENTS.Add_Category_success(self, setup)  ##Add Category


        # test start here
        ##PREREQUIRMENTS.Login_Success(self, setup)
        PREREQUIRMENTS.GetURL(self, setup)
        self.TO.Click_on_Topics()
        self.TO.Click_on_Add()
        self.TO.Click_on_specialization(Speciality_Name)
        sleep(3)
        self.TO.select_specialization(Speciality_Name)
        sleep(1)
        self.TO.Remove_spec_list()
        self.TO.Click_on_Category()
        self.TO.select_Category(Category_Name)
        self.TO.select_format1()
        self.TO.Add_Description("Testwejnfk weyfg bwu jwebfwbefiwehu iuwehfi wiuehdiuwehfi jweniqw")
        self.TO.F1_Doc1_upload("C:/Users/NITHIN/PycharmProjects/ClinicTopics/Admin/DocumentFiles/FRONT PAGE_ Corticosteroids in treatment of cough.pdf")
        self.TO.F1_Doc2_upload("C:/Users/NITHIN/PycharmProjects/ClinicTopics/Admin/DocumentFiles/SLIDE FLIP PAGE Corticosteroids in treatment of cough.pdf")
        self.TO.Click_Publish_now()
        self.TO.Click_Save()

        try:
            self.driver.find_element_by_xpath("//*[text()=' Title cannot be empty']")
            assert True
            self.driver.close()

        except:
            # To take the Screenshote
            FunName = inspect.currentframe().f_code.co_name
            PREREQUIRMENTS.TAKE_SCREENSHOT(self, FunName)
            assert False

    @pytest.mark.regression
    @pytest.mark.run(order=32)
    def test_Add_Topic_Format1_fail_Without_Description(self, setup):
        self.driver = setup
        self.driver.get(BASEURL)

        ##ClassObjects
        self.TO = Topics(self.driver)

        ##PreRequirments
        PREREQUIRMENTS.Login_Success(self, setup)
        Speciality_Name = PREREQUIRMENTS.Add_Specialities_success(self, setup)  ##Add Speciality
        Sub_Speciality_Name = PREREQUIRMENTS.Add_Sub_Specialities_success(self, setup,Speciality_Name)  ##Add Zub Speciality
        Category_Name = PREREQUIRMENTS.Add_Category_success(self, setup)  ##Add Category
        Title = "F1 Title " + PREREQUIRMENTS.random_generator()


        # test start here
        ##PREREQUIRMENTS.Login_Success(self, setup)
        PREREQUIRMENTS.GetURL(self, setup)
        self.TO.Click_on_Topics()
        self.TO.Click_on_Add()
        self.TO.Click_on_specialization(Speciality_Name)
        sleep(3)
        self.TO.select_specialization(Speciality_Name)
        sleep(1)
        self.TO.Remove_spec_list()
        self.TO.Click_on_Category()
        self.TO.select_Category(Category_Name)
        self.TO.select_format1()
        self.TO.Add_Title(Title)
        self.TO.F1_Doc1_upload("C:/Users/NITHIN/PycharmProjects/ClinicTopics/Admin/DocumentFiles/FRONT PAGE_ Corticosteroids in treatment of cough.pdf")
        self.TO.F1_Doc2_upload("C:/Users/NITHIN/PycharmProjects/ClinicTopics/Admin/DocumentFiles/SLIDE FLIP PAGE Corticosteroids in treatment of cough.pdf")
        self.TO.Click_Publish_now()
        self.TO.Click_Save()

        try:
            self.driver.find_element_by_xpath("//*[text()='Description cannot be empty']")
            self.driver.refresh()
            self.TO.Click_on_Topics()
            sleep(3)
            Check = self.TO.Check_Topic_found(Title)
            if Check == 1:
                # To take the Screenshote
                FunName = inspect.currentframe().f_code.co_name
                PREREQUIRMENTS.TAKE_SCREENSHOT(self, FunName)
                assert False
            else:
                assert True
                self.driver.close()
        except:
            # To take the Screenshote
            FunName = inspect.currentframe().f_code.co_name
            PREREQUIRMENTS.TAKE_SCREENSHOT(self, FunName)
            assert False

    @pytest.mark.regression
    @pytest.mark.run(order=33)
    def test_Add_Topic_Format1_fail_Without_First_Document(self, setup):
        self.driver = setup
        self.driver.get(BASEURL)

        ##ClassObjects
        self.TO = Topics(self.driver)

        ##PreRequirments
        PREREQUIRMENTS.Login_Success(self, setup)
        Speciality_Name = PREREQUIRMENTS.Add_Specialities_success(self, setup)  ##Add Speciality
        Sub_Speciality_Name = PREREQUIRMENTS.Add_Sub_Specialities_success(self, setup,Speciality_Name)  ##Add Zub Speciality
        Category_Name = PREREQUIRMENTS.Add_Category_success(self, setup)  ##Add Category
        Title = "F1 Title " + PREREQUIRMENTS.random_generator()

        # test start here
        ##PREREQUIRMENTS.Login_Success(self, setup)
        PREREQUIRMENTS.GetURL(self, setup)
        self.TO.Click_on_Topics()
        self.TO.Click_on_Add()
        self.TO.Click_on_specialization(Speciality_Name)
        sleep(3)
        self.TO.select_specialization(Speciality_Name)
        sleep(1)
        self.TO.Remove_spec_list()
        self.TO.Click_on_Category()
        self.TO.select_Category(Category_Name)
        self.TO.select_format1()
        self.TO.Add_Title(Title)
        self.TO.Add_Description("Testwejnfk weyfg bwu jwebfwbefiwehu iuwehfi wiuehdiuwehfi jweniqw")
        self.TO.F1_Doc2_upload("C:/Users/NITHIN/PycharmProjects/ClinicTopics/Admin/DocumentFiles/SLIDE FLIP PAGE Corticosteroids in treatment of cough.pdf")
        self.TO.Click_Publish_now()
        self.TO.Click_Save()

        try:
            self.driver.find_element_by_xpath("//*[text()='Please upload Front Pdf']")
            self.driver.refresh()
            self.TO.Click_on_Topics()
            sleep(3)
            Check = self.TO.Check_Topic_found(Title)
            if Check == 1:
                # To take the Screenshote
                FunName = inspect.currentframe().f_code.co_name
                PREREQUIRMENTS.TAKE_SCREENSHOT(self, FunName)
                assert False
            else:
                assert True
                self.driver.close()
        except:
            # To take the Screenshote
            FunName = inspect.currentframe().f_code.co_name
            PREREQUIRMENTS.TAKE_SCREENSHOT(self, FunName)
            assert False

    @pytest.mark.regression
    @pytest.mark.run(order=34)
    def test_Add_Topic_Format1_fail_Without_Second_Document(self, setup):
        self.driver = setup
        self.driver.get(BASEURL)

        ##ClassObjects
        self.TO = Topics(self.driver)

        ##PreRequirments
        PREREQUIRMENTS.Login_Success(self, setup)
        Speciality_Name = PREREQUIRMENTS.Add_Specialities_success(self, setup)  ##Add Speciality
        Sub_Speciality_Name = PREREQUIRMENTS.Add_Sub_Specialities_success(self, setup,Speciality_Name)  ##Add Zub Speciality
        Category_Name = PREREQUIRMENTS.Add_Category_success(self, setup)  ##Add Category
        Title = "F1 Title " + PREREQUIRMENTS.random_generator()

        # test start here
        ##PREREQUIRMENTS.Login_Success(self, setup)
        PREREQUIRMENTS.GetURL(self, setup)
        self.TO.Click_on_Topics()
        self.TO.Click_on_Add()
        self.TO.Click_on_specialization(Speciality_Name)
        sleep(3)
        self.TO.select_specialization(Speciality_Name)
        sleep(1)
        self.TO.Remove_spec_list()
        self.TO.Click_on_Category()
        self.TO.select_Category(Category_Name)
        self.TO.select_format1()
        self.TO.Add_Title(Title)
        self.TO.Add_Description("Testwejnfk weyfg bwu jwebfwbefiwehu iuwehfi wiuehdiuwehfi jweniqw")
        self.TO.F1_Doc1_upload("C:/Users/NITHIN/PycharmProjects/ClinicTopics/Admin/DocumentFiles/FRONT PAGE_ Corticosteroids in treatment of cough.pdf")
        self.TO.Click_Publish_now()
        self.TO.Click_Save()

        try:
            self.driver.find_element_by_xpath("//*[text()='Please upload Back Pdf']")
            self.driver.refresh()
            self.TO.Click_on_Topics()
            sleep(3)
            Check = self.TO.Check_Topic_found(Title)
            if Check == 1:
                # To take the Screenshote
                FunName = inspect.currentframe().f_code.co_name
                PREREQUIRMENTS.TAKE_SCREENSHOT(self, FunName)
                assert False
            else:
                assert True
                self.driver.close()

        except:
            # To take the Screenshote
            FunName = inspect.currentframe().f_code.co_name
            PREREQUIRMENTS.TAKE_SCREENSHOT(self, FunName)
            assert False

    @pytest.mark.regression
    @pytest.mark.run(order=35)
    def test_Add_Topic_Format1_fail_Without_When_to_publish(self, setup):
        self.driver = setup
        self.driver.get(BASEURL)

        ##ClassObjects
        self.TO = Topics(self.driver)

        ##PreRequirments
        PREREQUIRMENTS.Login_Success(self, setup)
        Speciality_Name = PREREQUIRMENTS.Add_Specialities_success(self, setup)  ##Add Speciality
        Sub_Speciality_Name = PREREQUIRMENTS.Add_Sub_Specialities_success(self, setup,
                                                                          Speciality_Name)  ##Add Zub Speciality
        Category_Name = PREREQUIRMENTS.Add_Category_success(self, setup)  ##Add Category
        Title = "F1 Title " + PREREQUIRMENTS.random_generator()

        # test start here
        ##PREREQUIRMENTS.Login_Success(self, setup)
        PREREQUIRMENTS.GetURL(self, setup)
        self.TO.Click_on_Topics()
        self.TO.Click_on_Add()
        self.TO.Click_on_specialization(Speciality_Name)
        sleep(3)
        self.TO.select_specialization(Speciality_Name)
        sleep(1)
        self.TO.Remove_spec_list()
        self.TO.Click_on_Category()
        self.TO.select_Category(Category_Name)
        self.TO.select_format1()
        self.TO.Add_Title(Title)
        self.TO.Add_Description("Testwejnfk weyfg bwu jwebfwbefiwehu iuwehfi wiuehdiuwehfi jweniqw")
        self.TO.F1_Doc2_upload("C:/Users/NITHIN/PycharmProjects/ClinicTopics/Admin/DocumentFiles/SLIDE FLIP PAGE Corticosteroids in treatment of cough.pdf")
        self.TO.F1_Doc1_upload("C:/Users/NITHIN/PycharmProjects/ClinicTopics/Admin/DocumentFiles/FRONT PAGE_ Corticosteroids in treatment of cough.pdf")
        self.TO.Click_Save()

        try:
            self.driver.find_element_by_xpath("//*[text()='Publish time cannot be empty']")
            self.driver.refresh()
            self.TO.Click_on_Topics()
            sleep(3)
            Check = self.TO.Check_Topic_found(Title)
            if Check == 1:
                # To take the Screenshote
                FunName = inspect.currentframe().f_code.co_name
                PREREQUIRMENTS.TAKE_SCREENSHOT(self, FunName)
                assert False
            else:
                assert True
                self.driver.close()

        except:
            # To take the Screenshote
            FunName = inspect.currentframe().f_code.co_name
            PREREQUIRMENTS.TAKE_SCREENSHOT(self, FunName)
            assert False


class Test_Edit_Topics_F1:

    @pytest.mark.sanity
    @pytest.mark.regression
    @pytest.mark.run(order=36)
    def test_Edit_Topic_Format1_success(self, setup):
        self.driver = setup
        self.driver.get(BASEURL)

        ##ClassObjects
        self.TO = Topics(self.driver)

        ##PreRequirments
        PREREQUIRMENTS.Login_Success(self, setup)
        Title = PREREQUIRMENTS.Add_Topic_Format1_success(self, setup)
        NewTitle = "F1 New Title " + PREREQUIRMENTS.random_generator()
        NewSpecialisation_Name= PREREQUIRMENTS.Add_Specialities_success(self, setup)  ##Add Speciality
        NewSub_Speciality_Name = PREREQUIRMENTS.Add_Sub_Specialities_success(self, setup,NewSpecialisation_Name)  ##Add Zub Speciality
        NewCategory_Name = PREREQUIRMENTS.Add_Category_success(self, setup)  ##Add Category


        # test start here
        ##PREREQUIRMENTS.Login_Success(self, setup)
        PREREQUIRMENTS.GetURL(self, setup)
        self.TO.Click_on_Topics()
        self.TO.Click_on_Edit_topic(Title)

        self.TO.Click_on_specialization(NewSub_Speciality_Name)
        sleep(3)
        self.TO.select_specialization(NewSub_Speciality_Name)
        sleep(1)
        self.TO.Remove_spec_list()
        self.TO.Click_on_Category()
        self.TO.select_Category(NewCategory_Name)
        self.TO.Add_Title(NewTitle)
        self.TO.Add_Description("Test Test TEst TEst TEst Test tEtst TRatyys")
        self.TO.F1_Doc1_upload("C:/Users/NITHIN/PycharmProjects/ClinicTopics/Admin/DocumentFiles/SLIDE FLIP PAGE Corticosteroids in treatment of cough.pdf")
        self.TO.F1_Doc2_upload("C:/Users/NITHIN/PycharmProjects/ClinicTopics/Admin/DocumentFiles/FRONT PAGE_ Corticosteroids in treatment of cough.pdf")
        self.TO.Click_Save()

        self.TO.Click_on_Topics()
        sleep(5)
        Check = self.TO.Check_Topic_found(NewTitle)
        if Check == 1:
            self.TO.Click_on_Topics()
            sleep(3)
            Check = self.TO.Check_Topic_found(Title)
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


class Test_Add_Topics_F2:
    @pytest.mark.sanity
    @pytest.mark.regression
    @pytest.mark.run(order=37)
    def test_Add_Topic_Format2_PDF_success(self, setup):
        self.driver = setup
        self.driver.get(BASEURL)

        ##ClassObjects
        self.TO = Topics(self.driver)

        ##PreRequirments
        PREREQUIRMENTS.Login_Success(self, setup)
        Speciality_Name = PREREQUIRMENTS.Add_Specialities_success(self, setup)  ##Add Speciality
        Sub_Speciality_Name = PREREQUIRMENTS.Add_Sub_Specialities_success(self, setup,
                                                                          Speciality_Name)  ##Add Zub Speciality
        Category_Name = PREREQUIRMENTS.Add_Category_success(self, setup)  ##Add Category
        Title = "F2 Title " + PREREQUIRMENTS.random_generator()

        # test start here
        ##PREREQUIRMENTS.Login_Success(self, setup)
        PREREQUIRMENTS.GetURL(self, setup)
        self.TO.Click_on_Topics()
        self.TO.Click_on_Add()
        self.TO.Click_on_specialization(Speciality_Name)
        sleep(1)
        self.TO.select_specialization(Speciality_Name)
        self.TO.Remove_spec_list()
        self.TO.Click_on_Category()
        self.TO.select_Category(Category_Name)
        self.TO.select_format2()
        self.TO.Add_Title(Title)
        self.TO.Add_Description("Testwejnfk weyfg bwu jwebfwbefiwehu iuwehfi wiuehdiuwehfi jweniqw")
        self.TO.F2_img_upload("C:/Users/NITHIN/PycharmProjects/ClinicTopics/Admin/ImageFiles/pexels-photo-7144362.jpeg")
        self.TO.F2_select_pdf()
        self.TO.F2_pdf_upload("C:/Users/NITHIN/PycharmProjects/ClinicTopics/Admin/DocumentFiles/SLIDE FLIP PAGE Corticosteroids in treatment of cough.pdf")
        self.TO.Click_Publish_now()
        self.TO.Click_Save()

        self.TO.Click_on_Topics()
        sleep(3)
        Check = self.TO.Check_Topic_found(Title)
        if Check == 1:
            assert True
            self.driver.close()
        else:
            # To take the Screenshote
            FunName = inspect.currentframe().f_code.co_name
            PREREQUIRMENTS.TAKE_SCREENSHOT(self, FunName)
            assert False


    @pytest.mark.sanity
    @pytest.mark.regression
    @pytest.mark.run(order=38)
    def test_Add_Topic_Format2_ExternalURL_success(self, setup):
        self.driver = setup
        self.driver.get(BASEURL)

        ##ClassObjects
        self.TO = Topics(self.driver)

        ##PreRequirments
        PREREQUIRMENTS.Login_Success(self, setup)
        Speciality_Name = PREREQUIRMENTS.Add_Specialities_success(self, setup)  ##Add Speciality
        Sub_Speciality_Name = PREREQUIRMENTS.Add_Sub_Specialities_success(self, setup,
                                                                          Speciality_Name)  ##Add Zub Speciality
        Category_Name = PREREQUIRMENTS.Add_Category_success(self, setup)  ##Add Category
        Title = "F2 Title " + PREREQUIRMENTS.random_generator()

        # test start here
        ##PREREQUIRMENTS.Login_Success(self, setup)
        PREREQUIRMENTS.GetURL(self, setup)
        self.TO.Click_on_Topics()
        self.TO.Click_on_Add()
        self.TO.Click_on_specialization(Speciality_Name)
        sleep(1)
        self.TO.select_specialization(Speciality_Name)

        self.TO.Remove_spec_list()
        self.TO.Click_on_Category()
        self.TO.select_Category(Category_Name)
        self.TO.select_format2()
        self.TO.Add_Title(Title)
        self.TO.Add_Description("Testwejnfk weyfg bwu jwebfwbefiwehu iuwehfi wiuehdiuwehfi jweniqw")
        self.TO.F2_img_upload("C:/Users/NITHIN/PycharmProjects/ClinicTopics/Admin/ImageFiles/pexels-photo-7144362.jpeg")
        self.TO.F2_select_ExternalURL()
        self.TO.F2_ExternalURL_add("https://www.google.co.in/")

        self.TO.Click_Publish_now()
        self.TO.Click_Save()

        self.TO.Click_on_Topics()
        sleep(3)
        Check = self.TO.Check_Topic_found(Title)
        if Check == 1:
            assert True
            self.driver.close()
        else:
            # To take the Screenshote
            FunName = inspect.currentframe().f_code.co_name
            PREREQUIRMENTS.TAKE_SCREENSHOT(self, FunName)
            assert False

    @pytest.mark.regression
    @pytest.mark.run(order=39)
    def test_Add_Topic_Format2_PDF_without_title(self, setup):
        self.driver = setup
        self.driver.get(BASEURL)

        ##ClassObjects
        self.TO = Topics(self.driver)

        ##PreRequirments
        PREREQUIRMENTS.Login_Success(self, setup)
        Speciality_Name = PREREQUIRMENTS.Add_Specialities_success(self, setup)  ##Add Speciality
        Sub_Speciality_Name = PREREQUIRMENTS.Add_Sub_Specialities_success(self, setup,
                                                                          Speciality_Name)  ##Add Zub Speciality
        Category_Name = PREREQUIRMENTS.Add_Category_success(self, setup)  ##Add Category
        Title = "F2 Title " + PREREQUIRMENTS.random_generator()

        # test start here
        ##PREREQUIRMENTS.Login_Success(self, setup)
        PREREQUIRMENTS.GetURL(self, setup)
        self.TO.Click_on_Topics()
        self.TO.Click_on_Add()
        self.TO.Click_on_specialization(Speciality_Name)
        sleep(1)
        self.TO.select_specialization(Speciality_Name)

        self.TO.Remove_spec_list()
        self.TO.Click_on_Category()
        self.TO.select_Category(Category_Name)
        self.TO.select_format2()
        self.TO.Add_Description("Testwejnfk weyfg bwu jwebfwbefiwehu iuwehfi wiuehdiuwehfi jweniqw")
        self.TO.F2_img_upload("C:/Users/NITHIN/PycharmProjects/ClinicTopics/Admin/ImageFiles/pexels-photo-7144362.jpeg")
        self.TO.F2_select_pdf()
        self.TO.F2_pdf_upload(
            "C:/Users/NITHIN/PycharmProjects/ClinicTopics/Admin/DocumentFiles/SLIDE FLIP PAGE Corticosteroids in treatment of cough.pdf")
        self.TO.Click_Publish_now()
        self.TO.Click_Save()

        try:
            self.driver.find_element_by_xpath("//*[text()=' Title cannot be empty']")
            assert True
            self.driver.close()

        except:
            # To take the Screenshote
            FunName = inspect.currentframe().f_code.co_name
            PREREQUIRMENTS.TAKE_SCREENSHOT(self, FunName)
            assert False

    @pytest.mark.regression
    @pytest.mark.run(order=40)
    def test_Add_Topic_Format2_PDF_without_description(self, setup):
        self.driver = setup
        self.driver.get(BASEURL)

        ##ClassObjects
        self.TO = Topics(self.driver)

        ##PreRequirments
        PREREQUIRMENTS.Login_Success(self, setup)
        Speciality_Name = PREREQUIRMENTS.Add_Specialities_success(self, setup)  ##Add Speciality
        Sub_Speciality_Name = PREREQUIRMENTS.Add_Sub_Specialities_success(self, setup,
                                                                          Speciality_Name)  ##Add Zub Speciality
        Category_Name = PREREQUIRMENTS.Add_Category_success(self, setup)  ##Add Category
        Title = "F2 Title " + PREREQUIRMENTS.random_generator()

        # test start here
        ##PREREQUIRMENTS.Login_Success(self, setup)
        PREREQUIRMENTS.GetURL(self, setup)
        self.TO.Click_on_Topics()
        self.TO.Click_on_Add()
        self.TO.Click_on_specialization(Speciality_Name)
        sleep(1)
        self.TO.select_specialization(Speciality_Name)

        self.TO.Remove_spec_list()
        self.TO.Click_on_Category()
        self.TO.select_Category(Category_Name)
        self.TO.select_format2()
        self.TO.Add_Title(Title)
        self.TO.F2_img_upload("C:/Users/NITHIN/PycharmProjects/ClinicTopics/Admin/ImageFiles/pexels-photo-7144362.jpeg")
        self.TO.F2_select_pdf()
        self.TO.F2_pdf_upload(
            "C:/Users/NITHIN/PycharmProjects/ClinicTopics/Admin/DocumentFiles/SLIDE FLIP PAGE Corticosteroids in treatment of cough.pdf")
        self.TO.Click_Publish_now()
        self.TO.Click_Save()

        try:
            self.driver.find_element_by_xpath("//*[text()=' Description cannot be empty']")
            self.driver.refresh()
            self.TO.Click_on_Topics()
            sleep(3)
            Check = self.TO.Check_Topic_found(Title)
            if Check == 1:
                # To take the Screenshote
                FunName = inspect.currentframe().f_code.co_name
                PREREQUIRMENTS.TAKE_SCREENSHOT(self, FunName)
                assert False
            else:
                assert True
                self.driver.close()
        except:
            # To take the Screenshote
            FunName = inspect.currentframe().f_code.co_name
            PREREQUIRMENTS.TAKE_SCREENSHOT(self, FunName)
            assert False


    @pytest.mark.regression
    @pytest.mark.run(order=41)
    def test_Add_Topic_Format2_PDF_without_Image(self, setup):
        self.driver = setup
        self.driver.get(BASEURL)

        ##ClassObjects
        self.TO = Topics(self.driver)

        ##PreRequirments
        PREREQUIRMENTS.Login_Success(self, setup)
        Speciality_Name = PREREQUIRMENTS.Add_Specialities_success(self, setup)  ##Add Speciality
        Sub_Speciality_Name = PREREQUIRMENTS.Add_Sub_Specialities_success(self, setup,
                                                                          Speciality_Name)  ##Add Zub Speciality
        Category_Name = PREREQUIRMENTS.Add_Category_success(self, setup)  ##Add Category
        Title = "F2 Title " + PREREQUIRMENTS.random_generator()

        # test start here
        ##PREREQUIRMENTS.Login_Success(self, setup)
        PREREQUIRMENTS.GetURL(self, setup)
        self.TO.Click_on_Topics()
        self.TO.Click_on_Add()
        self.TO.Click_on_specialization(Speciality_Name)
        sleep(1)
        self.TO.select_specialization(Speciality_Name)

        self.TO.Remove_spec_list()
        self.TO.Click_on_Category()
        self.TO.select_Category(Category_Name)
        self.TO.select_format2()
        self.TO.Add_Title(Title)
        self.TO.Add_Description("Testwejnfk weyfg bwu jwebfwbefiwehu iuwehfi wiuehdiuwehfi jweniqw")
        self.TO.F2_select_pdf()
        self.TO.F2_pdf_upload("C:/Users/NITHIN/PycharmProjects/ClinicTopics/Admin/DocumentFiles/SLIDE FLIP PAGE Corticosteroids in treatment of cough.pdf")
        self.TO.Click_Publish_now()
        self.TO.Click_Save()

        try:
            self.driver.find_element_by_xpath("//*[text()='Image cannot be empty']")
            self.driver.refresh()
            self.TO.Click_on_Topics()
            sleep(3)
            Check = self.TO.Check_Topic_found(Title)
            if Check == 1:
                # To take the Screenshote
                FunName = inspect.currentframe().f_code.co_name
                PREREQUIRMENTS.TAKE_SCREENSHOT(self, FunName)
                assert False
            else:
                assert True
                self.driver.close()

        except:
            # To take the Screenshote
            FunName = inspect.currentframe().f_code.co_name
            PREREQUIRMENTS.TAKE_SCREENSHOT(self, FunName)
            assert False

    @pytest.mark.regression
    @pytest.mark.run(order=42)
    def test_Add_Topic_Format2_PDF_without_pdf(self, setup):
        self.driver = setup
        self.driver.get(BASEURL)

        ##ClassObjects
        self.TO = Topics(self.driver)

        ##PreRequirments
        PREREQUIRMENTS.Login_Success(self, setup)
        Speciality_Name = PREREQUIRMENTS.Add_Specialities_success(self, setup)  ##Add Speciality
        Sub_Speciality_Name = PREREQUIRMENTS.Add_Sub_Specialities_success(self, setup,
                                                                          Speciality_Name)  ##Add Zub Speciality
        Category_Name = PREREQUIRMENTS.Add_Category_success(self, setup)  ##Add Category
        Title = "F2 Title " + PREREQUIRMENTS.random_generator()

        # test start here
        ##PREREQUIRMENTS.Login_Success(self, setup)
        PREREQUIRMENTS.GetURL(self, setup)
        self.TO.Click_on_Topics()
        self.TO.Click_on_Add()
        self.TO.Click_on_specialization(Speciality_Name)
        sleep(1)
        self.TO.select_specialization(Speciality_Name)

        self.TO.Remove_spec_list()
        self.TO.Click_on_Category()
        self.TO.select_Category(Category_Name)
        self.TO.select_format2()
        self.TO.Add_Title(Title)
        self.TO.Add_Description("Testwejnfk weyfg bwu jwebfwbefiwehu iuwehfi wiuehdiuwehfi jweniqw")
        self.TO.F2_img_upload("C:/Users/NITHIN/PycharmProjects/ClinicTopics/Admin/ImageFiles/pexels-photo-7144362.jpeg")
        self.TO.F2_select_pdf()
        self.TO.Click_Publish_now()
        self.TO.Click_Save()

        try:
            self.driver.find_element_by_xpath("//*[text()='PDF cannot be empty']")
            self.driver.refresh()
            self.TO.Click_on_Topics()
            sleep(3)
            Check = self.TO.Check_Topic_found(Title)
            if Check == 1:
                # To take the Screenshote
                FunName = inspect.currentframe().f_code.co_name
                PREREQUIRMENTS.TAKE_SCREENSHOT(self, FunName)
                assert False
            else:
                assert True
                self.driver.close()

        except:
            # To take the Screenshote
            FunName = inspect.currentframe().f_code.co_name
            PREREQUIRMENTS.TAKE_SCREENSHOT(self, FunName)
            assert False

    @pytest.mark.regression
    @pytest.mark.run(order=43)
    def test_Add_Topic_Format2_PDF_without_ExternalURL(self, setup):
        self.driver = setup
        self.driver.get(BASEURL)

        ##ClassObjects
        self.TO = Topics(self.driver)

        ##PreRequirments
        PREREQUIRMENTS.Login_Success(self, setup)
        Speciality_Name = PREREQUIRMENTS.Add_Specialities_success(self, setup)  ##Add Speciality
        Sub_Speciality_Name = PREREQUIRMENTS.Add_Sub_Specialities_success(self, setup,
                                                                          Speciality_Name)  ##Add Zub Speciality
        Category_Name = PREREQUIRMENTS.Add_Category_success(self, setup)  ##Add Category
        Title = "F2 Title " + PREREQUIRMENTS.random_generator()

        # test start here
        ##PREREQUIRMENTS.Login_Success(self, setup)
        PREREQUIRMENTS.GetURL(self, setup)
        self.TO.Click_on_Topics()
        self.TO.Click_on_Add()
        self.TO.Click_on_specialization(Speciality_Name)
        sleep(1)
        self.TO.select_specialization(Speciality_Name)

        self.TO.Remove_spec_list()
        self.TO.Click_on_Category()
        self.TO.select_Category(Category_Name)
        self.TO.select_format2()
        self.TO.Add_Title(Title)
        self.TO.Add_Description("Testwejnfk weyfg bwu jwebfwbefiwehu iuwehfi wiuehdiuwehfi jweniqw")
        self.TO.F2_img_upload("C:/Users/NITHIN/PycharmProjects/ClinicTopics/Admin/ImageFiles/pexels-photo-7144362.jpeg")
        self.TO.F2_select_ExternalURL()
        self.TO.Click_Publish_now()
        self.TO.Click_Save()

        try:
            self.driver.find_element_by_xpath("//*[text()='External url cannot be empty']")
            self.driver.refresh()
            self.TO.Click_on_Topics()
            sleep(3)
            Check = self.TO.Check_Topic_found(Title)
            if Check == 1:
                # To take the Screenshote
                FunName = inspect.currentframe().f_code.co_name
                PREREQUIRMENTS.TAKE_SCREENSHOT(self, FunName)
                assert False
            else:
                assert True
                self.driver.close()

        except:
            # To take the Screenshote
            FunName = inspect.currentframe().f_code.co_name
            PREREQUIRMENTS.TAKE_SCREENSHOT(self, FunName)
            assert False

class Test_Edit_Topics_F2:

    @pytest.mark.sanity
    @pytest.mark.regression
    @pytest.mark.run(order=44)
    def test_Edit_Topic_Format2_PDF_success(self, setup):
        self.driver = setup
        self.driver.get(BASEURL)

        ##ClassObjects
        self.TO = Topics(self.driver)

        ##PreRequirments
        PREREQUIRMENTS.Login_Success(self, setup)
        Title = PREREQUIRMENTS.Add_Topic_Format2_PDF_success(self, setup)
        NewTitle = "F2 New Title " + PREREQUIRMENTS.random_generator()
        NewSpecialisation_Name = PREREQUIRMENTS.Add_Specialities_success(self, setup)  ##Add Speciality
        NewSub_Speciality_Name = PREREQUIRMENTS.Add_Sub_Specialities_success(self, setup,NewSpecialisation_Name)  ##Add Zub Speciality
        NewCategory_Name = PREREQUIRMENTS.Add_Category_success(self, setup)  ##Add Category

        # test start here
        ##PREREQUIRMENTS.Login_Success(self, setup)
        PREREQUIRMENTS.GetURL(self, setup)
        self.TO.Click_on_Topics()
        self.TO.Click_on_Edit_topic(Title)

        self.TO.Click_on_specialization(NewSub_Speciality_Name)
        sleep(3)
        self.TO.select_specialization(NewSub_Speciality_Name)
        sleep(1)
        self.TO.Remove_spec_list()
        self.TO.Click_on_Category()
        self.TO.select_Category(NewCategory_Name)

        self.TO.Add_Title(NewTitle)
        self.TO.Add_Description("Test Test TEst TEst TEst Test tEtst TRatyys")
        self.TO.F2_img_upload("C:/Users/NITHIN/PycharmProjects/ClinicTopics/Admin/ImageFiles/Signs-of-Diabetes.png")
        self.TO.F2_pdf_upload("C:/Users/NITHIN/PycharmProjects/ClinicTopics/Admin/DocumentFiles/FRONT PAGE_ Corticosteroids in treatment of cough.pdf")
        self.TO.Click_Save()

        self.TO.Click_on_Topics()
        sleep(5)
        Check = self.TO.Check_Topic_found(NewTitle)
        if Check == 1:
            self.TO.Click_on_Topics()
            sleep(3)
            Check = self.TO.Check_Topic_found(Title)
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

    @pytest.mark.sanity
    @pytest.mark.regression
    @pytest.mark.run(order=45)
    def test_Edit_Topic_Format2_External_URL_success(self, setup):
        self.driver = setup
        self.driver.get(BASEURL)

        ##ClassObjects
        self.TO = Topics(self.driver)

        ##PreRequirments
        PREREQUIRMENTS.Login_Success(self, setup)
        Title = PREREQUIRMENTS.Add_Topic_Format2_External_URL_success(self, setup)
        NewTitle = "F2 New Title " + PREREQUIRMENTS.random_generator()
        NewSpecialisation_Name = PREREQUIRMENTS.Add_Specialities_success(self, setup)  ##Add Speciality
        NewSub_Speciality_Name = PREREQUIRMENTS.Add_Sub_Specialities_success(self, setup,NewSpecialisation_Name)  ##Add Zub Speciality
        NewCategory_Name = PREREQUIRMENTS.Add_Category_success(self, setup)  ##Add Category

        # test start here
        ##PREREQUIRMENTS.Login_Success(self, setup)
        PREREQUIRMENTS.GetURL(self, setup)
        self.TO.Click_on_Topics()
        self.TO.Click_on_Edit_topic(Title)

        self.TO.Click_on_specialization(NewSub_Speciality_Name)
        sleep(3)
        self.TO.select_specialization(NewSub_Speciality_Name)
        sleep(1)
        self.TO.Remove_spec_list()
        self.TO.Click_on_Category()
        self.TO.select_Category(NewCategory_Name)

        self.TO.Add_Title(NewTitle)
        self.TO.Add_Description("Test Test TEst TEst TEst Test tEtst TRatyys")
        self.TO.F2_img_upload("C:/Users/NITHIN/PycharmProjects/ClinicTopics/Admin/ImageFiles/Signs-of-Diabetes.png")
        self.TO.F2_ExternalURL_add("https://www.facebook.com/")
        self.TO.Click_Save()

        self.TO.Click_on_Topics()
        sleep(5)
        Check = self.TO.Check_Topic_found(NewTitle)
        if Check == 1:
            self.TO.Click_on_Topics()
            sleep(3)
            Check = self.TO.Check_Topic_found(Title)
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


class Test_Add_Topics_F3:
    @pytest.mark.sanity
    @pytest.mark.regression
    @pytest.mark.run(order=46)
    def test_Add_Topic_Format3_PDF_success(self, setup):
        self.driver = setup
        self.driver.get(BASEURL)

        ##ClassObjects
        self.TO = Topics(self.driver)

        ##PreRequirments
        PREREQUIRMENTS.Login_Success(self, setup)
        Speciality_Name = PREREQUIRMENTS.Add_Specialities_success(self, setup)  ##Add Speciality
        Sub_Speciality_Name = PREREQUIRMENTS.Add_Sub_Specialities_success(self, setup,Speciality_Name)  ##Add Zub Speciality
        Category_Name = PREREQUIRMENTS.Add_Category_success(self, setup)  ##Add Category
        Title = "F3 Title " + PREREQUIRMENTS.random_generator()

        # test start here
        ##PREREQUIRMENTS.Login_Success(self, setup)
        PREREQUIRMENTS.GetURL(self, setup)
        self.TO.Click_on_Topics()
        self.TO.Click_on_Add()
        self.TO.Click_on_specialization(Speciality_Name)
        sleep(1)
        self.TO.select_specialization(Speciality_Name)

        self.TO.Remove_spec_list()
        self.TO.Click_on_Category()
        self.TO.select_Category(Category_Name)
        self.TO.select_format3()
        self.TO.Add_Title(Title)
        self.TO.Add_Description("Testwejnfk weyfg bwu jwebfwbefiwehu iuwehfi wiuehdiuwehfi jweniqw")
        self.TO.F3_VideoURL_add("https://player.vimeo.com/video/577145762")
        self.TO.F2_select_pdf()
        self.TO.F2_pdf_upload("C:/Users/NITHIN/PycharmProjects/ClinicTopics/Admin/DocumentFiles/SLIDE FLIP PAGE Corticosteroids in treatment of cough.pdf")
        self.TO.Click_Publish_now()
        self.TO.Click_Save()

        self.TO.Click_on_Topics()
        sleep(3)
        Check = self.TO.Check_Topic_found(Title)
        if Check == 1:
            assert True
            self.driver.close()
        else:
            # To take the Screenshote
            FunName = inspect.currentframe().f_code.co_name
            PREREQUIRMENTS.TAKE_SCREENSHOT(self, FunName)
            assert False

    @pytest.mark.sanity
    @pytest.mark.regression
    @pytest.mark.run(order=47)
    def test_Add_Topic_Format3_ExternalURL_success(self, setup):
        self.driver = setup
        self.driver.get(BASEURL)

        ##ClassObjects
        self.TO = Topics(self.driver)

        ##PreRequirments
        PREREQUIRMENTS.Login_Success(self, setup)
        Speciality_Name = PREREQUIRMENTS.Add_Specialities_success(self, setup)  ##Add Speciality
        Sub_Speciality_Name = PREREQUIRMENTS.Add_Sub_Specialities_success(self, setup,
                                                                          Speciality_Name)  ##Add Zub Speciality
        Category_Name = PREREQUIRMENTS.Add_Category_success(self, setup)  ##Add Category
        Title = "F3 Title " + PREREQUIRMENTS.random_generator()

        # test start here
        ##PREREQUIRMENTS.Login_Success(self, setup)
        PREREQUIRMENTS.GetURL(self, setup)
        self.TO.Click_on_Topics()
        self.TO.Click_on_Add()
        self.TO.Click_on_specialization(Speciality_Name)
        sleep(1)
        self.TO.select_specialization(Speciality_Name)

        self.TO.Remove_spec_list()
        self.TO.Click_on_Category()
        self.TO.select_Category(Category_Name)
        self.TO.select_format3()
        self.TO.Add_Title(Title)
        self.TO.Add_Description("Testwejnfk weyfg bwu jwebfwbefiwehu iuwehfi wiuehdiuwehfi jweniqw")
        self.TO.F3_VideoURL_add("https://player.vimeo.com/video/577145762")
        self.TO.F2_select_ExternalURL()
        self.TO.F2_ExternalURL_add("https://www.google.co.in/")

        self.TO.Click_Publish_now()
        self.TO.Click_Save()

        self.TO.Click_on_Topics()
        sleep(3)
        Check = self.TO.Check_Topic_found(Title)
        if Check == 1:
            assert True
            self.driver.close()
        else:
            # To take the Screenshote
            FunName = inspect.currentframe().f_code.co_name
            PREREQUIRMENTS.TAKE_SCREENSHOT(self, FunName)
            assert False

    @pytest.mark.regression
    @pytest.mark.run(order=48)
    def test_Add_Topic_Format3_PDF_fail_without_title(self, setup):
        self.driver = setup
        self.driver.get(BASEURL)

        ##ClassObjects
        self.TO = Topics(self.driver)

        ##PreRequirments
        PREREQUIRMENTS.Login_Success(self, setup)
        Speciality_Name = PREREQUIRMENTS.Add_Specialities_success(self, setup)  ##Add Speciality
        Sub_Speciality_Name = PREREQUIRMENTS.Add_Sub_Specialities_success(self, setup,
                                                                          Speciality_Name)  ##Add Zub Speciality
        Category_Name = PREREQUIRMENTS.Add_Category_success(self, setup)  ##Add Category

        # test start here
        ##PREREQUIRMENTS.Login_Success(self, setup)
        PREREQUIRMENTS.GetURL(self, setup)
        self.TO.Click_on_Topics()
        self.TO.Click_on_Add()
        self.TO.Click_on_specialization(Speciality_Name)
        sleep(1)
        self.TO.select_specialization(Speciality_Name)

        self.TO.Remove_spec_list()
        self.TO.Click_on_Category()
        self.TO.select_Category(Category_Name)
        self.TO.select_format3()
        self.TO.Add_Description("Testwejnfk weyfg bwu jwebfwbefiwehu iuwehfi wiuehdiuwehfi jweniqw")
        self.TO.F3_VideoURL_add("https://player.vimeo.com/video/577145762")
        self.TO.F2_select_pdf()
        self.TO.F2_pdf_upload("C:/Users/NITHIN/PycharmProjects/ClinicTopics/Admin/DocumentFiles/SLIDE FLIP PAGE Corticosteroids in treatment of cough.pdf")
        self.TO.Click_Publish_now()
        self.TO.Click_Save()

        try:
            self.driver.find_element_by_xpath("//*[text()=' Title cannot be empty']")
            assert True
            self.driver.close()
        except:
            # To take the Screenshote
            FunName = inspect.currentframe().f_code.co_name
            PREREQUIRMENTS.TAKE_SCREENSHOT(self, FunName)
            assert False


    @pytest.mark.regression
    @pytest.mark.run(order=49)
    def test_Add_Topic_Format3_PDF_fail_without_description(self, setup):
        self.driver = setup
        self.driver.get(BASEURL)

        ##ClassObjects
        self.TO = Topics(self.driver)

        ##PreRequirments
        PREREQUIRMENTS.Login_Success(self, setup)
        Speciality_Name = PREREQUIRMENTS.Add_Specialities_success(self, setup)  ##Add Speciality
        Sub_Speciality_Name = PREREQUIRMENTS.Add_Sub_Specialities_success(self, setup,Speciality_Name)  ##Add Zub Speciality
        Category_Name = PREREQUIRMENTS.Add_Category_success(self, setup)  ##Add Category
        Title = "F3 Title " + PREREQUIRMENTS.random_generator()

        # test start here
        ##PREREQUIRMENTS.Login_Success(self, setup)
        PREREQUIRMENTS.GetURL(self, setup)
        self.TO.Click_on_Topics()
        self.TO.Click_on_Add()
        self.TO.Click_on_specialization(Speciality_Name)
        sleep(1)
        self.TO.select_specialization(Speciality_Name)

        self.TO.Remove_spec_list()
        self.TO.Click_on_Category()
        self.TO.select_Category(Category_Name)
        self.TO.select_format3()
        self.TO.Add_Title(Title)
        self.TO.F3_VideoURL_add("https://player.vimeo.com/video/577145762")
        self.TO.F2_select_pdf()
        self.TO.F2_pdf_upload("C:/Users/NITHIN/PycharmProjects/ClinicTopics/Admin/DocumentFiles/SLIDE FLIP PAGE Corticosteroids in treatment of cough.pdf")
        self.TO.Click_Publish_now()
        self.TO.Click_Save()

        try:
            self.driver.find_element_by_xpath("//*[text()=' Description cannot be empty']")
            self.driver.refresh()
            self.TO.Click_on_Topics()
            sleep(3)
            Check = self.TO.Check_Topic_found(Title)
            if Check == 1:
                # To take the Screenshote
                FunName = inspect.currentframe().f_code.co_name
                PREREQUIRMENTS.TAKE_SCREENSHOT(self, FunName)
                assert False
            else:
                assert True
                self.driver.close()
        except:
            # To take the Screenshote
            FunName = inspect.currentframe().f_code.co_name
            PREREQUIRMENTS.TAKE_SCREENSHOT(self, FunName)
            assert False


    @pytest.mark.regression
    @pytest.mark.run(order=50)
    def test_Add_Topic_Format3_without_videoURL(self, setup):
        self.driver = setup
        self.driver.get(BASEURL)

        ##ClassObjects
        self.TO = Topics(self.driver)

        ##PreRequirments
        PREREQUIRMENTS.Login_Success(self, setup)
        Speciality_Name = PREREQUIRMENTS.Add_Specialities_success(self, setup)  ##Add Speciality
        Sub_Speciality_Name = PREREQUIRMENTS.Add_Sub_Specialities_success(self, setup,
                                                                          Speciality_Name)  ##Add Zub Speciality
        Category_Name = PREREQUIRMENTS.Add_Category_success(self, setup)  ##Add Category
        Title = "F3 Title " + PREREQUIRMENTS.random_generator()

        # test start here
        ##PREREQUIRMENTS.Login_Success(self, setup)
        PREREQUIRMENTS.GetURL(self, setup)
        self.TO.Click_on_Topics()
        self.TO.Click_on_Add()
        self.TO.Click_on_specialization(Speciality_Name)
        sleep(1)
        self.TO.select_specialization(Speciality_Name)

        self.TO.Remove_spec_list()
        self.TO.Click_on_Category()
        self.TO.select_Category(Category_Name)
        self.TO.select_format3()
        self.TO.Add_Title(Title)
        self.TO.Add_Description("Testwejnfk weyfg bwu jwebfwbefiwehu iuwehfi wiuehdiuwehfi jweniqw")
        self.TO.F2_select_pdf()
        self.TO.F2_pdf_upload("C:/Users/NITHIN/PycharmProjects/ClinicTopics/Admin/DocumentFiles/SLIDE FLIP PAGE Corticosteroids in treatment of cough.pdf")
        self.TO.Click_Publish_now()
        self.TO.Click_Save()

        try:
            self.driver.find_element_by_xpath("//*[text()='Video url cannot be empty']")
            self.driver.refresh()
            self.TO.Click_on_Topics()
            sleep(3)
            Check = self.TO.Check_Topic_found(Title)
            if Check == 1:
                # To take the Screenshote
                FunName = inspect.currentframe().f_code.co_name
                PREREQUIRMENTS.TAKE_SCREENSHOT(self, FunName)
                assert False
            else:
                assert True
                self.driver.close()

        except:
            # To take the Screenshote
            FunName = inspect.currentframe().f_code.co_name
            PREREQUIRMENTS.TAKE_SCREENSHOT(self, FunName)
            assert False

    @pytest.mark.regression
    @pytest.mark.run(order=51)
    def test_Add_Topic_Format3_without_PDF(self, setup):
        self.driver = setup
        self.driver.get(BASEURL)

        ##ClassObjects
        self.TO = Topics(self.driver)

        ##PreRequirments
        PREREQUIRMENTS.Login_Success(self, setup)
        Speciality_Name = PREREQUIRMENTS.Add_Specialities_success(self, setup)  ##Add Speciality
        Sub_Speciality_Name = PREREQUIRMENTS.Add_Sub_Specialities_success(self, setup,
                                                                          Speciality_Name)  ##Add Zub Speciality
        Category_Name = PREREQUIRMENTS.Add_Category_success(self, setup)  ##Add Category
        Title = "F3 Title " + PREREQUIRMENTS.random_generator()

        # test start here
        ##PREREQUIRMENTS.Login_Success(self, setup)
        PREREQUIRMENTS.GetURL(self, setup)
        self.TO.Click_on_Topics()
        self.TO.Click_on_Add()
        self.TO.Click_on_specialization(Speciality_Name)
        sleep(1)
        self.TO.select_specialization(Speciality_Name)

        self.TO.Remove_spec_list()
        self.TO.Click_on_Category()
        self.TO.select_Category(Category_Name)
        self.TO.select_format3()
        self.TO.Add_Title(Title)
        self.TO.Add_Description("Testwejnfk weyfg bwu jwebfwbefiwehu iuwehfi wiuehdiuwehfi jweniqw")
        self.TO.F3_VideoURL_add("https://player.vimeo.com/video/577145762")
        self.TO.F2_select_pdf()
        self.TO.Click_Publish_now()
        self.TO.Click_Save()

        try:
            self.driver.find_element_by_xpath("//*[text()=' PDF cannot be empty']")
            self.driver.refresh()
            self.TO.Click_on_Topics()
            sleep(3)
            Check = self.TO.Check_Topic_found(Title)
            if Check == 1:
                # To take the Screenshote
                FunName = inspect.currentframe().f_code.co_name
                PREREQUIRMENTS.TAKE_SCREENSHOT(self, FunName)
                assert False
            else:
                assert True
                self.driver.close()

        except:
            # To take the Screenshote
            FunName = inspect.currentframe().f_code.co_name
            PREREQUIRMENTS.TAKE_SCREENSHOT(self, FunName)
            assert False

    @pytest.mark.regression
    @pytest.mark.run(order=52)
    def test_Add_Topic_Format3_without_ExternalURL(self, setup):
        self.driver = setup
        self.driver.get(BASEURL)

        ##ClassObjects
        self.TO = Topics(self.driver)

        ##PreRequirments
        PREREQUIRMENTS.Login_Success(self, setup)
        Speciality_Name = PREREQUIRMENTS.Add_Specialities_success(self, setup)  ##Add Speciality
        Sub_Speciality_Name = PREREQUIRMENTS.Add_Sub_Specialities_success(self, setup,Speciality_Name)  ##Add Zub Speciality
        Category_Name = PREREQUIRMENTS.Add_Category_success(self, setup)  ##Add Category
        Title = "F3 Title " + PREREQUIRMENTS.random_generator()

        # test start here
        ##PREREQUIRMENTS.Login_Success(self, setup)
        PREREQUIRMENTS.GetURL(self, setup)
        self.TO.Click_on_Topics()
        self.TO.Click_on_Add()
        self.TO.Click_on_specialization(Speciality_Name)
        sleep(1)
        self.TO.select_specialization(Speciality_Name)

        self.TO.Remove_spec_list()
        self.TO.Click_on_Category()
        self.TO.select_Category(Category_Name)
        self.TO.select_format3()
        self.TO.Add_Title(Title)
        self.TO.Add_Description("Testwejnfk weyfg bwu jwebfwbefiwehu iuwehfi wiuehdiuwehfi jweniqw")
        self.TO.F3_VideoURL_add("https://player.vimeo.com/video/577145762")
        self.TO.F2_select_ExternalURL()

        self.TO.Click_Publish_now()
        self.TO.Click_Save()

        try:
            self.driver.find_element_by_xpath("//*[text()=' External url cannot be empty']")
            self.driver.refresh()
            self.TO.Click_on_Topics()
            sleep(3)
            Check = self.TO.Check_Topic_found(Title)
            if Check == 1:
                # To take the Screenshote
                FunName = inspect.currentframe().f_code.co_name
                PREREQUIRMENTS.TAKE_SCREENSHOT(self, FunName)
                assert False
            else:
                assert True
                self.driver.close()

        except:
            # To take the Screenshote
            FunName = inspect.currentframe().f_code.co_name
            PREREQUIRMENTS.TAKE_SCREENSHOT(self, FunName)
            assert False

class Test_Edit_Topics_F3:

    @pytest.mark.sanity
    @pytest.mark.regression
    @pytest.mark.run(order=53)
    def test_Edit_Topic_Format3_PDF_success(self, setup):
        self.driver = setup
        self.driver.get(BASEURL)

        ##ClassObjects
        self.TO = Topics(self.driver)

        ##PreRequirments
        PREREQUIRMENTS.Login_Success(self, setup)
        Title = PREREQUIRMENTS.Add_Topic_Format3_PDF_success(self, setup)
        NewTitle = "F2 New Title " + PREREQUIRMENTS.random_generator()
        NewSpecialisation_Name = PREREQUIRMENTS.Add_Specialities_success(self, setup)  ##Add Speciality
        NewSub_Speciality_Name = PREREQUIRMENTS.Add_Sub_Specialities_success(self, setup,NewSpecialisation_Name)  ##Add Zub Speciality
        NewCategory_Name = PREREQUIRMENTS.Add_Category_success(self, setup)  ##Add Category

        # test start here
        ##PREREQUIRMENTS.Login_Success(self, setup)
        PREREQUIRMENTS.GetURL(self, setup)
        self.TO.Click_on_Topics()
        self.TO.Click_on_Edit_topic(Title)

        self.TO.Click_on_specialization(NewSub_Speciality_Name)
        sleep(3)
        self.TO.select_specialization(NewSub_Speciality_Name)
        sleep(1)
        self.TO.Remove_spec_list()
        self.TO.Click_on_Category()
        self.TO.select_Category(NewCategory_Name)

        self.TO.Add_Title(NewTitle)
        self.TO.Add_Description("Test Test TEst TEst TEst Test tEtst TRatyys")
        self.TO.F3_VideoURL_add("https://player.vimeo.com/video/577151758")
        self.TO.F2_pdf_upload("C:/Users/NITHIN/PycharmProjects/ClinicTopics/Admin/DocumentFiles/FRONT PAGE_ Corticosteroids in treatment of cough.pdf")
        self.TO.Click_Save()

        self.TO.Click_on_Topics()
        sleep(5)
        Check = self.TO.Check_Topic_found(NewTitle)
        if Check == 1:
            self.TO.Click_on_Topics()
            sleep(3)
            Check = self.TO.Check_Topic_found(Title)
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

    @pytest.mark.sanity
    @pytest.mark.regression
    @pytest.mark.run(order=54)
    def test_Edit_Topic_Format3_External_URL_success(self, setup):
        self.driver = setup
        self.driver.get(BASEURL)

        ##ClassObjects
        self.TO = Topics(self.driver)

        ##PreRequirments
        PREREQUIRMENTS.Login_Success(self, setup)
        Title = PREREQUIRMENTS.Add_Topic_Format3_External_URL_success(self, setup)
        NewTitle = "F2 New Title " + PREREQUIRMENTS.random_generator()
        NewSpecialisation_Name = PREREQUIRMENTS.Add_Specialities_success(self, setup)  ##Add Speciality
        NewSub_Speciality_Name = PREREQUIRMENTS.Add_Sub_Specialities_success(self, setup,NewSpecialisation_Name)  ##Add Zub Speciality
        NewCategory_Name = PREREQUIRMENTS.Add_Category_success(self, setup)  ##Add Category

        # test start here
        ##PREREQUIRMENTS.Login_Success(self, setup)
        PREREQUIRMENTS.GetURL(self, setup)
        self.TO.Click_on_Topics()
        self.TO.Click_on_Edit_topic(Title)

        self.TO.Click_on_specialization(NewSub_Speciality_Name)
        sleep(3)
        self.TO.select_specialization(NewSub_Speciality_Name)
        sleep(1)
        self.TO.Remove_spec_list()
        self.TO.Click_on_Category()
        self.TO.select_Category(NewCategory_Name)

        self.TO.Add_Title(NewTitle)
        self.TO.Add_Description("Test Test TEst TEst TEst Test tEtst TRatyys")
        self.TO.F3_VideoURL_add("https://player.vimeo.com/video/577151758")
        self.TO.F2_ExternalURL_add("https://www.facebook.com/")
        self.TO.Click_Save()

        self.TO.Click_on_Topics()
        sleep(5)
        Check = self.TO.Check_Topic_found(NewTitle)
        if Check == 1:
            self.TO.Click_on_Topics()
            sleep(3)
            Check = self.TO.Check_Topic_found(Title)
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


class Test_Delete_Topic:
    @pytest.mark.sanity
    @pytest.mark.regression
    @pytest.mark.run(order=55)
    def test_Delete_Topic_success(self, setup):
        self.driver = setup
        self.driver.get(BASEURL)

        ##ClassObjects
        self.TO = Topics(self.driver)

        ##PreRequirments
        PREREQUIRMENTS.Login_Success(self, setup)
        Title = PREREQUIRMENTS.Add_Topic_Format3_PDF_success(self, setup)

        # test start here
        ##PREREQUIRMENTS.Login_Success(self, setup)
        PREREQUIRMENTS.GetURL(self, setup)
        self.TO.Click_on_Topics()
        self.TO.Click_on_Delete_topic(Title)
        self.TO.Confirm_delete()

        self.TO.Click_on_Topics()
        sleep(5)
        Check = self.TO.Check_Topic_found(Title)
        if Check == 1:
            # To take the Screenshote
            FunName = inspect.currentframe().f_code.co_name
            PREREQUIRMENTS.TAKE_SCREENSHOT(self, FunName)
            assert False
        else:
            assert True
            self.driver.close()
