import unittest

import HtmlTestRunner

from Tests.TEST_BASIC.BASIC_login import LoginTest

""" 테스트 로더로 테스트 케이스 생성 """
testcase = unittest.TestLoader().loadTestsFromTestCase(LoginTest)

""" 테스트 스위트 구성 """
testsuite = unittest.TestSuite([testcase])

""" 테스트 러너로 테스트 실행 """
HtmlTestRunner.HTMLTestRunner(
                              output="Reports",      # 보고서 생성할 폴더 이름
                              report_name="Report",     # HTML 파일 이름
                              report_title="Test Results",   # HTML 파일 타이틀
                              combine_reports=True  # True : 테스트 케이스가 여러개 일 때 보고서 하나로 합치기
                              ).run(testsuite)