import pytest
from selenium.webdriver.chrome import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


def test_search():
    drw = webdriver.WebDriver('/Users/somet1me/Desktop/r2d2/webdriver/chromedriver')
    print(1)
    drw.get('http://www.google.ru')
    drw.maximize_window()
    print(2)
    element = WebDriverWait(drw, 20)\
        .until(expected_conditions.
               presence_of_element_located((By.XPATH, '//div[@aria-label="Голосовой поиск"]/../..//input')))
    print(3)

    element.send_keys('selenide', Keys.ENTER)
    print(4)
    element = wait_and_get_element('(//h3)[1]/..', driver=drw)
    str = element.get_attribute('href')

    if str == 'https://ru.selenide.org/':
        print('УРААААААА')
    else:
        pytest.fail(f'Ссылка "{str}" не совпадает с ожидаемым результатом "https://ru.selenide.org/"')

def tearDown(self):
    self.drw.close()


def wait_and_get_element(xpath, driver) -> WebElement:
    locator = (By.XPATH, xpath)
    WebDriverWait(driver=driver, timeout=20) \
        .until(expected_conditions.
               presence_of_element_located(locator=locator))
    element = driver.find_element_by_xpath(xpath=xpath)
    return element
