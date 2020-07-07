# -*- coding: utf-8 -*-
import allure
import pytest


@allure.feature('test_module_01')
@allure.story('test_story_01')
@allure.severity('blocker')
#test_case_01为用例title
def test_case_01():
    """
    用例描述：这是用例描述，Test case 01，第一条测试用例
    """
    assert 0

@allure.feature('test_module_01')
@allure.story('test_story_02')
@allure.severity('critical')
def test_case_02():
    """
    用例描述：这是用例描述，Test case 02，第二条测试用例
    """
    assert 0 == 0


if __name__ == '__main__':
    pytest.main(['-s', '-q', '--alluredir', '../report/xml'])