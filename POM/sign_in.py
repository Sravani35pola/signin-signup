#from selenium import webdriver
from selenium.webdriver.support.select import Select
from LIBRARY.config import Config
from DATA.reading_objects import ReadExcel
import time
class Sign_in:
    obj_1=ReadExcel()
    locator_n=obj_1.read_locators("register12")

    def __init__(self,driver):
        self.driver = driver

    def sign_in_block(self):
        locator=self.locator_n["signin_block"]
        self.driver.find_element(*locator).click()
        time.sleep(3)
    def sign_in(self):
        locator=self.locator_n["signin"]
        #self.driver.find_element("xpath",'//li[text()="Sign In/Sign Up"]').click()
        # locator = self.locator_n["signin"]
        self.driver.find_element(*locator).click()
        time.sleep(3)
        # time.sleep(3)
    def iframe(self):
        locator=self.locator_n["iframe"]
        ele=self.driver.find_element(*locator)
        self.driver.switch_to.frame(ele)
    def phonenumber(self,number):
        locator=self.locator_n["Phonenumber"]
        self.driver.find_element(*locator).send_keys(number)
    def recaptcha(self):
        locator=self.locator_n["Recaptcha"]
        self.driver.find_element(*locator).click()
        time.sleep(30)
    def otp(self):
         locator=self.locator_n["Generate otp"]
         self.driver.find_element(*locator).click()
         time.sleep(30)
    def verify(self):
        locator=self.locator_n["Verify user"]
        self.driver.find_element(*locator).click()
    # def username(self,name):
    #     #locator=self.locator_n["Username"]
    #     self.driver.find_element("xpath",'//input[@id="updateName"]').send_keys(name)
    # def user_mail(self,email):
    #      #locator=self.locator_n["Email"]
    #      self.driver.find_element("xpath",'//input[@id="updateEmail"]').send_keys(email)
    # def confirm(self):
    #     #locator=self.locator_n["Confirm"]
    #     self.driver.find_element("xpath",'//button[text()="CREATE PROFILE"]').click()
    #     time.sleep(5)



























#     def signin_with_google(self):
#         # ele = self.driver.find_element("xpath", '//iframe[@class="modalIframe"]')
#         # self.driver.switch_to.frame(ele)
#         locator=self.locator_n["signin_with_google"]
#         self.driver.find_element(*locator).click()
#         time.sleep(3)
#
#     def create_account(self):
#          handles =self.driver.window_handles
#          self.driver.switch_to.window(handles[1])
#          locator=self.locator_n["create account"]
#          self.driver.find_element(*locator).click()
#          time.sleep(3)
#     def first_name(self,firstname):
#         ele1 =self.driver.window_handles
#         self.driver.switch_to.window(ele1[1])
#         ele2 = self.driver.switch_to.default_content()
#         self.driver.switch_to.frame(ele2)
#         time.sleep(2)
#         locator=self.locator_n["firstname"]
#         self.driver.find_element(*locator).send_keys(firstname)
#
#     def last_name(self,lastname):
#         locator=self.locator_n["lastname"]
#         self.driver.find_element(*locator).send_keys(lastname)
#         time.sleep(3)
#     def user_name(self,username):
#         locator=self.locator_n["username"]
#         self.driver.find_element(*locator).send_keys(username)
#
#     def password(self,password):
#         locator=self.locator_n["password"]
#         self.driver.find_element(*locator).send_keys(password)
#     def confirm_password(self,confirmpassword):
#         locator=self.locator_n["confirm password"]
#         self.driver.find_element(*locator).send_keys(confirmpassword)
#     def check_box(self):
#         locator=self.locator_n["checkbox"]
#         self.driver.find_element(*locator).click()
#     def  next(self):
#         locator=self.locator_n["next"]
#         self.driver.find_element(*locator).click()
#     def phonenumber(self,phonenumber):
#         locator=self.locator_n["phonenumber"]
#         self.driver.find_element(*locator).send_keys(phonenumber)
#         time.sleep(5)
#     def next1(self):
#         locator=self.locator_n["next1"]
#         self.driver.find_element(*locator).click()
#         time.sleep(30)
#     def verication(self):
#         locator=self.locator_n["verification"]
#         self.driver.find_element(*locator).click()
#     def day(self,day):
#         locator=self.locator_n["day"]
#         self.driver.find_element(*locator).send_keys(day)
#     def month(self):
#         ele = self.driver.find_element("xpath", "//select[@id='month']")
#         sel_obj = Select(ele)
#         sel_obj.select_by_visible_text("August")
#         time.sleep(2)
#     def date(self,date):
#        locator=self.locator_n["date"]
#        self.driver.find_element(*locator).send_keys(date)
#     def gender(self):
#         ele1 = self.driver.find_element("xpath", "//select[@id='gender']")  # to select the gender
#         sel_obj1 = Select(ele1)
#         sel_obj1.select_by_visible_text("Female")
#     def next_2(self):
#         locator=self.locator_n["next2"]
#         self.driver.find_element(*locator).click()  # to click on next
#         time.sleep(5)
#     def yes_i_agree(self):
#         locator=self.locator_n["I agree"]
#         self.driver.find_element(*locator).click()
# #
# #
# #
# # # lg=Sign_in()
# # # lg.sign_in_block()
# # # lg. sign_in()
# # # lg.signin_with_google()
# # # lg.create_account()
# # # lg.first_name()
# # # lg.last_name()
# # # lg.user_name()
# # # lg.password()
# # # lg.confirm_password()
# # # lg.check_box()
# # # lg.next()
# # # lg.phonenumber()
# # # lg.next1()
# # # lg.verication()
# # # lg.day()
# # # lg.month()
# # # lg.date()
# # # lg.gender()
# # # lg.next_2()
# # # lg.yes_i_agree()
#
#
#


























































































# from DATA import reading_objects
# login_=reading_objects.read_locators()
# from selenium import webdriver
# from selenium.webdriver.support.select import Select
# import time
# # # from DATA import reading_objects
# # # sign_in=reading_objects.read_locators()
# path=r"C:\Users\Sravani\Downloads\chromedriver_win32\chromedriver.exe"
# driver_obj=webdriver.Chrome(path)
# driver_obj.get("https://www.redbus.in/")
# driver_obj.implicitly_wait(30)
# driver_obj.maximize_window()
# #from selenium.webdriver.support.select import Select
# from DATA import reading_objects
# login_=reading_objects.read_locators()
# # import time
# # driver_obj.implicitly_wait(30)
# # driver_obj.maximize_window()
#
# #print(login_)
#
#
# class Sign_in:
#     # def _init_(self,driver_obj):
#     #     self.driver=driver_obj
#     def sign_in_block(self):
#          driver_obj.find_element("xpath", '//div[@class="fr signin-block  "]').click()
#     def sign_in(self):
#         driver_obj.find_element("xpath",'//li[text()="Sign In/Sign Up"]').click()
#     def signin_with_google(self):
#         ele = driver_obj.find_element("xpath", '//iframe[@class="modalIframe"]')
#         driver_obj.switch_to.frame(ele)
#         driver_obj.find_element("xpath", '//span[text()="Sign in with Google"]').click()
#     def create_account(self):
#         handles =driver_obj.window_handles
#         driver_obj.switch_to.window(handles[1])
#         driver_obj.find_element("xpath", '//span[text()="Create account"]').click()
#     def first_name(self):
#         ele1 = driver_obj.window_handles
#         driver_obj.switch_to.window(ele1[1])
#         ele2 = driver_obj.switch_to.default_content()
#         driver_obj.switch_to.frame(ele2)
#         time.sleep(2)
#         driver_obj.find_element("xpath", '//input[@name="firstName"]').send_keys("lakshmi")
#     def last_name(self):
#         driver_obj.find_element("xpath", '//input[@name="lastName"]').send_keys("prashanthi")
#     def user_name(self):
#         driver_obj.find_element("xpath", '//input[@name="Username"]').send_keys("prashanthilakshmi080")
#     def password(self):
#         driver_obj.find_element("xpath", '//input[@type="password"]').send_keys("shanthi@123")
#     def confirm_password(self):
#         driver_obj.find_element("xpath", '//input[@name="ConfirmPasswd"]').send_keys("shanthi@123")
#     def check_box(self):
#         driver_obj.find_element("xpath", '//input[@type="checkbox"]').click()
#     def next(self):
#         driver_obj.find_element("xpath", '//span[text()="Next"]').click()
#     def phonenumber(self):
#         obj1 = driver_obj.find_element("xpath", '//input[@class="VfPpkd-fmcmS-wGMbrd "]').send_keys("6300285557")
#         time.sleep(5)
#     def next1(self):
#         driver_obj.find_element("xpath", '//span[@class="VfPpkd-vQzf8d"]').click()  # to click on next
#         time.sleep(30)
#     def verication(self):
#         driver_obj.find_element("xpath", "//span[text()='Verify']").click()  # to click on verify
#     def day(self):
#         driver_obj.find_element("xpath", "//input[@name='day']").send_keys("28")
#     def month(self):
#         ele = driver_obj.find_element("xpath", "//select[@id='month']")
#         sel_obj = Select(ele)
#         sel_obj.select_by_visible_text("August")
#         time.sleep(2)
#     def date(self):
#         driver_obj.find_element("xpath", "//input[@name='year']").send_keys("2000")
#     def gender(self):
#         ele1 = driver_obj.find_element("xpath", "//select[@id='gender']")  # to select the gender
#         sel_obj1 = Select(ele1)
#         sel_obj1.select_by_visible_text("Female")
#     def next_2(self):
#         driver_obj.find_element("xpath", '//span[@class="VfPpkd-vQzf8d"]').click()  # to click on next
#         time.sleep(5)
#     def yes_i_agree(self):
#         driver_obj.find_element("xpath", '//span[text()="I agree"]').click()
# lg=Sign_in()
# lg.sign_in_block()
# lg. sign_in()
# lg.signin_with_google()
# lg.create_account()
# lg.first_name()
# lg.last_name()
# lg.user_name()
# lg.password()
# lg.confirm_password()
# lg.check_box()
# lg.next()
# lg.phonenumber()
# lg.next1()
# lg.verication()
# lg.day()
# lg.month()
# lg.date()
# lg.gender()
# lg.next_2()
# lg.yes_i_agree()