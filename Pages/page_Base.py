from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    """ 모든 페이지에서 공통으로 사용할 메서드를 정의한다 """
    def __init__(self, driver):
        self.driver = driver

    # 엘러먼트를 클릭
    def click(self, by_locator):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).click()

    # 엘러먼트에 키를 입력
    def send_keys(self, by_locator, text):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).send_keys(text)


