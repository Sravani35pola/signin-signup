import pytest
from selenium import webdriver
from LIBRARY.config import Config

#path=r"C:\Users\Sravani\Downloads\chromedriver_win32\chromedriver.exe"
# from webdriver_manager.chrome import ChromeDriverManager
# from webdriver_manager.microsoft import EdgeChromiumDriverManager
# from webdriver_manager.firefox import GeckoDriverManager

# from selenium.webdriver.firefox.options import  Options

# @pytest.fixture(params=["Chrome","Firefox","Edge"])

@pytest.fixture(params=["Chrome"])
def _driver(request):


    if request.param == "Chrome":
        # driver = webdriver.Chrome(ChromeDriverManager().install())
        driver = webdriver.Chrome(executable_path=Config.Chrome_Driver_Path)
        driver.get(Config.URL)
        driver.maximize_window()
        yield driver
        print(driver.title)

        # _driver.save_screenshot("fb_notifications.png")
        # driver.close()

    # elif request.param == "Firefox":
    #     driver = webdriver.Firefox(GeckoDriverManager().install())
    #     # driver = webdriver.Firefox(executable_path=Config.Firefox_Driver_Path)
    #
    # elif request.param == "Edge":
    #     driver = webdriver.Edge(EdgeChromiumDriverManager().install())
    #
    #     # driver = webdriver.Edge(executable_path=Config.Edge_Driver_Path)

    # driver.get(Config.URL)
    # driver.maximize_window()
    # yield driver
    # print(driver.title)
    # #_driver.save_screenshot("fb_notifications.png")
    # driver.close()

# import pytest
# from selenium import webdriver
# from LIBRARY.config import Config
#
# path=r"C:\Users\Sravani\Downloads\chromedriver_win32\chromedriver.exe"
# from webdriver_manager.chrome import ChromeDriverManager
# from webdriver_manager.microsoft import EdgeChromiumDriverManager
# from webdriver_manager.firefox import GeckoDriverManager
# from selenium.webdriver.firefox.options import  Options
#
# @pytest.fixture(params=["Chrome","Firefox","Edge"])
# def _driver(request):
#
#
#     if request.param == "chrome":
#         driver = webdriver.Chrome(ChromeDriverManager().install())
#          # driver = webdriver.Chrome(executable_path=Chrome_Driver_Path)
#
#     elif request.param == "Firefox":
#         driver = webdriver.Firefox(GeckoDriverManager().install())
#         # driver = webdriver.Firefox(executable_path=Config.Firefox_Driver_Path)
#
#     elif request.param == "Edge":
#         driver = webdriver.Edge(EdgeChromiumDriverManager().install())
#
#         # driver = webdriver.Edge(executable_path=Config.Edge_Driver_Path)
#
#     _driver.get(Config.URL)
#     _driver.maximize_window()
#     yield _driver
#     print(_driver.title)
#     _driver.save_screenshot("fb_notifications.png")
#     _driver.close()