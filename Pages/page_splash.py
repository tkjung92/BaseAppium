from .page_Base import BasePage
from appium.webdriver.common.mobileby import MobileBy


class SplashPage(BasePage):

    # 스플래시 화면에서 등장하는 버튼 정의
    btn_positive = (MobileBy.ID, "com.mrt.ducati.dev:id/btn_positive")