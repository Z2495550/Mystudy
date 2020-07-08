# coding=utf-8
import pytest
import allure
import os

@pytest.fixture(scope='session')
def login_fixture():
    print('前置条件登录')

@allure.step('步骤')
def step_01():
    print('操作步骤----1')


@allure.step('步骤')
def step_02():
    print('操作步骤----2')


@allure.step('步骤')
def step_03():
    print('操作步骤----3')

@allure.epic('epic对大Story得一个描述性的标签')
@allure.feature('测试模块1')
class TestAllure():

    @allure.testcase('https://www.baidu.com')
    @allure.issue('http://www.baidu.com')
    @allure.title('用例的标题')
    @allure.story('用户故事：1')
    @allure.severity("critical")
    def test_case_01(self,login_fixture):
        '''
        1、打开网站
        2、操作1，操作2，操作3
        '''
        step_01()
        step_02()
        step_03()

    @allure.story('用户故事：2')
    def test_case_02(self,login_fixture):
        print('测试用例1')
        step_01()
        step_03()

@allure.epic("epic对大Story的一个描述性标签")
@allure.feature("测试模块2")
class TestDemo2():


    @allure.story("用户故事：3")
    def test_case_3(self, login_fixture):
        print("测试用例1")
        step_01()


    @allure.story("用户故事：4")
    def test_case_4(self, login_fixture):
        print("测试用例1")
        step_03()

if __name__ == '__main__':
    # 执行pytest单元测试，生成 Allure 报告需要的数据存在 /report/xml 目录
    pytest.main(['-s','-q','test_allure_02.py','--alluredir','../report/xml'])
    # 执行命令生成测试报告
    os.system('allure generate ../report/xml -o ../report/html --clean')

