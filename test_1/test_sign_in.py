import pytest
from DATA.reading_objects import ReadExcel
from POM.sign_in import Sign_in
from LIBRARY.config import Config

class TestSign_in:
    read_xl=ReadExcel()
    data=read_xl.read_test_data("data1")
    @pytest.mark.parametrize("number",data)
    def test_signin(self,number,_driver):
        lg = Sign_in(_driver)
        lg.sign_in_block()
        lg.sign_in()
        lg.iframe()
        lg.phonenumber(number)
        lg.recaptcha()
        lg.otp()
        lg.verify()
        # lg.username(name)
        # lg.user_mail(email)
        #lg.confirm()
    # @pytest.mark.parametrize("firstname,lastname,username,password,confirmpassword,phonenumber,day,date",data)
    # def test_signin(self,firstname,lastname,username,password,confirmpassword,phonenumber,day,date,_driver):
    #
    #     lg = Sign_in(_driver)
    #     lg.sign_in_block()
    #     lg.sign_in()
    #     lg.signin_with_google()
    #     lg.create_account()
    #     lg.first_name(firstname)
    #     lg.last_name(lastname)
    #     lg.user_name(username)
    #     lg.password(password)
    #     lg.confirm_password(confirmpassword)
    #     lg.check_box()
    #     lg.next()
    #     lg.phonenumber(phonenumber)
    #     lg.next1()
    #     lg.verication()
    #     lg.day(day)
    #     lg.month()
    #     lg.date(date)
    #     lg.gender()
    #     lg.next_2()
    #     lg.yes_i_agree()







































# from POM.sign_in import Sign_in
# class TestSign_in:
#     def test_signin(self):
#         lg = Sign_in()
#         lg.sign_in_block()
#         lg.sign_in()
#         lg.signin_with_google()
#         lg.create_account()
#         lg.first_name()
#         lg.last_name()
#         lg.user_name()
#         lg.password()
#         lg.confirm_password()
#         lg.check_box()
#         lg.next()
#         lg.phonenumber()
#         lg.next1()
#         lg.verication()
#         lg.day()
#         lg.month()
#         lg.date()
#         lg.gender()
#         lg.next_2()
#         lg.yes_i_agree()
