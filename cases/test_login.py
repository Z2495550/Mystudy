import pytest
import allure

class TestLogin:

    @allure.feature('test_login_01')
    @allure.story('test_story_03')
    @allure.severity('normal')
    def test_001(self):
        """
        用例描述：这是用例描述，Test case 001，第01条测试用例
        """
        print('测试用例一')
        assert 1 ==1

    @allure.feature('test_login_01')
    @allure.story('test_story_04')
    @allure.severity('minor')
    def test_002(self):
        """
        用例描述：这是用例描述，Test case 002，第002条测试用例
        """
        print('测试用例二')
        assert 2 == 2

    @allure.feature('test_login_01')
    @allure.story('test_story_05')
    @allure.severity('trivial')
    def test_003(self):
        """
        用例描述：这是用例描述，Test case 003，第003条测试用例
        """
        print('测试用例三')
        assert 1 == 2

if __name__ == '__main__':
    pytest.main(['-s','-q','--alluredir','../report/xml'])
