from TestBase.WebDriverSetup import WebDriverSetup
from Pages.page_splash import SplashPage


class LoginTest(WebDriverSetup):

    def test_runapp(self):

        # 스플래시 페이지 객체 생성
        splash = SplashPage(self.driver)
        splash.do_click(SplashPage.btn_positive)