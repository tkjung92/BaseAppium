from appium.webdriver.common.mobileby import MobileBy


class BasePage(object):
    """각 페이지 오브젝트 초기화시켜주는 BasePage 클래스 구현"""
    def __init__(self, driver):
        self.driver = driver


class SplashPage(BasePage):
    """Splash Page 오브젝트 생성"""

    # 스플래시 화면에서 등장하는 버튼 정의
    btn_positive = (MobileBy.ID, "com.mrt.ducati.dev:id/btn_positive")

    # 스플래시 화면에서 등장하는 버튼 클릭 메서드 구현
    def click_positive_btn(self):
        self.driver.find_element(SplashPage.btn_positive).click()
