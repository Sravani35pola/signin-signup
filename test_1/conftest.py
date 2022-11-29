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


    #if request.param == "Edge":
    #     # driver = webdriver.Chrome(ChromeDriverManager().install())
         #driver = webdriver.Edge(executable_path=Config.Edge_Driver_path)


    # elif request.param == "Firefox":
    #     driver = webdriver.Firefox(GeckoDriverManager().install())
    #     # driver = webdriver.Firefox(executable_path=Config.Firefox_Driver_Path)

    if request.param == "Chrome":
    #     driver = webdriver.Edge(EdgeChromiumDriverManager().install())
    #
         driver = webdriver.Chrome(executable_path=Config.Chrome_Driver_Path)
    #driver = webdriver.Chrome(executable_path=Config.Chrome_Driver_Path)
    driver.get(Config.URL)
    driver.maximize_window()
    yield driver
    print(driver.title)

