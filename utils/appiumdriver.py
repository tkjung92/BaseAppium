import time
import unittest
import os
import warnings

from appium import webdriver


class Driver(unittest.TestCase):

    def setUp(self):
        warnings.filterwarnings("ignore", category=ResourceWarning) # 세션 유지로 인한 리소스 워닝 로그 무시
        app = os.path.join(os.path.dirname(__file__), '/Users/taekyeong.jung/Desktop/workspace/','myrealtrip.apk')
        app = os.path.abspath(app)
        self.driver = webdriver.Remote(
            command_executor='http://127.0.0.1:4723/wd/hub',
            desired_capabilities={ #https://appium.io/docs/en/writing-running-appium/caps/
                'app': app,
                'platformName': 'Android',
                'udid': 'emulator-5554',
                'platformVersion': '11.0',
                'automationName': 'uiautomator2',
                'appPackage': 'com.mrt.ducati.dev',
                'appActivity': 'com.mrt.ducati.LauncherActivity',
                'chromeOptions': {'w3c': False}
            })
        self.driver.implicitly_wait(10)

    def tearDown(self):
        time.sleep(2)
        print("TearDown")
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
