
import datetime
from Admin.Pageobjectives.Login_Admin import LoginAdmin
from Admin.Pageobjectives.Category import Category
from Admin.Pageobjectives.Specialities import Specialities
from Admin.Pageobjectives.Topic import Topics
from Admin.Pageobjectives.Quiz import Quiz
from Admin.Pageobjectives.General_Ad import General_Ad
from Admin.Utilities.readproperties import ReadConfig
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import string
import random
from time import sleep
import inspect

BASEURL=ReadConfig.getBaseuRL()


class PREREQUIRMENTS:

    @staticmethod
    def TAKE_SCREENSHOT(self,Methodname):
        # To take the Screenshot
        now = datetime.datetime.now()
        dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
        #date_stamp = str(datetime.datetime.now()).split('//')[1].split('.')[0]
        filename = "Clinic_Topics_"+dt_string
        self.driver.save_screenshot("C:/Users/NITHIN/PycharmProjects/ClinicTopics/Admin/Screenshots/"+Methodname+".png")

    # Create Random string
    @staticmethod
    def random_generator(size=8, chars=string.ascii_lowercase):
        return ''.join(random.choice(chars) for x in range(7))

    @staticmethod
    def Login_Success(self, setup):
        self.driver = setup
        self.driver.get(BASEURL)

        ##ClassObjects
        self.LA = LoginAdmin(self.driver)

        #test start here
        self.LA.Login_Success()
        ExpectedURL="https://clinictest.metrictreelabs.com/data"
        try:
            WebDriverWait(self.driver, 10).until(EC.url_to_be(ExpectedURL))  # Wait for the next page to load
            assert True

        except:
            # To take the Screenshote
            FunName = inspect.currentframe().f_code.co_name
            PREREQUIRMENTS.TAKE_SCREENSHOT(self, FunName)
            assert False

    @staticmethod
    def GetURL(self, setup):
        self.driver = setup
        self.driver.get(BASEURL)

    @staticmethod
    def Add_Category_success(self, setup):
        self.driver = setup
        self.driver.get(BASEURL)


        ##ClassObjects
        self.CA = Category(self.driver)

        # test start here
        ##PREREQUIRMENTS.Login_Success(self, setup)
        PREREQUIRMENTS.GetURL(self, setup)
        self.CA.Click_on_Category()
        self.CA.Click_on_add()

        Category_name = "CAT" + PREREQUIRMENTS.random_generator()  # cReating Random Category name
        self.CA.Add_Name(Category_name)
        self.CA.Add_image("C:/Users/NITHIN/PycharmProjects/ClinicTopics/Admin/ImageFiles/pexels-photo-7144362.jpeg")
        self.CA.Save()
        Check = self.CA.Check_Categry_name(Category_name)
        if Check == 1:
            assert True
            return Category_name
        else:
            # To take the Screenshote
            FunName = inspect.currentframe().f_code.co_name
            PREREQUIRMENTS.TAKE_SCREENSHOT(self, FunName)
            assert False

    @staticmethod
    def Add_Specialities_success(self, setup):
        self.driver = setup
        self.driver.get(BASEURL)

        ##ClassObjects
        self.SP = Specialities(self.driver)

        # test start here
        ##PREREQUIRMENTS.Login_Success(self, setup)
        PREREQUIRMENTS.GetURL(self, setup)
        self.SP.Click_on_Specialities()
        self.SP.Click_on_Add()
        Speci_Name="SPEC" + PREREQUIRMENTS.random_generator()  # cReating Random Speciality name
        self.SP.Add_name(Speci_Name)
        self.SP.Click_Save()

        Check = self.SP.Check_Speciality_name(Speci_Name)
        if Check == 1:
            assert True
            return Speci_Name
        else:
            # To take the Screenshote
            FunName = inspect.currentframe().f_code.co_name
            PREREQUIRMENTS.TAKE_SCREENSHOT(self, FunName)
            assert False

    @staticmethod
    def Add_Sub_Specialities_success(self, setup,Speciality_Name):
        self.driver = setup
        self.driver.get(BASEURL)

        ##ClassObjects
        self.SP = Specialities(self.driver)

        # test start here
        ##PREREQUIRMENTS.Login_Success(self, setup)
        PREREQUIRMENTS.GetURL(self, setup)
        self.SP.Click_on_Specialities()
        self.SP.Click_Sub_spacialities(Speciality_Name)
        self.SP.Click_on_Add()
        SpeciSub__Name = "SUBSPEC" + PREREQUIRMENTS.random_generator()  # cReating Random Speciality name
        self.SP.Add_name(SpeciSub__Name)
        self.SP.Click_Save()

        Check = self.SP.Check_Speciality_name(SpeciSub__Name)
        if Check == 1:
            assert True
            return SpeciSub__Name

        else:
            # To take the Screenshote
            FunName = inspect.currentframe().f_code.co_name
            PREREQUIRMENTS.TAKE_SCREENSHOT(self, FunName)
            assert False

    @staticmethod
    def Add_Topic_Format1_success(self, setup):
        self.driver = setup
        self.driver.get(BASEURL)

        ##ClassObjects
        self.TO = Topics(self.driver)

        ##PreRequirments
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
        self.TO.Click_Publish_now()
        self.TO.Click_Save()

        self.TO.Click_on_Topics()
        sleep(5)
        Check = self.TO.Check_Topic_found(Title)
        if Check == 1:
            assert True
            return Title
        else:
            # To take the Screenshote
            FunName = inspect.currentframe().f_code.co_name
            PREREQUIRMENTS.TAKE_SCREENSHOT(self, FunName)
            assert False

    @staticmethod
    def Add_Topic_Format2_PDF_success(self, setup):
        self.driver = setup
        self.driver.get(BASEURL)

        ##ClassObjects
        self.TO = Topics(self.driver)

        ##PreRequirments
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
        sleep(5)
        Check = self.TO.Check_Topic_found(Title)
        if Check == 1:
            assert True
            return Title
        else:
            # To take the Screenshote
            FunName = inspect.currentframe().f_code.co_name
            PREREQUIRMENTS.TAKE_SCREENSHOT(self, FunName)
            assert False

    @staticmethod
    def Add_Topic_Format2_External_URL_success(self, setup):
        self.driver = setup
        self.driver.get(BASEURL)

        ##ClassObjects
        self.TO = Topics(self.driver)

        ##PreRequirments
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
            return Title
        else:
            # To take the Screenshote
            FunName = inspect.currentframe().f_code.co_name
            PREREQUIRMENTS.TAKE_SCREENSHOT(self, FunName)
            assert False

    @staticmethod
    def Add_Topic_Format3_PDF_success(self, setup):
        self.driver = setup
        self.driver.get(BASEURL)

        ##ClassObjects
        self.TO = Topics(self.driver)

        ##PreRequirments
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
        self.TO.F2_pdf_upload("C:/Users/NITHIN/PycharmProjects/ClinicTopics/Admin/DocumentFiles/SLIDE FLIP PAGE Corticosteroids in treatment of cough.pdf")
        self.TO.Click_Publish_now()
        self.TO.Click_Save()

        self.TO.Click_on_Topics()
        sleep(5)
        Check = self.TO.Check_Topic_found(Title)
        if Check == 1:
            assert True
            return Title
        else:
            # To take the Screenshote
            FunName = inspect.currentframe().f_code.co_name
            PREREQUIRMENTS.TAKE_SCREENSHOT(self, FunName)
            assert False

    @staticmethod
    def Add_Topic_Format3_External_URL_success(self, setup):
        self.driver = setup
        self.driver.get(BASEURL)

        ##ClassObjects
        self.TO = Topics(self.driver)

        ##PreRequirments
        #PREREQUIRMENTS.Login_Success(self, setup)
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
            return Title
        else:
            # To take the Screenshote
            FunName = inspect.currentframe().f_code.co_name
            PREREQUIRMENTS.TAKE_SCREENSHOT(self, FunName)
            assert False

    @staticmethod
    def Add_Quiz(self, setup):
        self.driver = setup
        self.driver.get(BASEURL)

        ##ClassObjects
        self.QU = Quiz(self.driver)

        ##PreRequirments
        #PREREQUIRMENTS.Login_Success(self, setup)
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
            return Title
        else:
            # To take the Screenshote
            FunName = inspect.currentframe().f_code.co_name
            PREREQUIRMENTS.TAKE_SCREENSHOT(self, FunName)
            assert False

    @staticmethod
    def Add_General_Ad(self, setup):
        self.driver = setup
        self.driver.get(BASEURL)

        ##ClassObjects
        self.GA = General_Ad(self.driver)

        ##PreRequirments
        #PREREQUIRMENTS.Login_Success(self, setup)
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
        self.GA.Enable_status()
        self.GA.Click_save()

        self.GA.Click_on_General_ad()
        sleep(2)
        Found = self.GA.Check_Ad_found(Title)
        if Found == 1:
            assert True
            return Title
        else:
            # To take the Screenshote
            FunName = inspect.currentframe().f_code.co_name
            PREREQUIRMENTS.TAKE_SCREENSHOT(self, FunName)
            assert False






