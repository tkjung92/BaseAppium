from utils.appiumdriver import Driver
from page.splash import SplashPage


class LoginTest(Driver):
    def testcase_1(self):
        """실제 테스트 케이스 스크립트 작성 영역"""

        # 스플래시 페이지 객체 생성
        splash = SplashPage(self.driver)

        # 생성된 객체로 클릭 메서드 호출
        splash.click_positive_btn()
